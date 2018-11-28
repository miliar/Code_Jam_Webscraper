#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;
const int maxn=2000000+123;
int st[]={10, 100, 1000, 10000, 100000, 1000000, 10000000};

inline int bit(int x)
{
    int t=1;
    for (; x; t++, x/=10);
    return t;
}

inline int rcc(int x, int t)
{
    return x/10+x%10*t;
}

int A, B;
int cnt[100];
bool flag[maxn];

bool none(int x)
{
    for (int i=1; i<=cnt[0]; ++i)
    {
        if(cnt[i]==x)return false;
    }
    return true;
}

int main ()
{
    int cas;
    freopen ("3.in", "r", stdin);
    freopen ("333.out", "w", stdout);
    scanf("%d", &cas);
    for (int I=1; I<=cas; ++I)
    {
        scanf ("%d%d", &A, &B);
        int t=bit(A), tt;
        memset (flag, false, sizeof(flag));
        int ans=0;
        for (int i=A; i<=B; ++i)
        {
            if(flag[i])continue;
            tt=i;
            int cnt=0;
            for (int j=0; j<t; ++j)
            {
                tt=rcc(tt, st[t-3]);

                if(tt>2000000)continue;
                if(flag[tt] || tt<A || tt>B)continue;
                cnt++;
                flag[tt]=true;
            }
            ans+=(cnt*(cnt-1))/2;
        }
        printf("Case #%d: %d\n", I, ans);
    }
    return 0;
}
/*
50
1052769 1957139

*/
