#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    int tc, cn;
    int i ,j ,k;
    int cnt, sum, min1;
    int n;
    int ori[100], num[100];
    int check[100];
    char buf[100];
    scanf("%d", &tc);
    for (cn = 1; cn <= tc; cn++) {
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%s", buf);
            for (j = n-1; j >= 0; j--) {
                if (buf[j] == '1')
                    break;
            }
            ori[i] = num[i] = j;
        }
        sort(num, num+n);
        min1 = 1000000;
        do {
            for (i = 0; i < n; i++) {
                if (num[i] <= i)
                    continue;
                break;
            }
            if (i < n) {
            }
            else {
                memset(check, 0, sizeof(check));
                sum = 0;
                for (i = 0; i < n; i++) {
                    cnt = 0;
                    for (j = 0; j < n; j++) {
                        if (!check[j] && ori[j] == num[i]) {
                            check[j] = 1;
                            sum += cnt;
                            break;
                        }
                        else if (!check[j]) {
                            cnt++;
                        }
                    }
                }
                min1 = min(min1, sum);
            }
        } while (next_permutation(num, num+n));
        printf("Case #%d: %d\n", cn, min1);
    }
    return 0;
}
