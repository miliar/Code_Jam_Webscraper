#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define debug 1
#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define Rep(it, a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); it++)
#define pb push_back
#define mp make_pair
#define sz(a) ((int)a.size())
#define all(a) a.begin(), a.end()
#define cp(a) cerr << "(" << #a << "," << a << ") "
#define cen cerr << endl

typedef long long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int inf = 0x7fffffff;

const int Size = 1000 * 1000 + 1;
char buffer[Size];

const double eps = 10e-9;

int solution(int nTest) {
	printf("Case #%d: ", nTest + 1);
	int n;
	scanf("%d", &n);
	vi ar;
	int sum = 0;
	For(i, 0, n) {
		int t;
		scanf("%d", &t);
		ar.pb(t);
		sum += t;
	}
	For(i, 0, sz(ar)) {
		double l = 0, r = 1. + eps;
		while(r - l > eps) {
			double m = (r + l) / 2.;
			double p = ar[i] + sum * m;
			double u = 1. - m;
			int flag = 0;
			For(j, 0, sz(ar)) {
				if(j == i) {
					continue;
				}
				if(ar[j] >= p) {
					continue;
				}
				else {
					double q = p - ar[j];
					double t = q / sum;
					u -= t;
				}
			}
			if(u <= 0) {
				r = m;
			}
			else {
				l = m;
			}
		}
		printf("%.8lf ", l * 100);
	}
	printf("\n");




	return 1;
}

int main() {
	if(debug) {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}


	int i = 0, n = 99999;
	scanf("%d", &n);
	while(i < n && solution(i)) {
		i++;
	}

	return 0;
}
