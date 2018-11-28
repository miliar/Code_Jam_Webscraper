#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <cmath>
#include <limits>
#define FWD(a,b,c) for(int a=(b); a<(c); a++)
#define BCK(a,b,c) for(int a=(b); a>(c); a--)
#define FE(a,b) for(typeof(b.end()) a=b.begin(); a!=b.end(); a++)
#define ALL(a) a.begin(), a.end()
#define UNIQUE(a) erase(unique(a.begin(), a.end()), a.end())
#define LL long long
#define ULL unsigned long long
#define PII pair<int, int>
#define PDD pair<double, double>
#define x first
#define y second
#define PACKS(a) int a; scanf("%d", &a); a++; while(--a)

//#define DEBUG
#ifdef DEBUG
	#define debug printf
#else
	#define debug
#endif

using namespace std;

int n, k;
double K[110];
double WP[110];
double OWP[110];
double OOWP[110];
char M[110][110];

inline double przekrec(int i, int j){
	if(M[i][j] == '.')
		return WP[j] / K[j];
	if(M[j][i] == '0')
		return WP[j] / (K[j] - 1.0);
	if(M[j][i] == '1')
		return (WP[j] - 1.0) / (K[j] - 1.0);
}

int main(){
	int z;
	scanf("%d", &z);
	FWD(i,0,z){
		printf("Case #%d:\n", i+1);
		scanf("%d", &n);
		FWD(i,0,n)
			scanf("%s", M[i]);
		FWD(i,0,n){
			WP[i] = OWP[i] = OOWP[i] = 0;
			k = 0;
			FWD(j,0,n)
				switch(M[i][j]){
					case '.': break;
					case '1':
						++WP[i];
					case '0':
						++k;
				}
			K[i] = k;
		}
		FWD(i,0,n){
			k = 0;
			FWD(j,0,n)
				if(M[i][j] != '.'){
						OWP[i] += przekrec(i, j);
						++k;
				}
			OWP[i] /= k;
		}
		FWD(i,0,n){
			k = 0;
			FWD(j,0,n)
				if(M[i][j] != '.'){
						OOWP[i] += OWP[j];
						++k;
				}
			OOWP[i] /= k;
			printf("%.7lf\n", 0.25 * (WP[i]/K[i]) + 0.5 * OWP[i] + 0.25 * OOWP[i]);
		}
	}
	return 0;
}

