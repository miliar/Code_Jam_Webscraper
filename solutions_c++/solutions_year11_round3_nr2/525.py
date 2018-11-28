#include<stdio.h>
#include<stdlib.h>
#include<string.h>


double Len[1005][3];
double S[1005];

int main()
{
	int i, j;
	int T;
	int L, time, N, M;
	double A, B;
	scanf("%d", &T);
	for ( int t = 1 ; t <= T ; t++ ) {
		scanf("%d %d %d %d", &L, &time, &N, &M);
		
		for ( i = 0 ; i < M ; i++ ) {
			scanf("%lf", &S[i]);
		}
		memset(Len,0,sizeof(Len));
		
		for ( i = 1 ; i <= N ; i++ ) {
			int pre = (i-1)%M;
			Len[i][0] = Len[i-1][0]+S[pre]*2;
			
			for ( j = 1 ; j <= L ; j++ ) {
				if ( time > Len[i-1][j-1] )
					A = Len[i-1][j-1] + S[pre] - ( time - Len[i-1][j-1] ) * 0.5 + time - Len[i-1][j-1];
				else
					A = Len[i-1][j-1] + S[pre];
				B = Len[i-1][j]+S[pre]*2;
				if ( A > B )
					Len[i][j] = B;
				else
					Len[i][j] = A;
			}
		}
		double min = Len[N][0];
		for ( i = 1 ; i <= L ; i++ ) {
			if ( Len[N][i] < min )
				min = Len[N][i];
		}
		printf("Case #%d: %.0lf\n", t, min);
	}
	return 0;
}
	