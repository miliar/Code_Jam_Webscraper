#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long LL;

int T;
LL N, D;
LL d[10005], l[10005];
LL dp[10005], len[10005];
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        cin >> N;
        for(int i = 0; i < N; i++) cin >> d[i] >> l[i];
        cin >> D;
        memset(dp, 0, sizeof(dp));
        dp[0] = 1; len[0] = d[0];
        for(int i = 1; i < N; i++)
        {
            LL cur = 0;
            for(int j = 0; j < i; j++) if (dp[j])
                if (len[j] >= d[i] - d[j])
                {
                    dp[i] = 1;
                    if (d[i] - d[j] >= l[i]) cur = l[i];
                    else
                    {
                        if (d[i] - d[j] > cur) cur = d[i] - d[j];
                    }
                }
            len[i] = cur;
        }
        //for(int i = 0; i < N; i++) cout << len[i] << endl;
        printf("Case #%d: ", t);
        bool flag = 0;
        for(int i = 0; i < N; i++) if (dp[i] && (d[i] + len[i] >= D)) flag = 1;
        if (flag) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    //system("pause");
    return 0;
}
