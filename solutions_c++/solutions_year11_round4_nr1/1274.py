
#include <cstdio>
#include <algorithm>
using namespace std;

int X, S, R, RT, N;
int ws[1005], wb[1005], we[1005];
pair<int,int> es[1005];

main() {
	int ntc;
	scanf("%d", &ntc);
	for (int tec=1; tec<=ntc; tec++) {
		printf("Case #%d: ", tec);
	
		scanf("%d%d%d%d%d", &X, &S, &R, &RT, &N);
		double d2w=X;
		for (int w=0; w<N; w++) {
			scanf("%d%d%d",wb+w, we+w, ws+w);
			es[w]=make_pair(ws[w],w);
			d2w -= (we[w]-wb[w]);
		}
		
		double re=0, rt=RT;
		if (R*rt<d2w) {
			d2w -= R*rt;
			re += rt;
			rt = 0;
			re += d2w/S;
		} else {
			re += d2w/R;
			rt -= re;
		}
		
		sort(es,es+N);
		for (int w=0; w<N; w++) {
			int e=es[w].second;
			double len=we[e]-wb[e];
			double ttr=len/(R+ws[e]);
			if (ttr>rt) {
				re += rt;
				len -= (R+ws[e])*rt;
				rt = 0;
				re += len/(S+ws[e]);
			} else {
				re += ttr;
				rt -= ttr;
			}
		}
		printf("%.6lf\n", re);
	}
}
