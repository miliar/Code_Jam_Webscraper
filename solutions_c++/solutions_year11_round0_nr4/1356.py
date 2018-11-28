#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int s[1005],m,n,i,j,ans;    
int main()
{
    //freopen("D-large.in","r",stdin);
   // freopen("D-large.out","w",stdout);
    scanf("%d",&m);
    for (i=1;i<=m;i++)
    {
        scanf("%d",&n); 
		ans=n;
        for(j=1;j<=n;j++)
        {
            scanf("%d",&s[j]);
            if(s[j]==j) ans--;
        }               
        printf("Case #%d: %.6lf\n",i,(double)ans);
    }
    
    return 0;
}
