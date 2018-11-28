#define _CRT_SECURE_NO_DEPRECATE
#define _ASSERTE

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <ctime>
#include <queue>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = a; i < (int)(b); ++i)
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(a) a.begin,a.end()
#define ll long long
#define INF 1e9
#define EPS 1e-8

int d[10345], l[10345];
int can[10345];

int main(){
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int t;
	cin >> t;
	forn(tt, t){
		cerr << tt + 1 << endl;
			
		int n;
		cin >> n;
		forn(i, n)
			scanf("%d %d", &d[i], &l[i]);

		memset(can, 0, sizeof can);

		can[0] = d[0];
		l[n] = 1;
		scanf("%d", &d[n]);
		forn(i, n) {
			if (can[i]) {
				for(int j = i + 1; j <= n; j++) {
					if (d[j] - d[i] > can[i]) break;
					can[j] = max(can[j], min(l[j], d[j] - d[i]));
				}
			}
		}

		cout << "Case #" << (tt + 1) << ": " << (can[n] ? "YES\n" : "NO\n");
		
	}
	
	return 0;
}