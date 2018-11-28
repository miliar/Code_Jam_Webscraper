#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
char str[2000], temp[2000];
int main()
{
    int tc, cn;
    int len, k;
    int i, j;
    int min1, cnt;
    int idx[10];
    scanf("%d", &tc);
    for (cn = 1; cn <= tc; cn++) {
        scanf("%d%s", &k, str);
        for (i = 0; i < k; i++) {
            idx[i] = i;
        }
        len = strlen(str);
        min1 = 99999999;
        do {
            for (i = 0; i < len / k; i++) {
                for (j = 0; j < k; j++) {
                    temp[i*k+j] = str[idx[j]+k*i];
                }
            }
            temp[len] = 0;
            cnt = 1;
            for (i = 1; i < len; i++) {
                if (temp[i] != temp[i-1])
                    cnt++; 
            }
            if (cnt < min1)
                min1 = cnt;
        } while (next_permutation(idx, idx+k));
        printf("Case #%d: %d\n", cn, min1);
    }
    return 0;
}
