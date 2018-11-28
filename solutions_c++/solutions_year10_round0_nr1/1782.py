#include <stdio.h>
using namespace std;

int main()
{       int t,n,k;
      freopen("A.in","r",stdin);
      freopen("A.out","w",stdout);
        scanf("%d",&t);
        for (int i=1; i<=t; i++)
        {
                printf("Case #%d: ",i);
                scanf("%d%d",&n,&k);
                int ans=1;
                for (int j=1; j<=n; j++) ans=ans*2;
                if ((k+1)%ans==0) printf("ON\n"); else printf("OFF\n");
        }
}
