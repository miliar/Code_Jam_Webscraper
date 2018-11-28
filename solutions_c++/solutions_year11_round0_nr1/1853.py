#include<stdio.h>
#include<stdlib.h>
#include<math.h>
struct node
{
    int loc,pos;
};
struct node input[105];
int step,ans[2],loc[2],pre;
int max(int a,int b)
{
    return a>b?a:b;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int ti=1;ti<=t;ti++)
    {
        scanf("%d",&step);
        for(int i=1;i<=step;i++)
        {
            char str[2];
            scanf("%s",str);
            if(str[0]=='O') input[i].pos=1;
            else            input[i].pos=0;
            scanf("%d",&input[i].loc);
        }
        ans[0]=ans[1]=0;
        loc[0]=loc[1]=1;
        ans[input[1].pos]=abs(input[1].loc-loc[1])+1;
        loc[input[1].pos]=input[1].loc;
        pre=input[1].pos;
        for(int i=2;i<=step;i++)
        {
            if(input[i].pos==pre)
            {
                ans[input[i].pos]+=abs(input[i].loc-loc[input[i].pos])+1;
                loc[input[i].pos]=input[i].loc;
                pre=input[i].pos;
            }
            else
            {
                int temp=abs(input[i].loc-loc[input[i].pos])+1;
                ans[input[i].pos]+=temp;
                if(ans[input[i].pos]<=ans[1-input[i].pos])
                     ans[input[i].pos]=ans[1-input[i].pos]+1;

                loc[input[i].pos]=input[i].loc;
                pre=input[i].pos;
            }
        }
        printf("Case #%d: %d\n",ti,max(ans[0],ans[1]));

    }
}
