#include<stdio.h>
#include<string.h>
#include<fstream>
long long int t,n,i,j,s,fact,cnt,st,pos,m,f;
long long int a[100][10];
using namespace std;
int main()
{
freopen("C:\\Users\\Sameer\\Desktop\\B-small-attempt1.in","r",stdin);
freopen("C:\\Users\\Sameer\\Desktop\\output.out","w",stdout);
scanf("%lld",&t);
for(j=1;j<=t;j++)
{
    scanf("%lld",&n);
    for(i=1;i<=n;i++)
        scanf("%lld %lld",&a[i][1],&a[i][2]);
    for(i=1;i<=n;i++)
        a[i][0]=0;
    s=2*n;fact=1;cnt=0;st=0;
    while(st<s && fact)
    {
        fact=0;
        for(i=1;i<=n;i++)
        {
            if(a[i][2]<=st && a[i][0]==0)
            {
                cnt++;
                st+=2;
                a[i][0]=2;
                fact=1;
                break;
            }
        }

        if(fact==0)
        {
            for(i=1;i<=n;i++)
            {
                if(a[i][2]<=st && a[i][0]==1)
                {
                    cnt++;
                    st++;
                    a[i][0]=2;
                    fact=1;
                    break;
                }
            }
        }

        if(fact==0)
        {
            m=-1;f=0;
            for(i=1;i<=n;i++)
            {
                if(a[i][1]<=st && a[i][0]==0)
                {
                    if(a[i][2]>m)
                    {
                        m=a[i][2];
                        pos=i;
                        f=1;
                    }
                }
            }

            if(f)
            {
                cnt++;
                st++;
                a[pos][0]=1;
                fact=1;
            }
        }

    }
    if(fact)
        printf("Case #%lld: %lld\n",j,cnt);
    else
        printf("Case #%lld: Too Bad\n",j);
}
return 0;
}
