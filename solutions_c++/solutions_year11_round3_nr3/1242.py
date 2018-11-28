#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("c.out","w",stdout);
    int i,j,k,l,t,kase=1,f,r,c,p[10009],cnt,n,h;
    scanf("%d",&t);
    while (t--)
    {
        f=0;
        scanf("%d %d %d",&n,&l,&h);
        for(i=0;i<n;i++)
        scanf("%d",&p[i]);

        for(i=l;i<=h;i++)
        {
           cnt=0;
           for(j=0;j<n;j++)
           {
               if(i%p[j]==0 || p[j]%i==0)
               cnt++;
           }
           if(cnt==n)
           {
            f=1;
           printf("Case #%d: %d\n",kase++,i);
           break;
           }
        }
        if(f==0)
        printf("Case #%d: NO\n",kase++);
    }
    return 0;
}

