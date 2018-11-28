#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
vector<string> a;
double owp[101][101];

int main() {
	int testCnt;
	cin >> testCnt;
	for (int T = 0; T < testCnt; ++T) {
		int n;
		cin >> n;
		a.clear();
		memset(owp, 0, sizeof owp);

		for (int i = 0; i < n; ++i) {
			string s;
			cin >> s;
			a.push_back(s);
		}
		for (int i = 0; i < n; ++i) {
			double gw = 0, gl = 0;
			for (int j = 0; j < n; ++j) {
				if (a[i][j] == '.') continue;
				if (a[i][j] == '0') ++gl; else ++gw;
			}
			for (int j = 0; j < n; ++j) {
				double ggw = gw, ggl = gl;
				if (a[i][j] == '0') --ggl; 
				if (a[i][j] == '1') --ggw;
				owp[i][j] = ggw / (ggw+ggl);
			}
		}
		cout << "Case #" << T+1 << ":" << endl;
		for (int i = 0; i < n; ++i) {
			double gw = 0, gl = 0;
			for (int j = 0; j < n; ++j) {
				if (a[i][j] == '.') continue;
				if (a[i][j] == '0') ++gl; else ++gw;
			}
			if (gw+gl == 0) {
				cout << "0" << endl;
				continue;
			}

			double r = 0.25 * ((double)gw / (double)(gw+gl));
			double oowp = 0;
			for (int j = 0; j < n; ++j) {
				if (a[i][j] != '.')
					oowp += owp[j][i];		
			}
			r += 0.5 * oowp/(gw+gl);
			oowp = 0;
			int c = 0;
			for (int j = 0; j < n; ++j) {
				if (a[i][j] == '.')
					continue;
				c = 0;
				double t = 0;
				for (int k = 0; k < n; ++k) { 
					if (a[j][k] == '.') continue;
					++c; t += owp[k][j];
				}
				t /= c;
				oowp += t;
			}
			oowp = oowp / (gw+gl);
			r += 0.25 * oowp;
			cout << r << endl;
		}
	}
	return 0;
}