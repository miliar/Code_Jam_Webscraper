//#pragma comment(linker, "/STACK:65536000")
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<iostream>
#define clr(x,y) memset(x,y,sizeof(x))
#define ll __int64
using namespace std;

int a[100000],n,s,p;
int i,j,k,ans;
int flag[100000][4];

void dfs(int d,int s,int cnt){
    if(s<0) return ;
    if(d==n+1){
        if(cnt>ans) ans=cnt;
        return ;
    }
    if(flag[d][0])
        dfs(d+1,s-1,cnt+1);
    if(flag[d][1])
        dfs(d+1,s,cnt+1);
    if(flag[d][2])
        dfs(d+1,s-1,cnt);
    dfs(d+1,s,cnt);
}
int main(){
    freopen("e:\\in.txt","r",stdin);
    freopen("e:\\out.txt","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--){
        clr(flag,0);
        cas++;
        scanf("%d%d%d",&n,&s,&p);
        for(i=1;i<=n;i++){
            scanf("%d",&a[i]);
            for(j=0;j<=10;j++){
                for(k=0;k<=10;k++){
                    int l=a[i]-j-k;
                    if(l<0||l>10) continue;
                    if(abs(l-j)>2||abs(l-k)>2||abs(k-j)>2) continue;
                    if((abs(l-j)==2||abs(l-k)==2||abs(k-j)==2)&&max(max(j,k),l)>=p)
                        flag[i][0]=true;
                    else{
                        if(max(max(j,k),l)>=p) flag[i][1]=true;
                        if(abs(l-j)==2||abs(l-k)==2||abs(k-j)==2) flag[i][2]=true;
                    }
                }
            }
        }
        ans=0;
        dfs(1,s,0);
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
