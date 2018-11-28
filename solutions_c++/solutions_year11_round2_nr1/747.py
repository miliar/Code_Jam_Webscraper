#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <algorithm>
#include <limits>

#define px first
#define py second
#define mp make_pair

using namespace std;

const int INF = numeric_limits<int>::max();

int caseNum;

void solve()
{
	int n;
	scanf("%d\n", &n);
	vector<vector<char> > shedule(n, vector<char>(n));
	vector<int> sumWin(n, 0);
	vector<double> wp(n), owp(n), oowp(n), rpi(n);
	vector<vector<int> > opponents(n);
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			scanf("%c", &shedule[i][j]);
		}
		scanf("\n");
	}
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if (shedule[i][j] != '.') {
				opponents[i].push_back(j);
				if (shedule[i][j] == '1') {
					sumWin[i]++;
				}
			}
		}
	}
	for (int i = 0; i < n; ++i) {
		wp[i] = 1.0 * sumWin[i] / opponents[i].size();
	}
	for (int i = 0; i < n; ++i) {
		double owr = 0;
		for (size_t j = 0; j < opponents[i].size(); ++j) {
			int won;
			if (shedule[i][opponents[i][j]] == '0') {
				won = 1;
			} else {
				won = 0;
			}
			owr += 1.0 * (sumWin[opponents[i][j]] - won) / (opponents[opponents[i][j]].size() - 1);
		}
		owp[i] = owr / opponents[i].size();
	}
	for (int i = 0; i < n; ++i) {
		double oowr = 0;
		for (size_t j = 0; j < opponents[i].size(); ++j) {
			oowr += owp[opponents[i][j]];
		}
		oowp[i] = oowr / opponents[i].size();
	}
	for (int i = 0; i < n; ++i) {
		rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
	}
	for (int i = 0; i < n; ++i) {
		printf("%0.7lf\n", rpi[i]);
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n", &caseNum);
	for (int i = 0; i < caseNum; ++i) {
		printf("Case #%d:\n", i + 1);
		solve();
	}
	return 0;
}