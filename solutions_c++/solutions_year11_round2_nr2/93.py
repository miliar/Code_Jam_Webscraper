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

ll p[210], v[210];
int n, d;

inline bool check(ld m){
	ld maxx = -10000000000000.0;
	forn(i, n){
		forn(j, v[i]){
			ld max1 = max(maxx + d, p[i] - m);
			if (max1 > p[i] + m) return false;
			maxx = max1;
		}
	}
	return true;
}

ld bin(){
	ld l = 0, r = 10000000000000.0;
	forn(j, 150){
		ld m = (l + r) / 2;
		if (check(m)) r = m;
		else l = m;
	}
	return l;
}

int main(){
#ifndef ONLINE_JUDGE
	freopen ("input.txt","rt",stdin);
	freopen ("output.txt","wt",stdout);
#endif
	int t;
	cin >> t;
	forn(qqq, t){
		printf ("Case #%d: ", qqq + 1);
		cin >> n >> d;
		forn(i, n)
			cin >> p[i] >> v[i];
		printf ("%0.10f\n", bin());
	}
	return 0;
}