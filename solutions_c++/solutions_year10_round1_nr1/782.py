#include <stdio.h>

int T,N,K,P,R,B,S;
char D[55][55];
char C[55][55];

int main()
{
	freopen ("A.in","r",stdin);
	freopen ("A.out","w",stdout);
	int i,j,k;

	scanf ("%d",&T);
	while (T--){
		scanf ("%d %d",&N,&K);
		for (i=0;i<N;i++){
			scanf ("%s",&D[i]); P = N-1;
			for (j=N-1;j>=0;j--) if (D[i][j] != '.') C[i][P--] = D[i][j];
			for (P;P>=0;P--) C[i][P] = '.';
			C[i][N] = '\0';
		}
		R = B = 0;
		for (i=0;i<N;i++){
			for (j=0;j<N;j++){
				if (i + K <= N){
					for (k=1;k<K;k++) if (C[i][j] != C[i+k][j]) break;
					if (k == K){
						if (C[i][j] == 'R') R = 1;
						if (C[i][j] == 'B') B = 1;
					}
				}
				if (j + K <= N){
					for (k=1;k<K;k++) if (C[i][j] != C[i][j+k]) break;
					if (k == K){
						if (C[i][j] == 'R') R = 1;
						if (C[i][j] == 'B') B = 1;
					}
				}
				if (i + K <= N && j + K <= N){
					for (k=1;k<K;k++) if (C[i][j] != C[i+k][j+k]) break;
					if (k == K){
						if (C[i][j] == 'R') R = 1;
						if (C[i][j] == 'B') B = 1;
					}
				}
				if (i + K <= N && j - K >= -1){
					for (k=1;k<K;k++) if (C[i][j] != C[i+k][j-k]) break;
					if (k == K){
						if (C[i][j] == 'R') R = 1;
						if (C[i][j] == 'B') B = 1;
					}
				}
			}
		}

		printf ("Case #%d: ",++S);
		if (R & B) printf ("Both\n");
		else if (R) printf ("Red\n");
		else if (B) printf ("Blue\n");
		else printf ("Neither\n");
	}

	return 0;
}
