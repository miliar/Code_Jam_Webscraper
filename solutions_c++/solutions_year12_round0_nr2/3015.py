#include<cstdio>
using namespace std;
int main()
{
    int t,i,j,n,s,p,o,k1,k2,k3,a,m;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d%d%d",&n,&s,&p);
        o=0;
        for(j=0;j<n;j++)
        {
            scanf("%d",&a);
            m=a/3;
            if(a%3!=0)m++;
            if(m>=p)o++;
            else if(s!=0 && m+1>=p && a>=p && a%3!=1)
            {
                s--;
                o++;
            }
        }
        printf("Case #%d: %d\n",i,o);
    }
}
