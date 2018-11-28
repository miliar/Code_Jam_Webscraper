#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("outB.txt","w",stdout);
    int num,n,nn,s,p,k=1,m,sum,mm[110];
    scanf("%d",&num);
    while(num--)
    {
        sum=0;
        scanf("%d%d%d",&n,&s,&p);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&mm[i]);
            m=mm[i]/3;
            if(m>=p)
            {
                sum++;
            }
            else
            {
                nn=mm[i]%3;
                if(nn==0)
                {
                    if(m+1>=p&&s&&m-1>=0)
                    {
                        sum++;
                        s--;
                    }
                }
                if(nn==1)
                {
                    if(m+1>=p)
                    {
                        sum++;
                    }
                }
                if(nn==2)
                {
                    if(m+1>=p)
                    {
                        sum++;
                    }
                    else
                    {
                        if(m+2>=p&&s)
                        {
                            sum++;
                            s--;
                        }
                    }
                }
            }
        }
        printf("Case #%d: %d\n",k++,sum);
    }
}
