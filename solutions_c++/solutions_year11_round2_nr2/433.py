
#include <cstdio>
#include <algorithm>
using namespace std;

int C,D;
int pos[205], cnt[205];
double cost[205], sta[205], end[205];

double dabs(double x) {
	return x<0?-x:x;
}

main() {
	int ntc;
	scanf("%d", &ntc);
	for (int tec=1; tec<=ntc; tec++) {
	
		scanf("%d%d",&C,&D);
		for (int c=0; c<C; c++) {
			scanf("%d%d",pos+c, cnt+c);
		}
		
		for (int c=0; c<C; c++) {
			double spr=(cnt[c]-1)*1.0*D;
			cost[c]=spr/2;
			sta[c]=pos[c]-spr/2;
			end[c]=pos[c]+spr/2;
		}
		
		int NI=C;
		while(1) {
			bool opt=false;
			for (int a=0; a<NI-1; a++) {
				int b=a+1;
				double dif=sta[b]-end[a];
				if (dif<D) {
					opt=true;
					double sh=D-dif;
					if (cost[a]<cost[b]) {
						double sha=min(sh, cost[b]-cost[a]);
						sh-=sha;
						cost[a]+=sha;
						sta[a]-=sha; end[a]-=sha;
					}
					if (cost[b]<cost[a]) {
						double shb=min(sh, cost[a]-cost[b]);
						sh-=shb;
						cost[b]+=shb;
						sta[b]+=shb; end[b]+=shb;
					}
					if (sh>0) {
						cost[a]+=sh/2;
						cost[b]+=sh/2;
						sta[a]-=sh/2; end[b]+=sh/2;
					}
					cost[a]=max(cost[a],cost[b]);
					end[a]=end[b];
					
					for (int i=b+1; i<NI; i++) {
						cost[i-1]=cost[i];
						sta[i-1]=sta[i]; end[i-1]=end[i];
					}
					NI--;
					break;
				}
			}
			if (!opt) break;
		}
		
		double re=0;
		for (int c=0; c<NI; c++) {
			re=max(re,cost[c]);
		}
		printf("Case #%d: %.7lf\n", tec, re);
	}
}
