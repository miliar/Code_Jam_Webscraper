#pragma comment(linker, "/STACK:40000000") 

#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>

using namespace std;


int main()
{
    freopen("i.txt", "r", stdin);
    freopen("o.txt", "w", stdout);

    int N;
    scanf("%d", &N);
    for (int I = 1; I <= N; ++I) {
        int n;
        long long xor = 0, sum = 0, less = 1000000000000000000ll;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            long long x;
            scanf("%I64d", &x);
            sum += x;
            less = min(less, x);
            xor ^= x;
        }
        
        if (xor) {
            printf("Case #%d: NO\n", I);
        } else {
            printf("Case #%d: %I64d\n", I, sum - less);
        }
    }

    return 0;
}
