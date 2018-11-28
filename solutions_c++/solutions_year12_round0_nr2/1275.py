#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

const int maxn=1000+123;
int a[maxn];
int main()
{
    int cas, n, s, p;
    freopen("2B.in", "r", stdin);
    freopen("gcj22.out", "w", stdout);
    scanf("%d", &cas);
    for (int I=1; I<=cas; ++I)
    {
        scanf("%d%d%d", &n, &s, &p);
        int t1=max(p*3-2, p);
        int t2=max(p*3-4, p);
        int ans=0, cnt=0;
        for (int i=0; i<n; ++i)
        {
            scanf("%d", a+i);
            if(a[i]>=t1)ans++;
            else
            {
                if(a[i]>=t2)cnt++;
            }
        }
        ans+=min(cnt, s);
        printf("Case #%d: %d\n", I, ans);
    }
    return 0;
}
