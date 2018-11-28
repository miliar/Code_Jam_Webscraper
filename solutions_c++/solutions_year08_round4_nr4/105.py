// D2.cc

#include <stdio.h>
#include <string.h>
#define inf 0x3f3f3f3f

int S[16][16];
int E[16][16];
int L,K,G;
char s[51000];
int dp[16][16][1<<16]; // dp[beg][cur][stat]

int max(int i,int j){return i>j?i:j;}

void solve(int cas){
	int i,j,k,nj,nk,B;
	int res,tmp;
	scanf("%d%s",&K,s);
	L=strlen(s);
	G=L/K;
	memset(S,0,sizeof(S));
	memset(E,0,sizeof(E));
	for (i=0;i<K;i++) S[i][i]=E[i][i]=-100000000;
	for (B=0;B<L;B+=K){
		for (i=0;i<K;i++) for (j=0;j<K;j++)
			if (s[B+i]==s[B+j]) S[i][j]++;
	}
	for (B=0;B+K<L;B+=K){
		for (i=0;i<K;i++) for (j=0;j<K;j++)
			if (s[B+i]==s[B+j+K]) E[i][j]++;
	}
	memset(dp,0xff,sizeof(dp));
	for (i=0;i<K;i++) dp[i][i][1<<i]=0;
	for (k=0;k<(1<<K);k++){
		// i:start j:cur
		for (i=0;i<K;i++) for (j=0;j<K;j++){
			if (dp[i][j][k]==-1) continue;
			if ((k&(1<<j))==0) continue;
			for (nj=0;nj<K;nj++){
				if (k&(1<<nj)) continue;
				nk=k|(1<<nj);
				dp[i][nj][nk]=max(dp[i][nj][nk],dp[i][j][k]+S[j][nj]);
			}
		}
	}
	res=0;
	k=(1<<K)-1;
	for (i=0;i<K;i++) for (j=0;j<K;j++){
		tmp=dp[i][j][k]+E[j][i];
		if (tmp>res) res=tmp;
//		printf("tmp[%d][%d]=%d\n",i,j,tmp);
	}
	printf("Case #%d: %d\n",cas,L-res);
	fprintf(stderr,"Case #%d: %d\n",cas,L-res);
}

int main(){
	int t,cas;
	freopen("D-large.in.txt","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&t);
	for (cas=1;cas<=t;cas++)
		solve(cas);
	return 0;
}
