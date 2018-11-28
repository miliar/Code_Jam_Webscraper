#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<memory.h>

#define DEBUG1

int const inf = 2147483647;

int dp[1024][1024] = {0};
int S,Q,N;
char search[128][128];
int query[1024];
int res;

int main(int argc, char* argv[]) {
#define MAXLEN 4096
	char line[MAXLEN];
	int nc;
	nc = 0;
	fgets(line, MAXLEN, stdin);
	sscanf(line, "%d", &N);
	while (N--) {
		fgets(line, MAXLEN, stdin);
		sscanf(line, "%d", &S);
		for ( int i = 1 ; i <= S ; ++i ) {
			fgets(search[i], 128, stdin);
			search[i][strlen(search[i])-1] = 0;
#ifdef DEBUG
					printf("%d-%s\n", i, search[i]);
#endif
		}

		fgets(line, MAXLEN, stdin);
		sscanf(line, "%d", &Q);
		for ( int i = 1 ; i <= Q ; ++i ) {
			fgets(line, 128, stdin);
			line[strlen(line)-1] = 0;
			for ( int j = 1 ; j <= S ; ++j ) {
				if ( strcmp(line, search[j]) == 0 ) {
					query[i] = j;
#ifdef DEBUG
					printf("%d-%s\n", j, line);
#endif
					break;
				}
			}
		}
		
		for ( int i = 0 ; i <= Q ; ++i ) {
			for ( int j = 0 ; j <= S ; ++j ) {
				dp[i][j] = inf;
			}
		}

		dp[0][0] = 0;
		query[0] = -1;

		for ( int i = 0 ; i < Q ; ++i ) {
			int min = inf;
			for ( int j = 0 ; j <= S ; ++j ) {
				if ( dp[i][j] == inf ) continue;
				if ( j == query[i] ) continue;
				min = min<dp[i][j]?min:dp[i][j];
				if ( j != query[i+1] && j != 0 )
					dp[i+1][j] = dp[i][j]<dp[i+1][j]?dp[i][j]:dp[i+1][j];
			}
			min = min + 1;
			for ( int j = 1 ; j <= S ; ++j ) {
				dp[i+1][j] = dp[i+1][j]<min?dp[i+1][j]:min;
			}
		}

		res = inf;
		for ( int i = 1 ; i <= S ; ++i ) {
			if ( i == query[Q] ) continue;
			res = res<dp[Q][i]?res:dp[Q][i];
		}
		if (res == inf) res = 1;

		++nc;
		printf("Case #%d: %d\n", nc, res-1);
	}
	return 0;
}

