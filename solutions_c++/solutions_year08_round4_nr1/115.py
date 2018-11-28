#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

typedef long long int64;

int n, desired, n_int, n_ext;

int op[100000];
int ch[100000];

int cost[100000][2];
const int IMP = 999999;

void solve()
{
    scanf("%d%d", &n, &desired);
    n_int = (n-1)/2;
    n_ext = (n+1)/2;

    for (int i = 1; i <= n_int; i++)
        scanf("%d%d", &op[i], &ch[i]);

    for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++)
        cost[i][j] = IMP;

    for (int i = n_int + 1; i <= n; i++) {
        int val;
        scanf("%d", &val);
        cost[i][val] = 0;
    }

    for (int i = n_int; i >= 1; i--) {
        int or_false = cost[2*i][0] + cost[2*i+1][0];
        int or_true = std::min(cost[2*i][1], cost[2*i+1][1]);

        int and_false = std::min(cost[2*i][0], cost[2*i+1][0]);
        int and_true = cost[2*i][1] + cost[2*i+1][1];
        
        if (!ch[i]) {
            if (op[i]) {
                cost[i][0] = and_false;
                cost[i][1] = and_true;
            } else {
                cost[i][0] = or_false;
                cost[i][1] = or_true;
            }
        } else {
            if (op[i]) {
                cost[i][0] = std::min(or_false + 1, and_false);
                cost[i][1] = std::min(or_true + 1, and_true);
            } else {
                cost[i][0] = std::min(or_false, and_false + 1);
                cost[i][1] = std::min(or_true, and_true + 1);
            }
        }
    }

    /*
    printf("\n");
    for (int i = 1; i <= n; i++)
        printf("%d 0=%d 1=%d\n", i, cost[i][0], cost[i][1]);
    */
    
    int res = cost[1][desired];

    if (res >= IMP)
        printf("IMPOSSIBLE");
    else
        printf("%d", res);
}

int main()
{
    int n_cases;
    scanf("%d", &n_cases);

    for (int i = 0; i < n_cases; i++) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
}

