# include <cstdio>
# include <cstring>
# include <string>
# include <vector>
# include <set>
# include <map>
# include <algorithm>
# include <queue>
# include <cmath>
# include <stack>
# include <cassert>
# include <ctime>
# include <cstdlib>

# define EPS 1e-9

using namespace std;

int T, C, D;
int vet[256][2];


inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

double MAX (double a, double b){
	if( cmp(a,b) >= 0 ) return a;
	return b;
}

bool pode(double tempo){
	double last = -1000000000000000.0;
	// printf("%f\n", tempo);
	for(int i = 0 ; i < C; i++){
		double first = last + D;
		double secon  = -tempo + vet[i][0];
		double fato  = MAX(first, secon);
		last = fato + (vet[i][1]-1)*D;
		// printf("%f %f\n", fato, last);
		if( cmp(fabs(-fato + vet[i][0]), tempo) > 0 ) return false;
		if( cmp(fabs(last - vet[i][0]), tempo) > 0 ) return false;
	}
	return true;
}

int main (void){
	scanf("%d", &T);
	for(int tc = 1; tc <= T; tc++){
		scanf("%d%d", &C, &D);
		for(int i = 0 ; i < C; i++){
			scanf("%d%d", &vet[i][0], &vet[i][1]);
		}
		double lo = 0.0;
		double hi = 1000000000000000.0;
		double resp = 0.0;
		
		for(int i = 0 ; i <= 256; i++){
			double mid = lo + (hi-lo)/2;
			if( pode(mid) ){
				hi = mid;
				resp = mid;
			}
			else{
				lo = mid;
			}
		}
		printf("Case #%d: %.9f\n", tc, resp);
	}
	return 0;
}