#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <stdio.h>


double exp(int l) {
	static double exp_mem[1001];
	if (l == 1) return 0;
	double& r = exp_mem[l];
	if (exp_mem[l] != 0) return r;
	r = l - 1 + exp(l - 1);
	for (int i = 2; i < l; ++i)
		r += exp(i) + exp(l-i);
	return r /= (l - 1.0);
}

double solve() {
	int n;
	scanf("%d", &n);
	std::vector<int> a;
	for (int i = 0; i < n; ++i) {
		int x;
		scanf("%d", &x);
		a.push_back(x-1);
	}
	double r = 0;
	std::vector<int> used(a.size(), 0);
	for (int i = 0; i < n; ++i) if(!used[i]) {
		int l = 0;
		for (int j = i; !used[j]; j = a[j]) {
			used[j] = 1;
			++l;
		}
		if (l > 1)
			r += exp(l) + 1;
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