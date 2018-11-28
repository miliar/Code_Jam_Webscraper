#include <set>
#include <map>
#include <list>
#include <cmath>
#include <queue>
#include <deque>
#include <vector>
#include <bitset>
#include <string>
#include <memory>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <cassert>
#include <iostream>
#include <algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define s(c) ((int)((c).size()))
#define all(c) (c).begin(),(c).end()
#define abs(x) ((x) < 0 ? -(x) : (x))
#define f(i, lo, hi) for (int i = (lo), Max = (hi); i <= Max; ++i)
#define rf(i, hi, lo) for (int i = (hi), Min = (lo); i >= Min; --i)
#define c(i, c) f(i, 0, s(c) - 1)
#define rc(i, c) rf(i, s(c) - 1, 0)
typedef vector<int> vint;
typedef long long lint;

int n;
char res[105][105];
int sum[105], win[105];
double wp[105], owp[105], oowp[105];

void solve(int T) {
	scanf("%d", &n);
	f(i, 1, n)
		scanf("%s", &res[i][1]);
	f(i, 1, n) {
		sum[i] = 0;
		win[i] = 0;
		f(j, 1, n) {
			if (res[i][j] == '1') {
				++sum[i]; ++win[i];
			} else if (res[i][j] == '0') {
				++sum[i];
			}
		}
		wp[i] = (double)win[i] / sum[i];
	}
	f(i, 1, n) {
		double all = 0;
		f(j, 1, n) {
			int s = sum[j];
			int w = win[j];
			if (res[i][j] == '1') {
				--s;
			} else if (res[i][j] == '0') {
				--s;
				--w;
			} else {
				continue;
			}
			all += (double)w / s;
		}
		owp[i] = all / sum[i];
	}
	f(i, 1, n) {
		double all = 0;
		f(j, 1, n) {
			if (res[i][j] == '1') {
				all += owp[j];
			} else if (res[i][j] == '0') {
				all += owp[j];
			}
		}
		oowp[i] = all / sum[i];
	}
	printf("Case #%d:\n", T);
	f(i, 1, n)
		printf("%.9lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	f(i, 1, t) solve(i);
	return 0;
}
