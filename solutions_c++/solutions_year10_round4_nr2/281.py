#include<stdio.h>
int a[2010],b[2010],dp[10010][22];
int n,MAX=1000000000;
void DFS(int s){
if(s>=n){
dp[s][a[s-n]]=0;
return;}
DFS(s*2);
DFS(s*2+1);
int i=0,j=0,m;
for(i=0;i<=15;i++){
for(j=0;j<=15;j++){
m=i;
if(m<j)m=j;
if(dp[s][m]>dp[s*2][i]+dp[s*2+1][j])dp[s][m]=dp[s*2][i]+dp[s*2+1][j];
}}
for(i=1;i<=15;i++)
if(dp[s][i-1]>dp[s][i]+b[s])dp[s][i-1]=dp[s][i]+b[s];
}
int main(){
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
int T,t,i,j,p,w,e;
scanf("%d",&T);
for(t=1;t<=T;t++){
scanf("%d",&n);
p=n;n=(1<<n);
for(i=0;i<=n*2;i++)for(j=0;j<20;j++)dp[i][j]=MAX;
for(i=0;i<n;i++){scanf("%d",&a[i]);a[i]=p-a[i];}
w=n/2;e=n;
while(w!=0){
for(i=w;i<e;i++){
	scanf("%d",&b[i]);}
e=w;w/=2;
}
DFS(1);
printf("Case #%d: %d\n",t,dp[1][0]);
}
}
