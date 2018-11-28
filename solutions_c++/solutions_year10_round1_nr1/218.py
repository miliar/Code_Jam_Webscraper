#include <cstdio>

const int N=51;

char A[N][N];
char B[N][N];
int n,K;

int main(){
	int cas,ic;
	scanf("%d",&cas);
	for(ic=1;ic<=cas;ic++){
		scanf("%d%d",&n,&K);
		int i,j,k;
		for(i=0;i<n;i++) scanf("%s",A[i]);
		for(j=0;j<n;j++){
			i=n-1;
			for(k=n-1;k>=0;k--){
				if(A[n-j-1][k]!='.') B[i--][j]=A[n-1-j][k];
			}
			for(;i>=0;i--) B[i][j]='.';
		}
		bool b,r;
		b=r=0;
		//for(i=0;i<n;i++) printf("%s\n",B[i]);
		for(i=0;i<n;i++){
			for(j=0;j<=n-K;j++){
				for(k=1;k<K;k++){
					if(B[i][j+k]!=B[i][j]) break;
				}
				if(k>=K&&B[i][j]!='.'){
					if(B[i][j]=='B') b=1;
					else r=1;
				}
			}
		}
		for(i=0;i<=n-K;i++){
			for(j=0;j<n;j++){		
				for(k=1;k<K;k++){
					if(B[i+k][j]!=B[i][j]) break;
				}
				if(k>=K&&B[i][j]!='.'){
					if(B[i][j]=='B') b=1;
					else r=1;
				}
			}
		}
		for(i=0;i<=n-K;i++){
			for(j=0;j<=n-K;j++){
				for(k=1;k<K;k++){
					if(B[i+k][j+k]!=B[i][j]) break;
				}
				if(k>=K&&B[i][j]!='.'){
					if(B[i][j]=='B') b=1;
					else r=1;
				}
			}
		}
		for(i=0;i<=n-K;i++){
			for(j=0;j<=n-K;j++){
				for(k=1;k<K;k++){
					if(B[i+k][j+K-1-k]!=B[i][j+K-1]) break;
				}
				if(k>=K&&B[i][j+K-1]!='.'){
					if(B[i][j+K-1]=='B') b=1;
					else r=1;
				}
			}
		}
		if(b==0&&r==0){
			printf("Case #%d: Neither\n",ic);
		}else if(b==1&&r==1){
			printf("Case #%d: Both\n",ic);
		}else if(b==1){
			printf("Case #%d: Blue\n",ic);
		}else printf("Case #%d: Red\n",ic);
	}
	return 0;
}
