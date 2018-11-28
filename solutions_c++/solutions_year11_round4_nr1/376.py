#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

vector< pair<int,int> > V;

int main() {
	int t,T,i,j,N,L,S,R,D,e,s,w;
	double sec, tot;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
        tot = 0;
		scanf("%d %d %d %lf %d",&L,&S,&R,&sec,&N);
		V.clear();
		for(i=0;i<N;i++) {
			scanf("%d %d %d",&s,&e,&w);
			V.push_back( make_pair( w, e-s ) );
			L -= e-s;
		}
		V.push_back( make_pair( 0, L ) );
		sort(V.begin(),V.end());
		for(i=0;i<=N;i++) {
			double t = V[i].second * 1.0 / (R + V[i].first);
			if(t <= sec) {
				tot += t;
				sec -= t;
			} else {
				tot += sec;
				tot += (V[i].second - (R + V[i].first)*sec)/(S + V[i].first);
				sec = 0;
			}
		}
		printf("Case #%d: %.9lf\n",t,tot);
	}
	return 0;
}
