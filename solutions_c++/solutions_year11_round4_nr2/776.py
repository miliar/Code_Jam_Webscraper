#include <cstdio>
#include <cstring>
#include <cassert>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int ar[555][555];
char s[555];

#define EPS 1e-3

int main(){
	int tc, tcN;
	scanf("%d", &tcN);
	for(tc=0; tc<tcN; ++tc){
		int R, C, D;
		memset(ar, 0, sizeof(ar));
		scanf("%d %d %d", &R, &C, &D);
		gets(s);
		for(int i=0; i<R; ++i){
			gets(s);
			for(int j=0; j<C; ++j){
				ar[i+1][j+1] = s[j] - '0';
			}
		}

		for(int s = min(R, C); s>=3; --s){
			for(int i=1; i<=R-s+1; ++i){
				for(int j=1; j<=C-s+1; ++j){
					double sumx = (ar[i][j] + ar[i+s-1][j] - ar[i][j+s-1] - ar[i+s-1][j+s-1]) * .5 * (s-1) * -1;
					double sumy = (ar[i][j] + ar[i][j+s-1] - ar[i+s-1][j] - ar[i+s-1][j+s-1]) * .5 * (s-1) * -1;
					for(int ii=i; ii<i+s; ++ii){
						for(int jj=j; jj<j+s; ++jj){
							sumx += ar[ii][jj] * (j + .5 * (s-1) - jj);
							sumy += ar[ii][jj] * (i + .5 * (s-1) - ii);
						}
					}
					if(fabs(sumx) < EPS && fabs(sumy) < EPS){
						printf("Case #%d: %d\n", tc+1, s);
						goto end;
					}
				}
			}
		}
		printf("Case #%d: IMPOSSIBLE\n", tc+1);
end:
	;	
	}
}
