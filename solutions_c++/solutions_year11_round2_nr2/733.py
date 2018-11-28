#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <algorithm>
#include <limits>

#define px first
#define py second
#define mp make_pair

using namespace std;

const int INF = numeric_limits<int>::max();
const int ITER_MAX = 10000;

int caseNum;
int n, d;
vector<int> p;

bool check(double t)
{
	vector<double> pos(p.size());
	pos[0] = p[0] - t;
	for (size_t i = 1; i < p.size(); ++i) {
		double diff = 1.0 * p[i] - pos[i - 1];
		if (diff < 0) {
			if (p[i] + t < pos[i - 1] + d) {
				return false;
			} else {
				pos[i] = pos[i - 1] + d;
				continue;
			}
		}
		if (p[i] < pos[i - 1] + d) {//Move right
			if (p[i] + t < pos[i - 1] + d) {
				return false;
			} else {
				pos[i] = pos[i - 1] + d;
			}
		} else {//Move left
			if (p[i] - t < pos[i - 1] + d) {
				pos[i] = pos[i - 1] + d;
			} else {
				pos[i] = p[i] - t;
			}
		}
	}
	return true;
}

void solve()
{
	scanf("%d%d", &n, &d);
	p.clear();
	for (int i = 0; i < n; ++i) {
		int pos, v;
		scanf("%d%d", &pos, &v);
		for (int j = 0; j < v; ++j) {
			p.push_back(pos);
		}
	}
	double l = 0, r = INF;
	for (int iter = 0; iter < ITER_MAX; ++iter) {
		double x = (l + r) / 2;
		if (check(x)) {
			r = x;
		} else {
			l = x;
		}
	}
	printf("%0.6lf\n", l);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n", &caseNum);
	for (int i = 0; i < caseNum; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}