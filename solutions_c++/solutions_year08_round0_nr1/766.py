#pragma warning(disable:4786)

#include <stdio.h>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

#define Inf 999999999
#define min(a,b) (((a)<(b))?(a):(b))

int dp[2001][201];

int v[2001];


int main()
{

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

//	freopen("a.txt","r",stdin);
	int C;

	char search[1005];

	int p,i,j,k;

	int S,Q;

	while (scanf("%d",&C) != EOF) {
		for (p = 1; p <= C; p ++) {


			map<string,int> Map;

			
			scanf("%d ",&S);

			memset(dp,0,sizeof(dp));

			for (i = 0; i < S; i ++) { 
				gets(search);
				string Sear(search);
				Map[Sear] = i;
			}

			scanf("%d ",&Q);

			if (Q == 0) {
				printf("Case #%d: ",p);

				printf("0\n");
				continue;
			}


			for (i = 0; i < Q; i ++) {
			//	scanf("%s",search);
				gets(search);
				string Sear(search);

			/*	if (Map.find(Sear) == Map.end()) {
					printf("error\n");
				}*/
				v[i] = Map[Sear];
			}

			for (i = 0; i < S; i ++) {
				if (v[0] == i) {
					dp[0][i] = Inf;
				} else {
					dp[0][i] = 0;
				}
			}

			for (i = 1; i < Q; i ++) {
				for (j = 0; j < S; j ++) {

					if (j == v[i]) {
						// dp[i-1][j] ---> dp[i][j]  0<=j<S   j!=v[i] = dp[i-1][j] + 1;

						dp[i][j] = Inf;


						for (k = 0; k < S; k ++) {

							if (k != j) {

								dp[i][k] = min(dp[i][k],dp[i-1][j] + 1);
							}
						}



					} else {

						// j != v[i]

						int t = Inf;

						for (k = 0; k < S; k ++) {
							if (k == j) continue;

							t = min(t,dp[i-1][k] + 1);


						}

						t = min(t,dp[i-1][j]);

						dp[i][j] = t;
					}
				}
			}

			int ans = Inf;

			for (i = 0; i < S; i ++) {

				ans = min(ans,dp[Q-1][i]);
			}
		/*	for (i = 0; i < Q; i ++) {
				for (j = 0; j < S; j ++) {
					printf("[%d,%d]=%d ",i,j,dp[i][j]);
				}
				printf("\n");
			}
			printf("\n");*/
			
			printf("Case #%d: ",p);

			printf("%d\n",ans);







			

		}
	}

	int x = x;









	return 0;
}

