#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#define maxn 2000001

using namespace std;

struct node
{
    int x,y;
}s[10000000];

int p,dp[maxn],mat[1100];

int main(){
    int i,j,t,tt,n,sumUp,ss,tmp;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    cin>>t;
    for(tt=1;tt<=t;tt++){
        cin>>n;
        sumUp=0;
        ss=0;
        for(i=0;i<n;i++){
            scanf("%d",&mat[i]);
            sumUp=sumUp^mat[i];
            ss+=mat[i];
        }
        for(i=0;i<maxn;i++){
            dp[i]=-1;
        }
        dp[0]=0;
        for(i=0;i<n;i++){
            p=0;
            for(j=maxn-1;j>=0;j--){
                tmp=j^mat[i];
                if(dp[j]!=-1&&tmp>=0&&tmp<maxn&&dp[tmp]<dp[j]+mat[i]){
                    s[p].x=tmp;
                    s[p++].y=dp[j]+mat[i];
                }
            }
            for(j=0;j<p;j++){
                dp[s[j].x]=s[j].y;
            }
        }
        int ans=0;
        for(i=maxn-1;i>0;i--){
            if(dp[i]>0&&dp[i]!=ss&&i==int(sumUp^i)){
                if(ans<dp[i])
                ans=dp[i];
            }
        }
        if(ans){
            printf("Case #%d: %d\n",tt,ans);
        }
        else{
            printf("Case #%d: NO\n",tt);
        }
    }
    return 0;
}
