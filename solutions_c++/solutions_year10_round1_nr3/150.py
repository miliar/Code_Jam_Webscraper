#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <set>
#include <algorithm>
#include <vector>

using namespace std;

int t,iii,x,y,i,j;
int a1,a2,b1,b2,tmp1,tmp2;
int ans;

inline int maxx(int tmpx,int tmpy)
{
    if(tmpx>tmpy)
    return tmpx;
    else
    return tmpy;
}

int solve(int xxx,int yyy)
{
    if(yyy==0)
    return 1;
    if(xxx/yyy>=2)
    return 1;
    else
    return 1-solve(yyy,xxx-yyy);
}

int main()
{
    scanf("%d",&t);
    for(iii=1;iii<=t;iii++)
    {
        scanf("%d %d %d %d",&a1,&a2,&b1,&b2);
        ans=0;
        for(i=a1;i<=a2;i++)
        {
            for(j=b1;j<=b2;j++)
            {
                tmp1=maxx(i,j);
                tmp2=i+j-tmp1;
                ans+=solve(tmp1,tmp2);
            }
        }
        printf("Case #%d: %d\n",iii,ans);
    }
    return 0;
}
