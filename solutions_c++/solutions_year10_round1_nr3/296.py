#include <cstdio>
#include <iostream>
using namespace std;

int recursion(int a,int b)
{
    if(a<b)
    {
        return recursion(b,a);
    }
    if(b==0)
    {
        return 1;
    }
    else if(a/b==1)
    {
        return recursion(b,a%b)^1;
    }
    else
    {
        return 1;
    }
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int a,b,c,t,a1,a2,b1,b2,cnt;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d %d %d %d",&a1,&a2,&b1,&b2);
        cnt=0;
        for(a=a1;a<=a2;a++)
        {
            for(b=b1;b<=b2;b++)
            {
                if(recursion(a,b)==1)
                {
                    cnt++;
                }
            }
        }
        printf("Case #%d: %d\n",c+1,cnt);
    }
    return 0;
}
