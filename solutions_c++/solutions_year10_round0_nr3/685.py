#include <stdio.h>
#define MAX_N 1111

__int64 R,K,G[MAX_N*2],S[MAX_N],U[MAX_N],E[MAX_N],W,P,Z,Y;
int T,N,C,X,L,I[MAX_N];

int main()
{
	freopen ("C.in","r",stdin);
	freopen ("C.out","w",stdout);
	int i,j;

	scanf ("%d",&T);
	while (T--){
		scanf ("%I64d %I64d %d",&R,&K,&N); P = 0;
		for (i=0;i<N;i++) scanf ("%I64d",&G[i]), G[i+N] = G[i], E[i] = 0;
		for (i=0;i<N;i++){
			W = 0;
			for (j=i;j<i+N;j++){
				if (W + G[j] > K) break;
				W += G[j];
			} j %= N;

			S[i] = W; I[i] = j;
		}

		U[1] = S[0]; X = I[0]; L = 2; E[0] = 1;
		if (X != 0){
			E[X] = 2;
			while (1){
				U[L] = U[L-1] + S[X]; L++;
				if (E[I[X]] != 0) break;
				E[I[X]] = E[X] + 1; X = I[X];
			}
		}

		Y = E[X] - E[I[X]] + 1;
		printf ("Case #%d: %I64d\n",++C,(U[L-1]-U[L-Y-1])*((R-L+Y)/Y)+U[(R-L+Y)%Y+L-Y]);
	}

	return 0;
}
