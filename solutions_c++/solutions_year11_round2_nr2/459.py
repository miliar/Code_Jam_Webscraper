#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>

bool can(const std::vector<int>& p, const std::vector<int>& v, double t, int d) {
	double left = -1e9;
	for (int i = 0; i < p.size(); ++i) 
		for (int j = 0; j < v[i]; ++j) {
			if (left > p[i] + t) return false;
			left = std::max(p[i] - t, left) + d;
		}
	return true;
}

double solve() {
	int c, d;
	scanf("%d%d", &c, &d);
	std::vector<int> p, v;
	for (int i = 0; i < c; ++i) {
		int a, b;
		scanf("%d%d", &a, &b);
		p.push_back(a);
		v.push_back(b);
	}
	if (can(p, v, 0, d)) return 0;
	double l = 0, r = 1e9;
	while (r - l > 1e-9) {
		double t = (l + r) / 2;
		if (can(p, v, t,d ))
			r = t;
		else
			l = t;
	}
	return r;
}

char s[1024];
int main(int argc, char* argv[]) {
    freopen(argv[1], "r", stdin);
    strcat(s, argv[1]);
    strcat(s, ".out");
    freopen(s, "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        printf("Case #%d: %.9lf\n", i+1, solve());
    }
        
}