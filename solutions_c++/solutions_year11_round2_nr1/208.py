#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define For(i, a, b) for (int i = (a); i < (b); ++i)
#define Fod(i, a, b) for (int i = (a); i >= (b); --i)
#define Rep(i, a) for (int i = 0; i < (a); ++i)
#define sz(a) ((int)((a).size()))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(a) (a).begin(), (a).end()
#define Sort(a) sort(all(a))

typedef long long ll;
typedef pair <int, int> pii;

double owp[100];
double wp[100];

int main(int argc, char ** argv)
{
	if (argc > 1)
		freopen(argv[1], "r", stdin);
	int T;
	scanf("%d", &T);
	Rep(t, T) {
		printf("Case #%d:\n", t + 1);
		int n;
		scanf("%d\n", &n);
		vector <vector <char> > a(n, vector <char> (n));
		vector <int> w(n);
		vector <int> num(n);
		Rep(i, n) {
			Rep(j, n) {
				scanf("%c", &a[i][j]);
				if (a[i][j] != '.') {
					if (a[i][j] == '1') {
						++w[i];
					}
					++num[i];
				}
			}
			scanf("\n");
		}
		vector <double> wp(n);
		Rep(i, n) {
			double wps = 0;
			int wpn = 0;
			Rep(j, n) {
				if (a[i][j] != '.') {
					wps += (w[j] - (a[j][i] == '1' ? 1 : 0)) / (num[j] - 1.0);
					++wpn;
				}
			}
			owp[i] = wps / wpn;
		}
		Rep(i, n) {
			double score = w[i] / (double)num[i] / 4 + owp[i] * 0.5;
			double s = 0;
			int nu = 0;
			Rep(j, n) {
				if (a[i][j] != '.') {
					s += owp[j];
					++nu;
				}
			}
			score += s / nu / 4.0;
			printf("%.6lf\n", score);
		}
	}
	return 0;
}

