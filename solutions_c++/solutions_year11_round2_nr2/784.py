#include <stdio.h>
#include <stdlib.h>
#define maxn 8100

int T,zu,D,C,V,P,tot;
int list[maxn];
double t;

int charge(double x){
	int i,j;
	double pos;
	pos = list[1] - x;
	for (i = 2; i <= tot; i++){
		if (list[i] + x - pos < D) return 0;
		if (list[i] - x - pos < D)
				pos = pos + D;
		else pos = list[i] - x;
	}
	return 1;
}

void process(){
	int i,j;
	double low,high,mid;
	low = 0;
	high = 110001000;
	while (high - low > 1e-8){
		mid = (low + high) / 2;
		if (charge(mid)) high = mid;
		else low = mid;
	}
	printf("Case #%d: %.7lf\n",zu,low);
}

int main(){
	int i,j,tem;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	for (zu = 1; zu <= T; zu++){
		tot = 0;
		scanf("%d%d",&C,&D);
		for (i = 1; i <= C; i++){
			scanf("%d%d",&P,&V);
			while (V > 0){
				list[++tot] = P;
				V--;
			}
		}
		process();
	}
	return 0;
}
