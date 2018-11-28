#include<iostream>


using namespace std;

int i,j,k,l,m,n,t;
int ans;
int main()
{
    freopen("tmp.in","r",stdin);
    freopen("tmp.out","w",stdout);
    scanf("%d",&t);
    for (j=1;j<=t;++j)
    {
        scanf("%d%d",&n,&k);
        m=1;
        for (l=1;l<=n;l++)
        {
            m*=2;
        }
        ans=k%m;
        printf("Case #%d: ",j);
        if (ans==m-1) printf("ON\n");
            else printf("OFF\n");
          
        
    }
}
