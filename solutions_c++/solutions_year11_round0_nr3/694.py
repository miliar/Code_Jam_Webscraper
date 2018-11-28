#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <iostream>
#include <vector>
using namespace std;

int num[1000010];

int T;

#define min(a, b) (a) < (b) ? (a) : (b)

int n;
int cas;

int main() {

	cas = 1;

    scanf("%d", &T);
	int i;
    while (T--) {

        int ans = 0;
		
		int mymin = 99999999;
		int sum = 0;

        scanf("%d", &n);
        for (i = 0; i < n; ++i) {
            scanf("%d", &num[i]);
            ans ^= num[i];
			mymin = min(mymin, num[i]);
            sum += num[i];
        }

        if (ans != 0) {
            printf("Case #%d: NO\n", cas++);
        } else {
            printf("Case #%d: %d\n", cas++, sum - mymin);
        }
    }
    return 0;
}