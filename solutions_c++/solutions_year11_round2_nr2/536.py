#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;


const int MAX_N = 204;
const double eps = 1e-8;

int C;
double D;
double result;

double p[MAX_N];
int v[MAX_N];

bool isAccepted(double m) {
	double now = -1e+8;
	for (int i = 0; i < C; ++i) {
		for (int j = 0; j < v[i]; ++j) {
			if (now < p[i] - m) {
				now = p[i] - m;
				continue;
			}
			if (now + D > p[i] + m) return false;
			now += D;
		}
	}
	return true;
}

void solve() {
	cin >> C >> D;
	for (int i = 0; i < C; ++i) {
		cin >> p[i] >> v[i];
	}

	double inf = 0.0, sup = 1e+13;
	while (inf + eps < sup) {
		double mid = (inf + sup) / 2;
		if (isAccepted(mid)) {
			result = mid;
			sup = mid;
		} else inf = mid;
	}

	cout << setprecision(8) << fixed << result << endl;
}

int main() {
	int nTest;
	cin >> nTest;
	for (int i = 1; i <= nTest; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;	
}

