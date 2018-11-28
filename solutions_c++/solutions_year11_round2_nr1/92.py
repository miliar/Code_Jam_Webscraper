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

char a[200][200];
pair<int, int> wp[200];
ld owp[200], oowp[200];

int main(){
#ifndef ONLINE_JUDGE
	freopen ("input.txt","rt",stdin);
	freopen ("output.txt","wt",stdout);
#endif
	int t;
	cin >> t;
	forn(qqq, t){
		int n;
		scanf("%d\n", &n);
		forn(i, n){
			wp[i].first = wp[i].second = owp[i] = oowp[i] = 0;
			forn(j, n)
				scanf("%c", &a[i][j]);
			scanf("\n");
		}
		printf ("Case #%d:\n", qqq + 1);
		forn(i, n)
			forn(j, n)
				if (a[i][j] == '1'){
					wp[i].first ++;
					wp[i].second ++;
				} else if (a[i][j] == '0')
					wp[i].second ++;
		forn(i, n){
			ld s = 0;
			forn(j, n){
				if (i == j || a[i][j] == '.') continue;
				pair<int, int> k = wp[j];
				if (a[i][j] == '1') k.second --;
				else if (a[i][j] == '0'){
					k.first --;
					k.second --;
				}
				s += (1.0 * k.first) / (1.0 * k.second);	
			}
			owp[i] = s / (1.0 * wp[i].second);
		}
		forn(i, n){
			ld s = 0;
			forn(j, n){
				if (i == j || a[i][j] == '.') continue;
				s += owp[j];
			}
			oowp[i] = s / (1.0 * wp[i].second);
		}
		forn(i, n)
			printf ("%0.10f\n", 0.25 * wp[i].first / wp[i].second + 0.5 * owp[i] + 0.25 * oowp[i]);
	}
	return 0;
}