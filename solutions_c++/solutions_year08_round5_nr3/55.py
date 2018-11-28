#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define MAXN 15
#define MAXANAK 2004

using namespace std;

int dp[1050][MAXN];
int a,b,c,d,e,f,g;
int tinggi,panjang;
bool broke[MAXN][MAXN];
int jmlcase;
bool terisi[MAXN];
bool tersiksa[MAXN];
char sapi;

int main() {
	
	scanf("%d",&jmlcase);
	
	for (g = 0;g < jmlcase;g++) {
		printf("Case #%d: ",g + 1);
		scanf("%d%d\n",&tinggi,&panjang);
		//printf("%d %d\n",tinggi,panjang);
		memset(broke,0,sizeof(broke));
		for (a = tinggi;a >= 1;a--) {
			for (b = 1;b <= panjang;b++) {
				sapi = getchar();
				if (sapi == 'x') {
					
					broke[b][a] = 1;
					}
				}
			sapi = getchar();
			}
		memset(dp,-1,sizeof(dp));
		dp[0][0] = 0;
		
		for (a = 1;a <= tinggi;a++) {
			for (b = 0;b < (1 << panjang);b++) {
				if (dp[b][a - 1] == -1) continue;
				terisi[0] = terisi[panjang + 1] = 0;
				d = b;
				for (c = 1;c <= panjang;c++) {
					terisi[c] = d % 2;
					d /= 2;
					}
				for (d = 0;d < (1 << panjang);d++) {
					e = d;
					tersiksa[0] = tersiksa[panjang + 1] = 0;
					bool valid = 1;
					int jml = 0;
					for (f = 1;f <= panjang;f++) {
						tersiksa[f] = e % 2;
						jml += tersiksa[f];
						e /= 2;
						}
					
					for (f = 1;f <= panjang;f++) {
						if (tersiksa[f]) {
						if (broke[f][a] || tersiksa[f - 1] || tersiksa[f + 1] ||
						terisi[f - 1] || terisi[f + 1]) {
							valid = 0;
							break;
							}
						}
						}
						
					if (!valid) continue;
					//printf("%d %d %d\n",a,d,jml);
					dp[d][a] = max(dp[d][a],dp[b][a - 1] + jml);
					}
				}
			}
		
		int minanswer = -1;
		
		for (a = 0;a < (1 << panjang);a++) {
			minanswer = max(minanswer,dp[a][tinggi]);
			}
		
		printf("%d\n",minanswer);
		}
						
					
		
					
	
	return 0;
	}
