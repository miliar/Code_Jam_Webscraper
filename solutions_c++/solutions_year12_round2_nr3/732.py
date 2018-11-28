#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long ll;
const int maxn=1000;
int a[maxn];
int b[maxn];
bool flag;

void dfs(int dfn, int s)
{
    if(s==dfn)
    {
        int sum1=0, sum2=0;
        for (int i=0; i<s; ++i)
        {
            if(b[i]==1)sum1+=a[i];
            if(b[i]==2)sum2+=a[i];
        }
        if(sum1==sum2 && sum1>0)flag=true;
        return;
    }
    //puts("@");
    for (int i=0; i<3; ++i)
    {
        if(!flag)
        {
            b[dfn]=i;
            dfs(dfn+1, s);
        }
    }
}


int main ()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    int cas; scanf("%d", &cas);

    for (int I=1; I<=cas; ++I)
    {
        int n; scanf("%d", &n);
        for (int i=0; i<n; ++i)
        {
            scanf("%d", a+i);
        }
        flag=false;
        memset (b, 0 , sizeof(b));
        sort(a, a+n);

        dfs(0, n);
        printf("Case #%d:\n", I);
        if(flag)
        {
            for (int i=0; i<n; ++i)
                if(b[i]==1)printf("%d ", a[i]);
                printf("\b\n");
            for (int i=0; i<n; ++i)
                if(b[i]==2)printf("%d ", a[i]);
                printf("\b\n");
        }
        else    puts("Impossible");

    }
    return 0;
}
/*
3
20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
20 120 266 858 1243 1657 1771 2328 2490 2665 2894 3117 4210 4454 4943 5690 6170 7048 7125 9512 9600
20 1 2 4 8 16 32 64 128 256 512 1024 2048 4096 10000 20000 40000 80000 160000 320000 640000
*/
