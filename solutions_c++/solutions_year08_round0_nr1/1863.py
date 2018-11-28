#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <string>
using namespace std;
char qu[1002][100];
int main()
{
    int tc, cn;
    int n, q;
    int i, j, k;
    int cnt;
    char buf[1000];
    char check[1000];
    scanf("%d", &tc);
    for (cn = 1; cn <= tc; cn++) {
        map<string, int> idx;
        scanf("%d", &n); 
        gets(buf);
        memset(check, 0, sizeof(check));
        for (i = 1; i <= n; i++) {
            gets(buf);
            idx[buf] = i;
        }
        scanf("%d", &q);
        gets(buf);
        for (i = 0; i < q; i++) {
            gets(qu[i]);
        }
        cnt = 0;
        for (i = 0; i < q; i++) {
            j = idx[qu[i]];
            check[j] = 1; 
            for (k = 1; k <= n; k++) {
                if (check[k] == 0)
                    break;
            }
            if (k == n+1) {
                cnt++;
                memset(check, 0, sizeof(check));
                check[j] = 1;
            }
        }
        printf("Case #%d: %d\n", cn, cnt);
    }
    return 0;
}
