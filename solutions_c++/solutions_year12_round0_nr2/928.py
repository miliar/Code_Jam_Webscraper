#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
int t,s,p,n;
int num[110];
bool cmp(int a,int b)
{
    return a>b;
}
int main()
{
    freopen("D:\\B-large.in","r",stdin);
    freopen("D:\\out.txt","w",stdout);
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        scanf("%d%d%d",&n,&s,&p);
        for(int i=0;i<n;i++)
            scanf("%d",&num[i]);
        sort(num,num+n,cmp);
        int ans=0;
        for(int i=0;i<n;i++)
        {
            if(num[i]==1)
            {
                if(p<=1)
                    ans++;
            }
            else if(num[i]==0)
            {
                if(p==0)
                    ans++;
            }
            else if(num[i]>=p*3-2)
                ans++;
            else if(num[i]>=p*3-4 && s)
            {
                ans++;
                s--;
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
}
