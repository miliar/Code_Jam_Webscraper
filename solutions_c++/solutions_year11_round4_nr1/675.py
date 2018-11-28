#include <cstdio>
#include <map>
using namespace std;

#define rep(i,a,b) for (int i=(a); i<(b); ++i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)

int main() {
	int T;
	scanf("%d", &T);
	rep(t,0,T) {
		int X, S, R, M, N; // M is t!
		scanf("%d%d%d%d%d",&X,&S,&R,&M,&N);
		int pos = 0;
		R -= S;
		map<int,int> spdist;
		rep(n,0,N) {
			int B,E,W;
			scanf("%d%d%d", &B,&E,&W);
			spdist[S] += B-pos;
			spdist[S+W] += E-B;
			pos = E;
		}
		spdist[S] += X-pos;
		
		long double ti = 0;
		trav(it, spdist) {
			int S = it->first;
			long double l = it->second;
			if(ti>=M) // No running left
				ti += l/S;
			else if(ti+(l/(R+S))<=M) // Run all the way
				ti += l/(R+S);
			else { // Run partially
				l -= (M-ti)*(R+S);
				ti = M;
				ti += l/S;
			}
		}
		
		printf("Case #%d: %.8Lf\n",t+1, ti);
	}
	return 0;
}