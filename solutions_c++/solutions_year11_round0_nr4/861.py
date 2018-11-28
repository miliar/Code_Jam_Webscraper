#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MAXN 1200
int CAS,n;
int per[MAXN];
int a,b,c;
double ans;
int main()
{
    int temp;
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&CAS);
    for(int cas = 1;cas <= CAS;cas++)
    {
        scanf("%d",&n);
        for(int i = 1;i <= n;i++)
            scanf("%d",&per[i]);
        ans = 0;
        for(int i = 1;i <=n;i++)
            if(per[i] != i)
                ans = ans+1;
        printf("Case #%d: %.6lf\n",cas,ans);
    }
    fclose(stdout);
    fclose(stdin);
}
