#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

vector< pair<int,int> > V;

int T, X, S, R, N;
int B, E, w, D, dist;
double res, p, r;
int main() {
	freopen("google.in","r",stdin);
	freopen("google.out","w",stdout);
	int i, t;
	scanf("%d", &T);
	for(t=0;t<T;t++) {
		V.clear();
		res = p = 0;
		dist = 0;
		scanf("%d %d %d %lf %d", &X, &S, &R, &r, &N);	
		for(i=0;i<N;i++) {
			scanf("%d %d %d", &B, &E, &w);
			D = E - B;
			dist += D;
			V.push_back(make_pair(w, D));
		}
		V.push_back(make_pair(0, X-dist));
		sort(V.begin(), V.end());
		for(i=0;i<=N;i++) {
			p = (double) V[i].second / ( R + V[i].first );
			if(p <= r) {
				res += p;
				r -= p;					
			} else {
				res += r;
				res += (double) (V[i].second -  (R + V[i].first)*r ) / ( S + V[i].first );				
				r = 0;				
			}
		}		
		printf("Case #%d: %lf\n",t+1, res);
	}	
	return 0;	
}
