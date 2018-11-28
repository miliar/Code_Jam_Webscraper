#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
using namespace std;

void solve()
{
	int N;
	cin >> N;
	vector<string> result(N);
	vector<int> a(N, 0);
	vector<int> b(N, 0);
	vector<double> wp(N, 0);
	vector<double> owp(N, 0);
	vector<double> oowp(N, 0);
	vector<double> rpi(N, 0);
	
	for (int i = 0; i < N; ++i) cin >> result[i];
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			if (result[i][j] == '1') ++a[i], ++b[i];
			else if (result[i][j] == '0') ++b[i];
		}
		wp[i] = (double) a[i] / (double) b[i];
		//printf("wp[%d] = %f\n", i, wp[i]);
	}
	
	for (int i = 0; i < N; ++i) {
		int c = 0;
		for (int j = 0; j < N; ++j) {
			if (result[i][j] == '.') continue;
			if (result[j][i] == '1') {
				owp[i] += (double) (a[j] - 1) / (double) (b[j] - 1);
			} else {
				owp[i] += (double) (a[j]) / (double) (b[j] - 1);
			}
			++c;
		}
		owp[i] /= (double) c;
		//printf("owp[%d] = %f\n", i, owp[i]);
	}
	for (int i = 0; i < N; ++i) {
		int cnt = 0;
		for (int j = 0; j < N; ++j) {
			if (result[i][j] == '.') continue;
			oowp[i] += owp[j];
			++cnt;
		}
		oowp[i] /= (double) cnt;
		//printf("oowp[%d] = %f\n", i, oowp[i]);
	}
	for (int i = 0; i < N; ++i) {
		rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
		printf("%.12f\n", rpi[i]);
	}
}

int main()
{
	int T;
	int N, PD, PG;
	
	cin >> T;
	
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ": " << endl;
		solve();
	}
	return 0;
}