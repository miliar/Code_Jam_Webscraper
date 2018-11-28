#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <ctime>
#include <deque>

#define forn(i, n) for (int i = 0; i < int(n); i ++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i --)
#define mp make_pair
#define pb push_back
#define pi 3.1415926535897932
#define ll long long
#define ld long double

using namespace std;

char a[510][510];
int r, c, d;

inline ld abs1 (ld b){
	if (b < 0) return -b;
	return b;
}

bool check(int l, int x, int y){
	pair<ld, ld> m = mp(1.0 * (2 * x + l - 1) / 2.0, 1.0 * (2 * y + l - 1) / 2.0), st = mp(0, 0);  
	for (int i = x; i < x + l; i ++)
		for (int j = y; j < y + l; j ++){
			if ((i == x && j == y) || (i == x + l - 1 && j == y) || (i == x && j == y + l - 1) || (i == x + l - 1 && j == y + l - 1)) continue; 
			st.first += (1.0 * i - m.first) * (d + int(a[i][j]) - '0');
			st.second += (1.0 * j - m.second) * (d + int(a[i][j]) - '0');
		}
	return (abs1(st.first) < 0.0000000001 && abs1(st.second) < 0.0000000001);
}

int main(){
#ifndef ONLINE_JUDGE
	freopen ("input.txt","rt",stdin);
	freopen ("output.txt","wt",stdout);
#endif
	int t1;
	cin >> t1;
	forn(qqq, t1){
		scanf("%d %d %d\n", &r, &c, &d);	
		bool q = false;
		forn(i, r){
			forn(j, c)
				scanf("%c", &a[i][j]);
			scanf("\n");
		}
		for (int i = min(r, c); i >= 3; i --){
			for (int j = 0; j + i <= r; j ++)
				for (int k = 0; k + i <= c; k ++)
					if (!q && check(i, j, k)){
						printf ("Case #%d: %d\n", qqq + 1, i);
						q = true;
						break;
					}
		}
		if (!q) printf ("Case #%d: IMPOSSIBLE\n", qqq + 1);
	}
	return 0;
}