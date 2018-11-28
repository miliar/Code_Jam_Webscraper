#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define MOD 10007
#define MAXN 150

using namespace std;

int jmlcase;
bool evil[MAXN][MAXN];
int movex[2] = {1,2};
int movey[2] = {2,1};
int dp[MAXN][MAXN];
int tinggi,panjang;
int a,b,c,d,e,f,g;
int jmlevil;

int main() {
	
	scanf("%d",&jmlcase);
	
	for (g = 0;g < jmlcase;g++) {
		printf("Case #%d: ",g + 1);
		memset(dp,0,sizeof(dp));
		
		scanf("%d%d%d",&tinggi,&panjang,&jmlevil);
		memset(evil,0,sizeof(evil));
		for (a = 0;a < jmlevil;a++) {
			scanf("%d%d",&b,&c);
			
			evil[c][b] = 1;
			}
		
		dp[1][1] = 1;
		for (a = 1;a <= tinggi;a++) {
			for (b = 1;b <= panjang;b++) {
				if (evil[b][a]) continue;
				for (c = 0;c < 2;c++) {
					d = b + movex[c];
					e = a + movey[c];
					
					dp[d][e] += dp[b][a];
					dp[d][e] %= MOD;
					}
				}
			}
		
		printf("%d\n",dp[panjang][tinggi]);
		}
					
		
	
	return 0;
	}
