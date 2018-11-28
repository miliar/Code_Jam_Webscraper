#include<iostream>
using namespace std;

int t,n,k;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        scanf("%d%d",&n,&k);
        bool f=1;
        for(int i=0;i<n;i++)
        {
            if(!((1<<i)&k))
            {
                f=0;
                break;
            }
        }
        printf("Case #%d: ",c);
        if(!f) printf("OFF\n");
        else printf("ON\n");
    }
    
    return 0;
} 
