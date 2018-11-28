#include <cstdio>

const int N=501;
const int MOD=100003;

int C[N][N];
int F[N][N];

int main(){
	int i,j,k;
	for(i=0;i<N;i++) C[i][0]=C[i][i]=1;
	for(i=2;i<N;i++){
		for(j=1;j<i;j++) C[i][j]=(C[i-1][j]+C[i-1][j-1])%MOD;
	}
	
	for(i=2;i<N;i++) F[i][1]=F[i][2]=1;
	F[2][2]=0;
	for(i=4;i<N;i++){
		for(j=3;j<i;j++){
			for(k=1;k<j;k++){
				F[i][j]=(F[i][j]+1LL*F[j][k]*C[i-j-1][j-k-1])%MOD;
			}
		}
	}
	
	int ic,cas;
	scanf("%d",&cas);
	for(ic=1;ic<=cas;ic++){
		int n;
		scanf("%d",&n);
		int ans=0;
		for(i=1;i<n;i++) ans+=F[n][i];
		printf("Case #%d: %d\n",ic,ans%MOD);
	}
	return 0;
}
