#include <cstdio>
#include <cstring>

int DP[ 1000 ][22];

int N;

char STR[] = "welcome to code jam";
int STRLEN;
char INPUT[1000];

int main()
{
	int ccN,len;
	scanf("%d",&ccN);
	STRLEN = strlen( STR );
	for( int cc=0;cc<ccN;cc++ ) {
		memset( DP, 0, sizeof(DP) );
		scanf(" %[^\n] ", INPUT );
		len = strlen( INPUT );
		if( INPUT[0] == 'w' ) {
			DP[0][0] = 1;
		}
		for( int i=1;i<len;i++ ) {
			for( int j=0;j<STRLEN;j++ ) {
				if( INPUT[i] == STR[j] ) {
					if( j == 0 )
						DP[i][j] += 1;
					else
						DP[i][j] += DP[i-1][j-1];
				}
				DP[i][j] += DP[i-1][j];
				DP[i][j] %= 10000;
			}
		}
		/*
		for( int i=0;i<len;i++ ) {
			for( int j=0;j<STRLEN;j++ ) {
				printf("%d ", DP[i][j]);
			}
			printf("\n");
		}
		*/
		printf("Case #%d: %04d\n", cc+1, DP[len-1][STRLEN-1]);
	}
}
