#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
#include <stack>
#include <string>
#include <cctype>
using namespace std;

#define sz(a) int((a).size())
#define dump(a) cerr << #a << " = " << a << endl
#define rep(i, b, e) for((i) = (b); (i) < (e); ++(i))

typedef unsigned long long ull;
typedef long long ll;

int main()
{
	int tests, test;
	cin >> tests;
	cout.setf(ios::fixed);
	cout.precision(13);
	rep(test, 0, tests) {
		int n, i, j;
		cin >> n;
		vector <vector <char> > a(n, vector <char> (n));
		rep(i, 0, n) 
			rep(j, 0, n)
				cin >> a[i][j];
		vector <double> wp(n), ans(n), owp(n), oowp(n);
		vector <vector <int> > rivals(n);
		vector <double> pl(n, 0), won(n, 0);
		rep(i, 0, n) {
			rep(j, 0, n) {
				if (a[i][j] == '1') { ++won[i]; ++pl[i]; }
				if (a[i][j] == '0') { ++pl[i]; }
				if (a[i][j] != '.') rivals[i].push_back(j);
			}
			wp[i] = won[i] / pl[i];
		}
		int k;
		rep(i, 0, n) {
			double sum = 0;
			rep(j, 0, sz(rivals[i])) {
				int riv = rivals[i][j];
				double oppwon = won[riv];
				double opppl = pl[riv] - 1;
				if (a[riv][i] == '1') --oppwon;
				sum += oppwon / opppl;
			}
			owp[i] = sum / sz(rivals[i]);
		}
		rep(i, 0, n) {
			double t = 0;
			rep(j, 0, sz(rivals[i])) {
				t += owp[rivals[i][j]];
			}
			oowp[i] = t / sz(rivals[i]);
		}
		cout << "Case #" << test + 1 << ":" << endl;
		rep(i, 0, n)
			cout << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
	}
	return 0;
}
