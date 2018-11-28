#include<stdio.h>
#include<string.h>
#include<vector>
using namespace std;
int dp[410][410][410];
int adj[410][410];
int que[410*410*410][3];
int cnt[410][410][410];
int qs,qe;
int main(){
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
	int n,m,i,j,k,l;
	scanf("%d%d",&n,&m);
	memset(adj,0,sizeof(adj));
	while(m--){
	    int a,b;
	    scanf("%d,%d",&a,&b);
	    adj[a][b]=adj[b][a]=1;
	}
	printf("Case #%d: ",cas++);
	if(adj[0][1]){
	    int d=0;
	    for(i=1;i<n;i++)if(adj[0][i])d++;
	    printf("0 %d\n",d);
	}else{
	    for(i=0;i<=n;i++)for(j=0;j<n;j++)for(k=0;k<n;k++)dp[i][j][k]=-1;
	    qs=qe=0;
	    for(i=1;i<n;i++)if(adj[0][i]){
		dp[1][0][i]=0;
		for(j=1;j<n;j++)if(j!=i&&(adj[0][j]||adj[i][j]))dp[1][0][i]++;
		que[qe][0]=1;
		que[qe][1]=0;
		que[qe][2]=i;
		qe++;
	    }
	    for(i=0;i<n;i++){
		for(j=0;j<n;j++){
		    if(j==i)continue;
		    if(!adj[i][j])continue;
		    for(k=0;k<n;k++){
			if(k==j||k==i)continue;
			if(!adj[j][k])continue;
			cnt[i][j][k]=0;
			for(l=0;l<n;l++){
			    if(l==i||l==j||l==k)continue;
			    if(!adj[i][l]&&!adj[j][l]&&adj[k][l])cnt[i][j][k]++;
			}
		    }
		}
	    }
	    int nd,x1,x2;
	    while(qs<qe){
		nd=que[qs][0];
		x1=que[qs][1];
		x2=que[qs][2];
		//printf("nd=%d %d %d %d\n",nd,x1,x2,dp[nd][x1][x2]);
		qs++;
		if(adj[x2][1])break;
		for(j=0;j<n;j++){
		    if(j==x1||j==x2)continue;
		    if(!adj[x2][j])continue;
		    if(dp[nd+1][x2][j]==-1){
			que[qe][0]=nd+1;
			que[qe][1]=x2;
			que[qe][2]=j;
			qe++;
		    }
		    dp[nd+1][x2][j]=max(dp[nd+1][x2][j],dp[nd][x1][x2]+cnt[x1][x2][j]-1);
		}
	    }
	    int d=0;
	    for(i=0;i<n;i++)for(j=0;j<n;j++)if(adj[j][1])d=max(d,dp[nd][i][j]);
	    printf("%d %d\n",nd,d);
	}
    }
}
