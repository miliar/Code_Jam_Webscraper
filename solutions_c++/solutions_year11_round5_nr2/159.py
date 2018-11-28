#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

const int maxn = 1024;

int a[maxn];
int tail[maxn], len[maxn];
int cas, tot, n;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d",&cas);
    for (int run = 1; run<=cas; run++ )
    {
        scanf("%d",&n);
        for (int i = 0; i<n; i++ )
            scanf("%d",a+i);
        printf("Case #%d: ",run);
        if (n == 0)
        {
            printf("0\n");
            continue;
        }
        sort(a, a+n);
        tot = 0;
        for (int i = 0; i<n; i++ )
        {
            int chose = -1;
            for (int j = 0; j<tot; j++ )
                if (a[i] == tail[j]+1)
                    if (chose == -1 || len[j]<len[chose])
                        chose = j;
            if (chose == -1)
            {
                len[tot] = 0;
                chose = tot;
                ++tot;
            }
            tail[chose] = a[i];
            ++len[chose];
        }
        int ans = n;
        for (int i = 0; i<tot; i++ )
            ans = min(ans, len[i]);
        printf("%d\n",ans);
    }
    return 0;
}
