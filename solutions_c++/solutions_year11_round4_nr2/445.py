#include <cstdio>
#include <algorithm>
#include <cstring>
#define N 505
#define FOR(i,s,e) for (int i=(s); i<(int)(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(int)(e); i++)
using namespace std;

int tc, n, m, d, Sx[N][N], Sy[N][N], Sd[N][N], Dx[N][N], Dy[N][N], Dd[N][N];
int ret, ax, ay, ad, ex, ey;
char s[N];

int main(){

   	scanf("%d", &tc);
	FOE(c,1,tc){

		scanf("%d%d%*d", &n, &m);
		
		FOE(i,1,n){
			scanf("%s", s);
			FOE(j,1,m){
				d = s[j-1] - '0' + 1;
				Sd[i][j] = Sd[i][j-1] + Sd[i-1][j] - Sd[i-1][j-1] + d;
				Sx[i][j] = Sx[i][j-1] + Sx[i-1][j] - Sx[i-1][j-1] + d * i;
				Sy[i][j] = Sy[i][j-1] + Sy[i-1][j] - Sy[i-1][j-1] + d * j;
				Dx[i][j] = d * i;
				Dy[i][j] = d * j;
				Dd[i][j] = d;
			}
		}
		
		ret = 0;
		
		FOE(i,1,n){
			FOE(j,1,m){
				FOE(k, max(3, ret+1), min(i, j)){

					ax = Sx[i][j] - Sx[i-k][j] - Sx[i][j-k] + Sx[i-k][j-k];
					ay = Sy[i][j] - Sy[i-k][j] - Sy[i][j-k] + Sy[i-k][j-k];
					ad = Sd[i][j] - Sd[i-k][j] - Sd[i][j-k] + Sd[i-k][j-k];
					
					ax -= Dx[i][j] + Dx[i-k+1][j] + Dx[i][j-k+1] + Dx[i-k+1][j-k+1];
					ay -= Dy[i][j] + Dy[i-k+1][j] + Dy[i][j-k+1] + Dy[i-k+1][j-k+1];
					ad -= Dd[i][j] + Dd[i-k+1][j] + Dd[i][j-k+1] + Dd[i-k+1][j-k+1];
					
					ex = i*2 - (k-1);
					ey = j*2 - (k-1);
					
					if (ax*2%ad !=0 || ax*2/ad != ex) continue;
					if (ay*2%ad !=0 || ay*2/ad != ey) continue;

					if (k > ret) ret = k;
				}
			}
		}


		printf("Case #%d: ", c);
		if (ret < 3) printf("IMPOSSIBLE\n");
		else printf("%d\n", ret);

	}

	return 0;
}
