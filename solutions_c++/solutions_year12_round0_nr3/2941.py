#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<memory.h>
using namespace std;

char s[12],p[12];
int a,b;
bool f[2000001];

long long op(int i)
{
    memset(f,0,sizeof(f[0])*(b+5));
    memset(s,0,sizeof(s));
    sprintf(s,"%d",i);
    int n=strlen(s),t;
    long long ans=0;
    for(int k=1;k<n;k++)
    {
        memset(p,0,sizeof(p));
        for(int j=0;j<n;j++)
            p[j]=s[(j+k)%n];
        sscanf(p,"%d",&t);
        if(t>i&&t<=b&&!f[t])
        {
            f[t]=1;
            ans++;
        }
    }
    return ans;
}

int main()
{
    int t,cas=0,i;
    long long ans;
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        ans=0,cas++;
        scanf("%d%d",&a,&b);
        for(i=a;i<=b;i++)
        {
            ans+=op(i);
        }
        printf("Case #%d: %lld\n",cas,ans);
    }
    return 0;
}
