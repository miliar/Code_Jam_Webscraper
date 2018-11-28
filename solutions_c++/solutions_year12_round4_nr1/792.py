#include<algorithm>
#include<iostream>
#include<stdio.h>
#include<string.h>
#include<string>

using namespace std;
int t;
int g;
int aa[10100],bb[10100];
int dp[10100];
int n,dac;
int fun;
int dfs(int i,int l);

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>t;
    for (int nit=1;nit<=t;nit++)
    {
        memset(dp,0,sizeof(dp));
        cin>>n;
        for (g=1;g<=n;g++)
           cin>>aa[g]>>bb[g];
        cin>>fun;
        dac=0;
        dfs(1,aa[1]);
        printf("Case #%d: ",nit);
        if (dac==0)
            cout<<"NO"<<endl; else cout<<"YES"<<endl;
    }
}

int dfs(int i,int l)
{
    int a,b;
    if (dp[i]!=0 && dp[i]>l) return 0;
    dp[i]=l;
    if (dac==1) return 0;
    if (aa[i]+l>=fun) {dac=1; return 0;}
    for (a=i+1;a<=n && aa[a]-aa[i]<=l;a++)
    {
        dfs(a,min(bb[a],aa[a]-aa[i]));
    }
}
