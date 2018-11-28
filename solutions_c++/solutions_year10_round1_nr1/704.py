#include <stdio.h>

#define MAX 52

char table[MAX][MAX];

int main()
{
	int T, N, K;
	scanf("%d", &T);
	for (int cases = 0; cases < T; cases++) {
		scanf("%d%d", &N, &K);
		for (int n = 0; n<N; n++)
			scanf("%s", table[n]);

		for (int i = 0; i<N; i++)
			for (int l = N-1; l>0; l--) {
				if (table[i][l] == '.') {
					int k;
					for (k = l-1; k>=0 && table[i][k] == '.'; k--);
					if (k>=0) {
						table[i][l] = table[i][k];
						table[i][k] = '.';
					}
					else
						break;
				}
			}

		int Rwin = 0;
		int Bwin = 0;


		for (int i = 0; i<N; i++)
			for (int j = 0; j<=N-K; j++) {
				int tmpj;
				for (tmpj = j; table[i][tmpj] =='R' && tmpj <=N; tmpj++);
				if (tmpj >= j+K)	Rwin = 1;
				for (tmpj = j; table[i][tmpj] =='B' && tmpj <= N; tmpj++);
				if (tmpj >= j+K)	Bwin = 1;
			}
		for (int i = 0; i<=N-K; i++)
			for (int j = 0; j<N; j++) {
				int tmpi;
				for (tmpi = i;table[tmpi][j]=='R' && tmpi <=N ; tmpi++);
				if (tmpi >= i+K)	Rwin = 1;
				for (tmpi = i;table[tmpi][j]=='B' && tmpi <= N; tmpi++);
				if (tmpi >= i+K)	Bwin = 1;
			}
		for (int i = 0; i<=N-K; i++)
			for (int j = 0; j<=N-K; j++) {
				int tmpi, tmpj;
				for (tmpi = i, tmpj = j; table[tmpi][tmpj] == 'R' && tmpi <=N && tmpj <=N; tmpi++, tmpj++);
				if (tmpi >= i+K)	Rwin = 1;
				for (tmpi = i, tmpj = j; table[tmpi][tmpj] == 'B' && tmpi <=N && tmpj <=N; tmpi++, tmpj++);
				if (tmpi >= i+K)	Bwin = 1;
			}
		for (int i = 0; i<=N-K; i++)
			for (int j = K-1; j<N; j++) {
				int tmpi, tmpj;
				for (tmpi = i, tmpj = j; table[tmpi][tmpj] =='R' && tmpi <=N && tmpj >=0; tmpi++, tmpj--);
				if (tmpi >= i+K)	Rwin = 1;
				for (tmpi = i, tmpj = j; table[tmpi][tmpj] =='B' && tmpi <=N && tmpj >=0; tmpi++, tmpj--);
				if (tmpi >= i+K)	Bwin = 1;
			}

		printf("Case #%d: ", cases+1);
		if (Rwin==1 && Bwin == 1)
			printf("Both\n");
		else if (Rwin == 1 && Bwin == 0)
			printf("Red\n");
		else if (Rwin == 0 && Bwin == 1)
			printf("Blue\n");
		else
			printf("Neither\n");
	}
	return 0;
}
