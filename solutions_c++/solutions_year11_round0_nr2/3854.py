#include<stdio.h>
char QC[5];
char QD[5];
char S[150];
char Q[150];
int nq;
int C, D, N;

int match(char A, char B) {
	return ( (QC[0] == A && QC[1] == B) || (QC[0] == B && QC[1] == A) );
}
int oppose(char A, char B) {
	return ( (QD[0] == A && QD[1] == B) || (QD[0] == B && QD[1] == A) );
}

int main()
{
	int i, j;
	int T, t;
	scanf("%d", &T);
	for ( t = 1 ; t <= T ; t++ ) {
		scanf("%d", &C);
		if ( C )
			scanf("%s", QC);
		scanf("%d", &D);
		if ( D )
			scanf("%s", QD);
		scanf("%d%s", &N, S);
		Q[0] = ' ';
		nq = 1;
		for ( i = 0 ; i < N ; i++ ) {
			Q[nq++] = S[i];
			while ( C && match(Q[nq-1], Q[nq-2]) ) {
				nq--;
				Q[nq-1] = QC[2];
			}
			if ( D ) {
				for ( j = 1 ; j <= nq-2 ; j++ ) {
					if ( oppose(Q[j],Q[nq-1]) ) {
						nq = 1;
						break;
					}
				}
			}
		}
		printf("Case #%d: [", t);
		if ( nq > 1 ) {
			for ( i = 1 ; i < nq-1 ; i++ ) {
				printf("%c, ",Q[i]);
			}
			printf("%c]\n",Q[nq-1]);
		}
		else {
			printf("]\n");
		}
	}
			 
	return 0;
}
