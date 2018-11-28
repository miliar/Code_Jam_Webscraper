#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#define maxn 1500

using namespace std;
int CAS,n,k;
int sum;
int ci[maxn];
bool cmp(int a,int b)
{
    return a>b;
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&CAS);
    for(int cas = 1;cas <= CAS;cas++)
    {
        scanf("%d",&n);
        for(int i = 0;i < n;i++)
            scanf("%d",&ci[i]);
        sort(ci,ci+n,cmp);
        k = ci[0];
        for(int i = 1;i < n;i++)
            k = k ^ ci[i];
        sum = 0;
        for(int i = 0;i < n-1;i++)
            sum+=ci[i];
        if(k != 0)
            printf("Case #%d: NO\n",cas);
        else
            printf("Case #%d: %d\n",cas,sum);
    }
    fclose(stdin);
    fclose(stdout);
}
