#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
using namespace std;
int t, n, x[1000], num[2][1000], cnt[2], jeo;
void dfs(int deep)
{
    if (deep == n)
    {
        if (cnt[0] != 0 && cnt[1] != 0)
        {
            int ans[2], sum[2];
            ans[0] = ans[1] = sum[0] = sum[1] = 0;
            for(int i = 0; i < 2; i++)
                for(int j = 0; j < cnt[i]; j++)
                {
                    //cout << i << ' ' << num[i][j] << ' ';
                    ans[i] ^= num[i][j];
                    sum[i] += num[i][j];
                }
            //cout << endl;
            //cout << cnt[0] << ' ' << ans[0] << ' ' << cnt[1] << ' ' << ans[1] << endl;
            if (ans[0] == ans[1])
            {
                if (sum[0] > jeo) jeo = sum[0];
                if (sum[1] > jeo) jeo = sum[1];
            }
        }
        return;
    }
    num[0][cnt[0]++] = x[deep];
    dfs(deep + 1);
    cnt[0]--;
    num[1][cnt[1]++] = x[deep];
    dfs(deep + 1);
    cnt[1]--;
}
int main()
{
    freopen("C.txt", "w", stdout);
    scanf("%d", &t);
    for(int tt = 1; tt <= t; tt++)
    {
        scanf("%d", &n);
        for(int i = 0; i < n; i++) scanf("%d", &x[i]);
        jeo = -1;
        dfs(0); printf("Case #%d: ", tt);
        if (jeo == -1) printf("NO\n");
        else printf("%d\n", jeo);
    }
    return 0;
}
