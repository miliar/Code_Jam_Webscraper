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

#define forn(i, n) for (int i = 0; i < n; i ++)
#define ford(i, n) for (int i = n - 1; i >= 0; i --)
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define pi 3.1415926535897932
#define ll long long
#define ld long double

using namespace std;

int kol[32];

int main(){
#ifndef ONLINE_JUDGE
	freopen ("input.txt","rt",stdin);
	freopen ("output.txt","wt",stdout);
#endif
	int t;
	cin >> t;
	forn(qqq, t){
		int n;
		memset(kol, 0, sizeof(kol));
		cin >> n;
		int minn = 1000000000, sum = 0;
		forn(i, n){
			int t1;
			scanf("%d", &t1);
			sum += t1;
			minn = min(minn, t1);
			forn(j, 32)
				if ((t1 & (1 << j)) != 0) kol[j] ++;
		}
		printf ("Case #%d: ", qqq + 1);
		bool q = true;
		forn(i, 32)
			if (kol[i] & 1){
				printf ("NO\n");
				q = false;
				break;
			}
		if (q) cout << sum - minn << endl;
	}
	return 0;
}