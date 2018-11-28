#include <stdio.h>

int T,N,C[1010],I,MIN;
int CASE; long long SUM;

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int i;

	scanf ("%d",&T); while (T--){
		scanf ("%d",&N); MIN = 0x7fffffff; SUM = 0; I = 0;
		for (i=0;i<N;i++){
			scanf ("%d",&C[i]); SUM += C[i];
			I ^= C[i];
			if (MIN > C[i]) MIN = C[i];
		}

		printf ("Case #%d: ",++CASE);
		if (I != 0) printf ("NO\n");
		else{
			printf ("%lld\n",SUM-MIN);
		}
	}

	return 0;
}