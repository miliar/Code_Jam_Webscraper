#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;
typedef long long ll;
typedef vector<int> VI;
typedef vector<ll> VLL;
#define rep(i,N) for(i=0;i<N;i++)

int T,CA;
int N,M,D,ANS;
int MASS[555][555],MASSX[555][555],MASSY[555][555],SUM[555][555],SUMX[555][555],SUMY[555][555];

int out(int i, int j){ return SUM[i][j]; }
int outx(int i, int j){ return SUMX[i][j]; }
int outy(int i, int j){ return SUMY[i][j]; }

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int i,j,k;

	scanf ("%d",&T); while (T--){
		scanf ("%d %d %d",&N,&M,&D);
		for (i=1;i<=N;i++) for (j=1;j<=M;j++){
			scanf ("%1d",&MASS[i][j]);
			MASSX[i][j] = MASS[i][j] * i; MASSY[i][j] = MASS[i][j] * j;
			SUM[i][j] = SUM[i-1][j] + SUM[i][j-1] - SUM[i-1][j-1] + MASS[i][j];
			SUMX[i][j] = SUMX[i-1][j] + SUMX[i][j-1] - SUMX[i-1][j-1] + MASSX[i][j];
			SUMY[i][j] = SUMY[i-1][j] + SUMY[i][j-1] - SUMY[i-1][j-1] + MASSY[i][j];
		}
		ANS = -1;
		for (k=3;k<=min(N,M);k++){
			for (i=1;i<=N-k+1;i++){
				for (j=1;j<=M-k+1;j++){
					ll A = out(i+k-1,j+k-1) - out(i+k-1,j-1) - out(i-1,j+k-1) + out(i-1,j-1) - MASS[i][j] - MASS[i+k-1][j] - MASS[i][j+k-1] - MASS[i+k-1][j+k-1];
					ll X = outx(i+k-1,j+k-1) - outx(i+k-1,j-1) - outx(i-1,j+k-1) + outx(i-1,j-1) - MASSX[i][j] - MASSX[i+k-1][j] - MASSX[i][j+k-1] - MASSX[i+k-1][j+k-1];
					ll Y = outy(i+k-1,j+k-1) - outy(i+k-1,j-1) - outy(i-1,j+k-1) + outy(i-1,j-1) - MASSY[i][j] - MASSY[i+k-1][j] - MASSY[i][j+k-1] - MASSY[i+k-1][j+k-1];
					
					if (2 * X == A * (2 * i + k - 1) && 2 * Y == A * (2 * j + k - 1)) ANS = max(ANS,k);
				}
			}
		}

		printf ("Case #%d: ",++CA);
		if (ANS > 0) printf ("%d\n",ANS);
		else printf ("IMPOSSIBLE\n");
	}

	return 0;
}