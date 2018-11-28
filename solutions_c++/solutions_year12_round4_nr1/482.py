#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int t;
int a,b,c,d,e,f;
int di[10050],li[10050];
int dp[10050];
int n,judge;
int mubiao;
int dfs(int i,int l)
{
    int a,b;
    if (dp[i]!=0 && dp[i]>l) return 0;
    dp[i]=l;
    if (judge==1) return 0;
    if (di[i]+l>=mubiao) {judge=1; return 0;}
    for (a=i+1;a<=n && di[a]-di[i]<=l;a++)
    {
        dfs(a,min(li[a],di[a]-di[i]));
    }
}    

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>t;
    for (int cas=1;cas<=t;cas++)
    {
        memset(dp,0,sizeof(dp));
        cin>>n;
        for (a=1;a<=n;a++) cin>>di[a]>>li[a];
        cin>>mubiao;
        judge=0;
        dfs(1,di[1]);
        printf("Case #%d: ",cas);
        if (judge==0) cout<<"NO"<<endl; else cout<<"YES"<<endl;
    }
}
