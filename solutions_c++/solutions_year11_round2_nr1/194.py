#include <iostream>
#include <cstdio>

using namespace std;

char in[110][110];
int wn[110], num[110];
double wp[110], owp[110], oowp[110];

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		int n;
		cin >> n;
		for(int i = 0; i < n; ++i) scanf("%s", in[i]);
		printf("Case #%d:\n", t);
		for(int i = 0; i < n; ++i) {
			num[i] = wn[i] = 0;
			for(int j = 0; j < n; ++j) {
				if(in[i][j] == '.') continue;
				++num[i];
				if(in[i][j] == '1') ++wn[i];
			}
			wp[i] = wn[i] / (double)num[i];
		}
		for(int i = 0; i < n; ++i) {
			double sum = 0;
			for(int j = 0; j < n; ++j) {
				if(in[i][j] == '.') continue;
				if(in[i][j] == '1') sum += wn[j] / (double)(num[j] - 1);
				else sum += (wn[j] - 1) / (double)(num[j] - 1);
			}
			owp[i] = sum / num[i];
		}
		for(int i = 0; i < n; ++i) {
			double sum = 0;
			for(int j = 0; j < n; ++j) {
				if(in[i][j] == '.') continue;
				sum += owp[j];
			}
			oowp[i] = sum / num[i];
		}
		for(int i = 0; i < n; ++i) {
			printf("%.10f\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
	}
	return 0;
}
