#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <vector>

using namespace std;


int T;

#define maxn 1000000
#define inf 100000000

int cas = 1;

int n;

int main() {
    cas = 1;
	int i;
	double ans;
	int val;
    scanf("%d", &T);
    while (T--) {

        ans = 0;

        scanf("%d", &n);

        for (i = 1; i <= n; i++) {
            scanf("%d", &val);

			if (val != i) ans ++;
        }

        printf("Case #%d: %.6lf\n", cas++, ans);

    }

    return 0;
}