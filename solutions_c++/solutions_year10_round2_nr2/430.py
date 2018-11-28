#include <iostream>
#include <cstring>

using namespace std;

const double eps = 1e-8;

double b, t;
int n, need;
double x[51], v[51];
bool ok[51];

int main (int argc, char * const argv[])
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int testcace;
	cin >> testcace;
	for (int test = 1; test <= testcace; test++) {
		cin >> n >> need >> b >> t;
		for (int i = 0; i < n; i++) cin >> x[i];
		for (int i = 0; i < n; i++) cin >> v[i];
		memset(ok, 0, sizeof(ok));
		int ans = 0;
		for (int i = n - 1; i >= 0; i--) {
			if (need == 0) break;
			if ((b - x[i]) / v[i] < t + eps) {
				need--;
				for (int j = i + 1; j < n; j++)
					if (!ok[j]) ans++;
				ok[i] = true;
			}
		}
		cout << "Case #" << test << ": ";
		if (need > 0) cout << "IMPOSSIBLE" << endl; else cout << ans << endl;
	}
}
