#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int test,cas,n,tm1,tm2,ans,pos1,pos2,i,a;
    char ch;
    scanf("%d",&test);
    for (cas=1;cas<=test;cas++)
    {
        scanf("%d",&n);
        tm1=tm2=ans=0;
        pos1=pos2=1;
        for (i=0;i<n;i++)
        {
            cin>>ch;
            scanf("%d",&a);
            if (ch=='O')
            {
                ans=max(ans+1,tm1+abs(a-pos1)+1);
                tm1=ans;
                pos1=a;
            }
            else
            {
                ans=max(ans+1,tm2+abs(a-pos2)+1);
                tm2=ans;
                pos2=a;
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
