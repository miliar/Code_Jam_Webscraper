#include <fstream>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
const int Max=110;
int getMax(int x,int y)
{
    return x>y?x:y;
}
int fab(int x)
{
    return x<0?-x:x;
}
int dp1[Max],dp2[Max];
int main()
{
//    freopen("in.txt","r",stdin);
//   freopen("out.txt","w",stdout);
    dp1[0]=dp2[0]=0;
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;++cas)
    {
        int num;
        scanf("%d",&num);
        char str[3];
        int but1[Max],but2[Max];
        int top1=0,top2=0;
        but1[0]=but2[0]=1;
        int ans=0;
        for(int i=1;i<=num;++i)
        {
            scanf("%s",str);
            if(str[0]=='O')
            {
                top1++;
                scanf("%d",&but1[top1]);
                dp1[top1]=getMax(fab(but1[top1]-but1[top1-1])+dp1[top1-1],dp2[top2])+1;
                if(ans<dp1[top1])ans=dp1[top1];
            }
            else
            {
                top2++;
                scanf("%d",&but2[top2]);
                dp2[top2]=getMax(fab(but2[top2]-but2[top2-1])+dp2[top2-1],dp1[top1])+1;
                if(ans<dp2[top2])ans=dp2[top2];
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
