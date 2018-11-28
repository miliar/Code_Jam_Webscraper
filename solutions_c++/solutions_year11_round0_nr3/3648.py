#include <iostream>
#include <cstdio>
#define MAXN 1005
using namespace std;
int num[MAXN];

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int Min, sum, t, n, s;
    scanf("%d", &t);
    for(int cas=1; cas<=t; cas++)
    {
        scanf("%d", &n);
        sum=s=0;
        Min=10000000;
        for(int i=0; i<n; i++)
        {
            scanf("%d", &num[i]);
            s+=num[i];
            if(i!=0) sum=sum^num[i];
            else sum=num[i];
            if(Min>num[i]) Min=num[i];
        }
        printf("Case #%d: ", cas);
        if(sum==0)
            printf("%d\n", s-Min);
        else
            printf("NO\n");
    }
    return 0;
}
