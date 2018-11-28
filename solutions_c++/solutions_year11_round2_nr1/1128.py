#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

typedef pair<bool, bool> bb;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<bb> vbb;
typedef vector<ii> vii;
typedef vector<vector<int> > vvi;

typedef unsigned long long ull;


double calc_WP(const vvi& sched, int team)
{
	int total = 0, count = 0, n = sched.size();
	for (int i = 0; i < n; ++i) {
		if (sched[team][i] == -1) continue;
		total += sched[team][i];
		count++;
	}
	return (double) total / count;
}


double calc_OWP(const vvi& sched, int team)
{
	double total = 0;
	int count = 0, n = sched.size();
	for (int i = 0; i < n; ++i) {
		if (sched[team][i] == -1) continue;
		int total1 = 0, count1 = 0;
		for (int j = 0; j < n; ++j) {
			if (j == team) continue;
			if (sched[i][j] == -1) continue;
			total1 += sched[i][j];
			count1++;
		}
		total += (double) total1 / count1;
		count++;
	}
	return (total / count);
}


double calc_OOWP(const vvi& sched, const vd& OWP, int team)
{
	double total = 0;
	int count = 0, n = sched.size();
	for (int i = 0; i < n; ++i) {
		if (sched[team][i] == -1) continue;
		total += OWP[i];
		count++;
	}
	return (total / count);
}


double calc_RTI(const vd& WP, const vd& OWP, const vd& OOWP, int team)
{
	return (0.25 * WP[team] + 0.50 * OWP[team] + 0.25 * OOWP[team]);
}


int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N;
		cin >> N;
		vvi sched(N, vi(N));
		for (int n = 0; n < N; ++n) {
			for (int m = 0; m < N; ++m) {
				char x;
				cin >> x;
				if (x == '1') sched[n][m] = 1;
				if (x == '0') sched[n][m] = 0;
				if (x == '.') sched[n][m] = -1;
			}
		}
		cout << "Case #" << t << ":\n";
		vd WP(N), OWP(N), OOWP(N);
		for (int n = 0; n < N; ++n) {
			WP[n] = calc_WP(sched, n);
			//cout << "WP[n]=" << WP[n] << endl;
		}
		for (int n = 0; n < N; ++n) {
			OWP[n] = calc_OWP(sched, n);
			//cout << "OWP[n]=" << OWP[n] << endl;
		}
		for (int n = 0; n < N; ++n) {
			OOWP[n] = calc_OOWP(sched, OWP, n);
			//cout << "OOWP[n]=" << OOWP[n] << endl;
		}
		for (int n = 0; n < N; ++n) {
			printf("%.10lf\n", calc_RTI(WP, OWP, OOWP, n));
		}
	}
	
	return 0;
}
