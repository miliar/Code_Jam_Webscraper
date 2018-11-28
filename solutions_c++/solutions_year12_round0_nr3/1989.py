#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

typedef long long int64;

int log10(int x) {
    int len = 0;
    while(x > 0) {
        x /= 10;
        len++;
    }
    return len;
}

int main() {
	int t = 1, tc;
	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d: ", t);
        int a, b;
        scanf("%d%d", &a, &b);

        int len = log10(a);
        assert(len == log10(b) && len >= 1);
        int pw = 1;
        for(int j = 1; j < len; j++) pw *= 10;

        int ans = 0;

        for(int i = a; i < b; i++) {
            int x = i;
            std::set<int> res;
            for(int j = 1; j < len; j++) {
                x = (x / 10) + (x % 10) * pw;
                if(x > i && x <= b)
                    res.insert(x);
            }
            ans += res.size();
        }

        printf("%d\n", ans);
	}
	return 0;
}
