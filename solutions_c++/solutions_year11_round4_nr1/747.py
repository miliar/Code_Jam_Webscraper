#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct node {
	double A, B, W;
} ;

node p[1005];

int comp(const void * a, const void *b) {
	double w1 = ((node*)a)->W;
	double w2 = ((node*)b)->W;
	if ( w1 < w2 )
		return -1;
	return 1;
}

int main()
{
	int j;
	int T;
	int N;
	double L, w, run, time;
	int M;
	scanf("%d", &T);
	for ( int t = 1 ; t <= T ; t++ ) {
		memset(p,0,sizeof(p));
		scanf("%lf%lf%lf%lf%d", &L, &w, &run, &time, &M);
		double LL = L;
		for ( j = 0 ; j < M ; j++ ) {
			scanf("%lf%lf%lf", &p[j].A, &p[j].B, &p[j].W);
			LL -= p[j].B - p[j].A;
		}
		p[j].A = 0;
		p[j].B = LL;
		p[j].W = 0;
		qsort(p,M+1,sizeof(node),comp);
		
		double total = 0;
		for ( j = 0 ; j < M+1 ; j++ ) {
			double cost = (p[j].B-p[j].A)/(p[j].W+run);
			if ( time >= cost ) {
				time -= cost;
				total += cost;
			}
			else {
				total += time;
				double dist = p[j].B-p[j].A - time * (p[j].W+run);
				time = 0;
				total += dist/(p[j].W+w);
			}
		}
		printf("Case #%d: ", t);
		printf("%.9lf\n", total);
	}
	return 0;
}