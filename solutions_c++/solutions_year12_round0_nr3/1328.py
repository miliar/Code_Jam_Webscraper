#include"stdio.h"
int t,i,j,k,a,b,dg,tmp,dec[7]={1,10,100,1000,10000,100000,1000000};
int sum,count;
bool u[1000050];
int main()
{
    //freopen("2.in","r",stdin);
    //freopen("2.txt","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d%d",&a,&b);
        for(sum=j=0;j<=b-a;j++) u[j]=0;
        for(j=a,dg=-1;j;j/=10,dg++);
        for(j=a;j<=b;j++)
        {
            if(u[j-a]) continue;
            count=u[j-a]=1;
            for(tmp=j,k=0;k<dg;k++)
            {
                tmp= tmp/10 + tmp%10*dec[dg];
                if(tmp>a&&tmp<=b)
                    if(u[tmp-a]==0)
                    {
                        u[tmp-a]=1;
                        count++;
                    }
            }
            sum+=count*(count-1)/2;
        }
        printf("Case #%d: %d\n",i,sum);
    }
    //scanf(" ");
}
