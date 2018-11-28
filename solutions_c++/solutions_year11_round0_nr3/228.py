#include <iostream>
#include <numeric>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int a[1000];

int main() {
    int tott, n;
    scanf("%d", &tott);
    for (int curt = 1; curt <= tott; ++curt) {
        scanf("%d", &n);
        int sum = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%d", &a[i]);
            sum ^= a[i]; 
        }
        sort(a, a + n);
        printf("Case #%d: ", curt);
        if (sum == 0) {
            printf("%d\n", accumulate(a + 1, a + n, 0));
        } else {
            printf("NO\n");
        }
    }
    return 0;
}

