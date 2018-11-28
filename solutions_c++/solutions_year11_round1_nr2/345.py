#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

bool tb[30], flag[10010];
int T, N, M, len[10010], pos[12], minu[10010], ans[110];
char dict[10010][12];
char od[110][30];

int main()
{
	freopen("B-small-attempt2.in","r",stdin);

	int i, j, k, d, h, ct, cho, t = 0;
	int tmp;

	for ( scanf("%d",&T); T; T-- ) {
		for ( scanf("%d%d",&N,&M), i = 0; i < N; i++ ) {
			scanf("%s",dict[i]);
			len[i] = strlen(dict[i]);
		}
		for ( i = 0; i < M; i++ )
			scanf("%s",od[i]);

	printf("Case #%d:",++t);

	for ( i = 0; i < M; i++ ) {
		ans[i] = -1;
		for ( j = 0; j < N; j++ ) {
			minu[j] = 0;
			memset(flag,0,sizeof(flag));
			for ( k = 0; k < N; k++ )
				if ( len[k] != len[j] )
					flag[k] = 1;
			memset(tb,0,sizeof(tb));
			for ( cho = k = 0; k < N; k++ )
				if ( !flag[k] ) {
					cho++;
					for ( d = 0; dict[k][d]; d++ )
						tb[dict[k][d]-'a'] = 1;
				}
			for ( ct = k = 0; cho > 1 && ct < len[j] && k < 26; k++ )
				if ( tb[od[i][k]-'a'] == 1 ) {		
					for ( pos[0] = d = 0; dict[j][d]; d++ )
						if ( dict[j][d] == od[i][k] ) {
							pos[++pos[0]] = d;
						}
					if ( !pos[0] ) {
						minu[j]++;
						for ( d = 0; d < N; d++ )
							if ( !flag[d] ) {
								for ( h = 0; h < len[d]; h++ )
									if ( dict[d][h] == od[i][k] )
										break;
								if ( h < len[d] )
									flag[d] = 1;
							}
						memset(tb,0,sizeof(tb));
						for ( cho = d = 0; d < N; d++ )
							if ( !flag[d] ) {
								cho++;
								for ( h = 0; h < len[d]; h++ )
									tb[dict[d][h]-'a'] = 1;
							}
					}
					else {
						ct += pos[0];
						for ( d = 0; d < N; d++ )
							if ( !flag[d] ) {
								for ( h = 1; h <= pos[0]; h++ )
									if ( dict[d][pos[h]] != dict[j][pos[h]] )
										break;
								if ( h <= pos[0] )
									flag[d] = 1;
								for ( tmp = h = 0; h < len[d]; h++ )
									if ( dict[d][h] == dict[j][pos[1]] )
										tmp++;
								if ( tmp > pos[0] )
									flag[d] = 1;
							}
						memset(tb,0,sizeof(tb));
						for ( cho = d = 0; d < N; d++ )
                                                        if ( !flag[d] ) {
								cho++;
                                                                for ( h = 0; h < len[d]; h++ )
                                                                        tb[dict[d][h]-'a'] = 1;
                                                        }
					}
				} 
		}
		
		for ( j = N-1; j >= 0; j-- )
			if ( ans[i] == -1 || minu[ans[i]] <= minu[j] )
				ans[i] = j;
	}
	

	for ( i = 0; i < M; i++ )
		printf(" %s",dict[ans[i]]);
	putchar('\n');
	}

	return 0;
}

