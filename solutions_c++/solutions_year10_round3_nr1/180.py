#include<stdio.h>
#include<iostream>
#include<queue>
#include<map>
#include<vector>
#include<string>
#include<sstream>
#include<math.h>
#include<algorithm>
#define _clr(x) memset(x,-1,sizeof(x))
#define clr(x) memset(x,0,sizeof(x))
#define pb push_back
#define M 1001
using namespace std;
struct ftft
{
    int a,b;
}ft[1010];
int cmp(const ftft &a,const ftft &b)
{
    return a.a<b.a;
}
int main()
{
    freopen("in.txt","r",stdin);
    //freopen("in.in","r",stdin);
    freopen("in.out","w",stdout);
    int T;
    scanf("%d",&T);
    int ca=0;
    while(T--)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d%d",&ft[i].a,&ft[i].b);
        }
        sort(ft,ft+n,cmp);
        int ans=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<i;j++)
            {
                if(ft[i].b<ft[j].b)
                {
                    ans++;
                }
            }
        }
        printf("Case #%d: %d\n",++ca,ans);
    }
}
