#include <cstdio>
#include <cstdlib>
#include <map>
#include <string>
#include <vector>
#define INF 0x3f3f3f3f

using namespace std;

char str[111], cquer[1111][111];
int qv[1010], prev[1111][111];

int dp[1111][111];

vector<string> query;
map<string, int> A;

int max(int a, int b) { return ( a > b ? a : b ); }

int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i, j, k, T, S, Q, test, minv, ans;
	string eng;
	
	scanf("%d\n", &T);
	
	for (test=1; test<=T; test++) {
		A.clear();
		
		scanf("%d\n", &S);
		
		for (i=1; i<=S; i++) {
			gets(str);
			eng = str;
			
			A[eng] = i;
		}
		
		scanf("%d\n", &Q);
		
		query.resize(Q+1);
		
		for (i=1; i<=Q; i++) {
			gets(str);
			query[i] = str;
			
			qv[i] = A[ query[i] ];
		}
		
		/*for (i=1; i<=Q; i++) {
			printf("%d\n", qv[i]);
		}
		
		printf("\n\n\n");*/
		
		for (j=1; j<=S; j++) prev[1][j] = 0;
		
		for (i=2; i<=Q; i++) {
			for (j=1; j<=S; j++) {
				if ( qv[i-1] == j ) prev[i][j] = i-1;
				else prev[i][j] = prev[i-1][j];
			}
		}
		
		for (j=1; j<=S; j++) {
			if ( qv[1] == j ) dp[1][j] = INF;
			else dp[1][j] = 0;
		}
		
		for (i=1; i<=Q; i++) {	
			for (j=1; j<=S; j++) {
				if ( qv[i] == j ) dp[i][j] = INF;
				else {
					minv = INF;
					for (k=1; k<=S; k++) {
						if ( dp[ prev[i][j] ][k] < minv ) minv = dp[ prev[i][j] ][k];
					}
					dp[i][j] = 1 + minv;
				}
			}
		}
		
		ans = INF;
		for (i=1; i<=S; i++) if ( dp[Q][i] < ans ) ans = dp[Q][i];
		
		ans = max(ans-1, 0);
		
		printf("Case #%d: %d\n", test, ans);
	}
	
	return 0;
}
