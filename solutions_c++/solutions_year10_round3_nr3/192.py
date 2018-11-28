#include <stdio.h>
#define max(a,b) ((a>b)?(a):(b))
#define min(a,b) ((a<b)?(a):(b))

int T,N,M,C;
char ST[130];
int B[600][600][600],H[600][600][600];
int SI[600],CO[600],P;

int main()
{
	freopen ("C.in","r",stdin);
	freopen ("C.out","w",stdout);
	int i,j,x,y,k,o,c,v;

	scanf ("%d",&T);
	while (T--){
		scanf ("%d %d",&N,&M); P = 0;
		for (i=0;i<N;i++){
			scanf ("%s",ST);
			for (j=0;j<M/4;j++){
				if ('0' <= ST[j] && ST[j] <= '9') c = ST[j] - '0';
				else c = ST[j] - 'A' + 10;
				
				B[1][i][j*4+0] = (c & 8) / 8; H[1][i][j*4+0] = 0;
				B[1][i][j*4+1] = (c & 4) / 4; H[1][i][j*4+1] = 0;
				B[1][i][j*4+2] = (c & 2) / 2; H[1][i][j*4+2] = 0;
				B[1][i][j*4+3] = (c & 1) / 1; H[1][i][j*4+3] = 0;
			}
		}

		for (k=2;k<=min(N,M);k++){
			for (i=0;i<=N-k;i++){
				for (j=0;j<=M-k;j++){
					if (B[k-1][i][j] != -1 && B[k-1][i+1][j] != -1 && B[k-1][i][j+1] != -1 && B[k-1][i+1][j+1] != -1 &&
						B[k-1][i][j] == B[k-1][i+1][j+1] && B[k-1][i][j] != B[k-1][i+1][j] && B[k-1][i+1][j] == B[k-1][i][j+1]){
						B[k][i][j] = B[k-1][i][j];
					}
					else B[k][i][j] = -1;
					H[k][i][j] = 0;
				}
			}
		}

		for (k=min(N,M);k>=1;k--){
			v = 0;
			for (i=0;i<=N-k;i++){
				for (j=0;j<=M-k;j++){
					if (H[k][i][j] == 0 && B[k][i][j] != -1){
						for (o=1;o<=k;o++){
							for (x=max(0,i-o+1);x<=min(N-o,i+k-1);x++){
								for (y=max(0,j-o+1);y<=min(M-o,j+k-1);y++) H[o][x][y] = 1;
							}
						}
						v++;
					}
				}
			}
			if (v != 0){
				SI[P] = k; CO[P] = v; P++;
			}
		}

		printf ("Case #%d: %d\n",++C,P);
		for (i=0;i<P;i++) printf ("%d %d\n",SI[i],CO[i]);
	}

	return 0;
}
