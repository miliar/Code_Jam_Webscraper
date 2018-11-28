#include <iostream>
#include <cstdio>
using namespace std;
typedef long long ll;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("hello.txt","w",stdout);
    int t,s,p,n,a;
    scanf("%d",&t);
    for(int q=1;q<=t;q++)
    {
        scanf("%d%d%d",&n,&s,&p);
        int cnt=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&a);
            bool f1=false,f2=false;
            for(int x=10;x>=0;x--)
                for(int y=x;y>=max(0,x-2);y--)
                    for(int z=x;z>=max(x-2,0);z--)
                        if (x+y+z==a)
                        {
                            if (!(y==x-2 || z==x-2) && x>=p)
                                f1=true;
                            else if ((y==x-2 || z==x-2) && x>=p)
                                f2=true;
                        }
            if (f1)
                cnt++;
            else if (f2 && s>0)
            {
                s--;
                cnt++;
            }
        }
        printf("Case #%d: %d\n",q,cnt);
    }
    return 0;
}
