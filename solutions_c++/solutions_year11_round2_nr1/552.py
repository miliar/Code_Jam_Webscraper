#include <iostream>
#include <iomanip>

using namespace std;

const int MAX_N = 104;

char c[MAX_N][MAX_N];
double wp[MAX_N], owp[MAX_N], oowp[MAX_N];
int cm[MAX_N], countWin[MAX_N];
int n;

void solve() {
	cin >> n;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> c[i][j];
		}
	}
	memset(wp, 0.0, sizeof(wp));
	memset(owp, 0.0, sizeof(owp));
	memset(owp, 0.0, sizeof(oowp));
	memset(cm, 0, sizeof(cm));
	memset(countWin, 0, sizeof(countWin));

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if (c[i][j] == '.') continue;
			if (c[i][j] == '1') ++countWin[i];
			++cm[i];
		}
		wp[i] = countWin[i]*1.0 / cm[i];
	}

	for (int i = 0; i < n; ++i) {
		double total = 0.0;
		for (int j = 0; j < n; ++j) {
			if (c[i][j] == '.') continue;
			if (c[i][j] == '1') {
				total += (countWin[j]*1.0) / (cm[j]-1);
			} else {
				total += (countWin[j]-1)*1.0 / (cm[j]-1);
			}
		}
		owp[i] = total / cm[i];
	}

	for (int i = 0; i < n; ++i) {
		double total = 0.0;
		for (int j = 0; j < n; ++j) {
			if (c[i][j] == '.') continue;
			total += owp[j];
		}
		oowp[i] = total / cm[i];
	}

	for (int i = 0; i < n; ++i) {
//		cout << wp[i] << " # " << owp[i] << " # " << oowp[i] << endl;
		cout << setprecision(8) << fixed << (0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i]) << endl;
	}
}

int main() {
	int nTest;
	cin >> nTest;
	for (int i = 1; i <= nTest; ++i) {
		cout << "Case #" << i << ":" << endl;
		solve();
	}
	return 0;
}


