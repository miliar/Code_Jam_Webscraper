#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

int table[2000005];

int min_inversion(int n, int digits, int power, int A, int B) {
    int ans = n;
    for (int i=0; i < digits; ++i) {
        n = n / 10 + (n % 10) * power;
        if (n >= A && n <= B) {
            ans = min(ans, n);
        }
    }
    return ans;
}

void solve(int id) {
    printf("Case #%d: ", id);
    
    memset(table, 0, sizeof(table));
    
    int A, B;
    scanf("%d %d", &A, &B);
    
    int power = 1, digits = 1;
    while (power*10 <= A) {
        power *= 10;
        ++digits;
    }
    
    for (int i=A; i <= B; ++i) {
        ++table[min_inversion(i, digits, power, A, B)];
    }
    
    long long ans = 0;
    
    for (int i=A; i <= B; ++i) {
        ans += table[i] * (table[i] - 1) / 2;
    }
    
    printf("%lld\n", ans);
}

int main() {
    int t, T = 1;
    
    scanf("%d ", &t);
    while (t--) {
        solve(T++);
    }
    
    return 0;
}
