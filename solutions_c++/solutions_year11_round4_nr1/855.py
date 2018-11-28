#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <deque>
#include <algorithm>
using namespace std;

#define _(a,b) memset(a,b,sizeof(a))
#define f(a,b,c) for(int a=b; a<c; a++)

int T, cnt, w, r, n, l;
double t, tt;
struct W {
	int bg, en, sp, t;
} V[2011];

bool cmp_bg(W w1, W w2){
	return w1.bg < w2.bg;
}

bool cmp_sp(W w1, W w2){
	return w1.sp < w2.sp;
}

int main(void){
	scanf("%d", &T);
	for(int cas=1; cas<=T; cas++){
		scanf("%d%d%d%lf%d", &l, &w, &r, &t, &n);
		for(int i=0; i<n; i++){
			scanf("%d%d%d", &V[i].bg, &V[i].en, &V[i].sp);
		}
		sort(V, V+n, cmp_bg);
		cnt=n;
		if(V[0].bg > 0){
			V[cnt].bg=0;
			V[cnt].en=V[0].bg;
			V[cnt++].sp=0;
		}
		for(int i=0; i<n-1; i++){
			if(V[i].en < V[i+1].bg){
				V[cnt].bg=V[i].en;
				V[cnt].en=V[i+1].bg;
				V[cnt++].sp=0;
			}
		}
		if(V[n-1].en < l){
			V[cnt].bg=V[n-1].en;
			V[cnt].en=l;
			V[cnt++].sp=0;
		}
		sort(V, V+cnt, cmp_sp);
		tt=0;
		for(int i=0; i<cnt; i++){
			double len=V[i].en-V[i].bg, dis;
			if(t>=0){
				dis=min(t*(r+V[i].sp), len);
				tt+=dis/(V[i].sp+r);
				t-=dis/(V[i].sp+r);
				len-=dis;
				if(len>0){
					tt+=len/(V[i].sp+w);
				}
			} else {
				tt+=len/(V[i].sp+w);
			}
		}
		printf("Case #%d: %.7lf\n", cas, tt);

	}
	return 0;
}
