#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include<iostream>
#include<fstream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<list>
#include<map>
#include<deque>
#include<stack>
#include<queue>
#include<string>
#include<sstream>
#include<time.h>
#include<numeric>
#include<functional>

using namespace std;
#define _CRT_SECURE_NO_WARNINGS
#define INF  ((1 << 31) - 1)
#define LLINF  ((ll)((1LL << 63) - 1))
#define eps 0.00000001
#define million 1000000
#define PI 3.14159265358979323846
#define sz(v) ((int)(v).size())
#define MP make_pair
#define PB push_back
#define all(v) (v).begin(), (v).end()
typedef long long ll;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int id = 0; id < T; ++id) {
		cout << "Case #" << id + 1 <<": ";
		int n;cin >> n;
		vector<int> x;
		vector<int> y;
		vector<double> r;
		for (int i = 0; i < n; ++i) {
			int a,b,c;
			cin >> a>> b >> c;
			x.PB(a);
			y.PB(b);
			r.PB(c);
		}
		if (n == 1) {
			cout << r[0] << "\n";
			continue;
		}
		if (n == 2) {
			cout << max(r[0], r[1]) << "\n";
		}
		if (n == 3) {
			double dist[3][3];
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < n; ++j) {
					dist[i][j] = sqrt(1.0 * (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]));
				}
			}
			double res = 10000000000.0;
			res = min(res, max(r[0], (dist[1][2] + r[1]+ r[2])) / 2.0);
			res = min(res, max(r[1], (dist[0][2] + r[0]+ r[2])) / 2.0);
			res = min(res, max(r[2], (dist[0][1] + r[0]+ r[1])) / 2.0);
			printf("%lf\n", res);
		}
	}
	return 0;
}