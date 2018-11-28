#include <cstdio>
#include <iostream>
using namespace std;

int n,m,a,x2,y2,x3,y3;

bool search()
{
    for(x2=0;x2<=n;x2++)
    {
        for(y2=0;y2<=m;y2++)
        {
            for(x3=0;x3<=n;x3++)
            {
                for(y3=0;y3<=m;y3++)
                {
                    if(labs(((x2-x3)*y3-(y2-y3)*x3))==a)
                    {
                        return true;
                    }
                }
            }
        }
    }
    return false;
}

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int i,t;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d %d %d",&n,&m,&a);
        printf("Case #%d: ",i+1);
        if(search()==true)
        {
            printf("0 0 %d %d %d %d\n",x2,y2,x3,y3);
        }
        else
        {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
