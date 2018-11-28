#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <stdio.h>

std::string solve() {
	int n;
	scanf("%d", &n);
	std::vector<int> x;
	for (int i = 0; i < n; ++i) {
		int a;
		scanf("%d", &a);
		x.push_back(a);
	}
	int xor = std::accumulate(x.begin(), x.end(), 0, [](int a, int b) { return a^b; });
	if (xor) return "NO";
	std::stringstream oss;
	oss << std::accumulate(x.begin(), x.end(), 0) - *std::min_element(x.begin(), x.end());
	return oss.str();
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
        printf("Case #%d: %s\n", i+1, solve().c_str());
    }
        
}