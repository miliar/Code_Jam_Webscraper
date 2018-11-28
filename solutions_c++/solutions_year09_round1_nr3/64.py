#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

#define INF 1000000000
#define EPS 1E-8
#define PI 3.14159265358979

using namespace std;

typedef vector<double> vec;
typedef vector<vec> mat;

double comb[50][50];

int main() {
	int N;
	cin >> N;
	comb[0][0] = 1;
	for(int i = 1; i < 50; ++i) {
		comb[i][0] = comb[i][i] = comb[i - 1][0] / 2;
		for(int j = 1; j < i; ++j) {
			comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) / 2;
		}
	}
	for(int t = 0; t < N; ++t) {
		int c, n;
		cin >> c >> n;
		mat m(c + 1, vec(c + 1, 0.0));
		for(int i = 0; i <= c; ++i) {
			for(int j = 0; j <= i; ++j) {
				if(n - (i - j) >= 0) m[i][j] = comb[c - j][i - j] * comb[j][n - (i - j)] / comb[c][n];
			}
		}
		vec res(c + 1, 0.0);
		/*res[n] = 1;
		for(int i = n + 1; i <= c; ++i) {
			for(int j = 0; j < i; ++j) {
				if(res[j]) res[i] += m[i][j] * (1 / ((1 - m[j][j]) * (1 - m[j][j])) + res[j] / (1 - m[j][j]));
			}
		}*/
		res[0] = 1;
		double r = 0;
		for(int l = 0; l < 10000; ++l) {
			vec next(c + 1, 0.0);
			for(int i = 0; i <= c; ++i) {
				for(int j = 0; j <= c; ++j) next[i] += res[j] * m[i][j];
			}
			r += next[c] * (l + 1);
			next[c] = 0;
			res = next;
		}
		double sum = 0;
		for(int i = 0; i <= c; ++i) sum += res[i];
		cerr << sum << endl;
		printf("Case #%d: %.10f\n", t + 1, r);
	}
	return 0;
}
