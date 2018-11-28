#include<stdio.h>
int N, P[1000], V[1000];
double D;
int f(double d) {
	double last = -1e12, start;
	int i;
	for(i=0;i<N;i++) {
		if(last + D > P[i] - d) start = last + D;
		else start = P[i]-d;
		if(start+D*(V[i]-1) > P[i] + d) return 0;
		last = start+D*(V[i]-1);
 }
	return 1;
}

int main() {
	int t,T,i,j;
	double st,en,ans;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		scanf("%d %lf",&N,&D);
		for(i=0;i<N;i++) scanf("%d %d",&P[i],&V[i]);
		st = 0;
		en = 1e12;

		for(i=0;i<100;i++) {
			ans = (st+en)/2;
			if(f(ans)) en = ans;
			else st = ans;
		}

		printf("Case #%d: %.9lf\n",t,ans);
	}
	return 0;
}
