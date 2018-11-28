#include <stdio.h>
#include <iostream>
#include <cstring>
#include <string>
#include <map>

using namespace std;

int T;
int n,p,s,t[105];
int a,b,c,d,e;

int solve()
{
    if(s>=c)
        return a+c+d;
    else
        return a+d+s;
}

int main()
{
    freopen("B-large.in","r",stdin);
    //reopen("t.txt","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&T);

    for(int j=1;j<=T;++j)
    {
        printf("Case #%d: ",j);
        scanf("%d%d%d",&n,&s,&p);
        a=b=c=d=e=0;
        for(int i=1;i<=n;++i)
        {
            scanf("%d",t+i);
            if(t[i]==29 || t[i]==30)
            {
                d++;
                continue;
            }
            if(t[i]==0)
            {
                if(p==0)
                    d++;
                else
                    e++;
                continue;
            }
            if(t[i]==1)
            {
                if(p<=1)
                    d++;
                else
                    e++;
                continue;
            }

            if(t[i]<3*p-4)
                b++;
            else
            {
                if(t[i]==3*p-4 || t[i]==3*p-3)
                    c++;
                else
                    a++;
            }
        }
        //printf("a:%d b:%d c:%d d:%d\n",a,b,c,d);
        printf("%d\n",solve());
    }
    return 1;
}
