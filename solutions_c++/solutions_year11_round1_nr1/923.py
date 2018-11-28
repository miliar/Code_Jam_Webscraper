#include <cstdio>
#include <string>
#include<cmath>

using namespace std;

typedef long long ll;

int t,pd,pg,flag=0;
ll n,x;

int main ()
{
    scanf("%d",&t);
    int count=0;
    while(count<t)
    {
        count++;
        flag=0;
        scanf("%lld %d %d",&n,&pd,&pg);
        if (pg==0 || pg==100)
        {
            //printf("here\n");
            if(pd!=pg)
                flag=1;
        }
        else
        {
            flag=1;
            if(n>100)
            {
                flag=0;
            }
            else
            {
                    
                for(ll i=1;i<=n;i++)
                {
                    x=i*pd;
                    //printf("%lld\n",i);
                    if(x%100==0)
                    {
                        flag=0;
                        break;
                    }   
                }
            }
        
        }
        printf ("Case #%d: ", count);
        if(flag)
            printf("Broken\n");
        else
            printf("Possible\n");
        
    }
    //scanf("%d %lld",&t,&n);
    return 0;
}
