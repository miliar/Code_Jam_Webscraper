#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;
#define forn(i,n) for(int i=0; i<(n); i++)


int main() {
   freopen("A-large.in", "r", stdin);
   freopen("out.txt", "w", stdout);
   int ncase; cin >> ncase;
   forn(icase, ncase) {
		int L, walk, run, add, m;
		cin >> L >> walk >> run >> add >> m;
		vector<int> B(m), E(m), speed(m);
		forn(im, m) {
			cin >> B[im] >> E[im] >> speed[im];
			L -= (E[im]- B[im]);
		}
		B.push_back(0);E.push_back(L);speed.push_back(0); m++;
		double res = 0.0, left = add * 1.0;
		vector<bool> used(m, false);
		forn(im, m) {
			int max_speed = 1e9, pos = 0;
			forn(i, m) if(speed[i] < max_speed && !used[i]) {
				pos = i; 
				max_speed = speed[i];
			}
			double run_time = 1.0 * (E[pos]-B[pos]) / (speed[pos]+run);
			//L -= (E[pos]-B[pos]);
			if(run_time > left) {
				res += left; // as run
				res += 1.0*((E[pos]-B[pos]) - left*(speed[pos]+run)) / (speed[pos]+walk);
				left = 0.0;
			} else {
				res += run_time;
				left -= run_time;
			}
			used[pos] = true;
		}
		//printf("%lf\n", left);
	//	res += 1.0 * L / walk;
		printf("Case #%d: %.9lf\n", icase+1, res);
   }
}
	