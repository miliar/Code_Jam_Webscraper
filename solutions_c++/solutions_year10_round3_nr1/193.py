#include <stdio.h>

int T,N,X[1111],Y[1111],C,S;

int main()
{
	freopen ("A.in","r",stdin);
	freopen ("A.out","w",stdout);
	int i,j;

	scanf ("%d",&T);
	while (T--){
		scanf ("%d",&N); S = 0;
		for (i=0;i<N;i++) scanf ("%d %d",&X[i],&Y[i]);
		for (i=0;i<N;i++){
			for (j=i+1;j<N;j++){
				if (X[i] < X[j] && Y[i] > Y[j]) S++;
				if (X[i] > X[j] && Y[i] < Y[j]) S++;
			}
		}
		printf ("Case #%d: %d\n",++C,S);
	}

	return 0;
}
