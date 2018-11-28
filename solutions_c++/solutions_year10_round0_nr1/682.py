#include <stdio.h>

int T,N,C;
__int64 K,D[31];

int main()
{
	freopen ("A.in","r",stdin);
	freopen ("A.out","w",stdout);

	int i;

	D[1] = 1;
	for (i=2;i<=30;i++) D[i] = D[i-1] * 2 + 1;

	scanf ("%d",&T);
	while (T--){
		scanf ("%d %I64d",&N,&K);
		
		printf ("Case #%d: ",++C);
		if ((K + 1) % (D[N] + 1) == 0) printf ("ON\n");
		else printf ("OFF\n");
	}

	return 0;
}
