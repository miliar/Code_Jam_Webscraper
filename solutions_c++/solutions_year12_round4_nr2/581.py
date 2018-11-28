#include <cstdio>
#include <algorithm>
using namespace std;

int T , N, W, L;
struct cir{
	int r, x, y, i;
}a[1005];

bool cmp1(cir a,cir b){
	return a.r > b.r;
}

bool cmp2(cir a,cir b){
	return a.i < b.i;
}

int main(){
	scanf("%d", &T);
	for (int tc=1;tc<=T;++tc){
		scanf("%d%d%d", &N, &W, &L);
		
		for (int i=0;i<N;++i){
			scanf("%d", &a[i].r);
			a[i].i = i;
		}
		
		sort(a,a+N,cmp1);
		
		printf("Case #%d:", tc);
		
		{
			int x = 0;
			int y=0,my = 0;
			
			for (int i=0;i<N;++i){
				
				if (x) x += a[i].r;
				
				if (x > W){
					x = 0;
					y = my + a[i].r;
					my = y + a[i].r;
				}
				
				my = max(y+a[i].r,my);
				
				//printf(" %d %d", x, y);
				a[i].x = x;
				a[i].y = y;
				//if (y > L || x > W) puts("!!!!!");
				x += a[i].r;
			}
		}
		sort(a,a+N,cmp2);
		for (int i=0;i<N;++i){
			printf(" %d %d", a[i].x, a[i].y);
		//	if (a[i].x > W || a[i].y>L) puts("!!!");
		}
		
		puts("");
	}
	return 0;
}
