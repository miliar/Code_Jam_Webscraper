#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

vector<long long> p;

int main() {
    static int flag[1000001];
    for (int i = 2; i * i <= 1000000; ++i) {
        if (flag[i] == 0) {
            for (int j = i * i; j <= 1000000; j += i) {
                flag[j] = 1;
            }
        }
    }
    for (int i = 2; i <= 1000000; ++i){
        if (flag[i] == 0) {
            p.push_back(i);
        }
    }

    int tot_t;
    scanf("%d", &tot_t);
    for (int cur_t = 0; cur_t < tot_t; ++cur_t) {
        long long ans = 0, n;
        scanf("%lld", &n);
        for (size_t i = 0; i < p.size() && p[i] * p[i] <= n; ++i) {
            long long t = p[i] * p[i];
            int k = 2;
            while (t * p[i] <= n) {
                ++k;
                t *= p[i];
            }
            ans += k - 1;
        }
        ++ans;
        if (n == 1) {
            ans = 0;
        }
        printf("Case #%d: %lld\n", cur_t + 1, ans);
    }
    return 0;
}

