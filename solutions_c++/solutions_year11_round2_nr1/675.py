#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;
#define forn(i,n) for(int i=0; i<(n); i++)


double cal_rpi(double wp, double owp, double oowp) {
	return 0.25 * wp + 0.5 * owp + 0.25 * oowp;
}
double cal_wp(double k, string &s) {
	int win = 0, lose = 0;
	forn(i, s.size()) {
		if(s[i] == '1') win ++;
		if(s[i] == '0') lose ++;
	}
	return 1.0 * win / (win + lose);
}
double cal_owp(int k, vector<string> &g) {
	int teams = 0; double tot_wp = 0;
	forn(i, g.size()) {
		if(g[k][i] != '.') { // opnet
			int win = 0, lose = 0;
			forn(j, g.size()) if(j != k) {
				if(g[i][j] == '1') win ++;
				if(g[i][j] == '0') lose ++;
			}
			teams ++;
			tot_wp += 1.0 * win / (win + lose);
		}
	}
	return tot_wp / teams;
}
double cal_oowp(int k, string &s, vector<double> &owp) {
	int teams = 0; double tot_owp = 0;
	forn(i, s.size()) {
		if(s[i] != '.') {
			teams ++;
			tot_owp += owp[i];
		}
	}
	return tot_owp / teams;
}
int main() {
   freopen("A-large.in", "r", stdin);
   freopen("out.txt", "w", stdout);
   int ncase; cin >> ncase;
   forn(icase, ncase) {
		int teams; cin >> teams;
		vector<string> g(teams);
		forn(i, teams) cin >> g[i];
		
		vector<double> wp(teams);
		forn(t, teams) wp[t] = cal_wp(t, g[t]);

		vector<double> owp(teams);
		forn(t, teams) owp[t] = cal_owp(t, g);

		vector<double> oowp(teams);
		forn(t, teams) oowp[t] = cal_oowp(t, g[t], owp);

		//forn(t, teams) cout << wp[t] << " " << owp[t] << " " << oowp[t] << endl;

		printf("Case #%d:\n", icase+1);
		forn(t, teams) printf("%lf\n", cal_rpi(wp[t], owp[t], oowp[t]));
   }
}
	