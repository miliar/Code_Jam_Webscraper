#include <cstdio>
#include <cstdlib>

const int N=256;
const int INF=65536;

int A[N][N];

int n;

bool in(int x,int y){
	return x>=0&&x<2*n-1&&y>=0&&y<2*n-1;
}

int calc(int x,int y){
	int i,j;
	for(i=0;i<2*n-1;i++){
		for(j=0;j<2*n-1;j++){
			if(A[i][j]==-1) continue;
			if(in(2*x-i,j)&&A[2*x-i][j]!=-1&&A[2*x-i][j]!=A[i][j]) return INF;
			if(in(i,2*y-j)&&A[i][2*y-j]!=-1&&A[i][2*y-j]!=A[i][j]) return INF;
		}
	}
	//if(x==2&&y==3) printf("here %d,%d\n",abs(n-1-x),abs(n-1-y));
	int d=abs(n-1-x)+abs(n-1-y);
	return d*(2*n+d);
}

int main(){
	
	int cas,ic;
	scanf("%d",&cas);
	for(ic=1;ic<=cas;ic++){
		scanf("%d",&n);
		int i,j;
		for(i=0;i<N;i++){
			for(j=0;j<N;j++) A[i][j]=-1;
		}
		for(i=1;i<=n;i++){
			for(j=0;j<i;j++) scanf("%d",&A[i-1][n-i+j*2]);
		}
		for(i=n+1;i<2*n;i++){
			for(j=0;j<2*n-i;j++) scanf("%d",&A[i-1][i-n+j*2]);
		}
		
		//output()
		/*for(i=0;i<2*n-1;i++){
			for(j=0;j<2*n-1;j++) printf("%d ",A[i][j]);
			printf("\n");
		}*/
		
		int ans=INF;
		for(i=0;i<2*n;i++){
			for(j=0;j<2*n;j++){
				int cur=calc(i,j);
				if(ans>cur) ans=cur;
			}
		}
		printf("Case #%d: %d\n",ic,ans);
	}
	return 0;
}

						
