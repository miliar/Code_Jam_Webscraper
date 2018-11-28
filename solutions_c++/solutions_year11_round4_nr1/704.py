#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <ctime>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = a; i < (int)(b); ++i)
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(a) a.begin,a.end()
#define ll long long
#define fs first
#define EPS 1e-12
#define sc second

//int a[1234567];
pair<int, pair<int, int> > p[1234];

int main(){
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int t;
	cin >> t;
	forn(tt, t){
		int x, s, r, tm, n;
		cin >> x >> s >> r >> tm >> n;
		//memset(a, 0, sizeof a);
		int len = 0;
		forn(i, n){
			scanf("%d %d %d", &p[i].sc.fs, &p[i].sc.sc, &p[i].fs);
			len += p[i].sc.sc - p[i].sc.fs;
		}
		p[n].fs = 0;
		p[n].sc.sc = x - len;
		p[n].sc.fs = 0;
		sort(p, p + n + 1);
		//reverse(p, p + n + 1);


		long double time_use = tm;
		long double res = 0;
		forn(i, n + 1){
			long double to_run = (p[i].sc.sc - p[i].sc.fs) / (0. + r + p[i].fs);
			if(to_run <= time_use) {
				time_use -= to_run;
				res += to_run;
				continue;
			}
			// to_run > time_use
			long double dist = (p[i].sc.sc - p[i].sc.fs);
			if(fabsl(time_use) > EPS) {
				long double xx = time_use * (r + p[i].fs);
				dist -= xx;
				res += time_use;
				time_use = 0;
			}
			res += dist / (s + p[i].fs);
		}
		printf("Case #%d: %.12lf\n", tt + 1, res);
	}

	
	return 0;
}