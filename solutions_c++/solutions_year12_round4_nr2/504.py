#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

struct node {
	double x, y;
	void Rand(int W, int L) {
		x = (double)((int)rand()*10000+rand()%10000);
		x = ((int)x) % W;
		y = (double)((int)rand()*10000+rand()%10000);
		y = ((int)y) % L;
	}
	double r;
	int id;
} ;

node P[10005];

inline double dist(node a, node b) {
	return sqrt((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y))+1;
}

int comp1(const void * a, const void * b) {
	return ((node*)b)->r - ((node*)a)->r;
}

int comp2(const void * a, const void * b) {
	return ((node*)a)->id - ((node*)b)->id;
}
int main()
{
	int T;
	int N;
	double W, L;
	scanf("%d", &T);
	for ( int t = 1 ; t <= T ; t++ ) {
		scanf("%d%lf%lf", &N, &W, &L);
		for ( int i = 0 ; i < N ; i++ ) {
			scanf("%lf", &P[i].r);
			P[i].id = i;
		}
		qsort(P,N,sizeof(node),comp1);
		P[0].x = 0;
		P[0].y = 0;
		P[1].x = W;
		P[1].y = L;
		
		for ( int i = 2 ; i < N ; i++ ) {
			P[i].Rand(W,L);
			int key = 1;
			for ( int j = i-1 ; j >= 0 ; j-- ) {
				if ( dist(P[i], P[j]) < (P[i].r+P[j].r) ) {
					key = 0;
					break;
				}
			}
			if ( !key )	i--;
		}
		qsort(P,N,sizeof(node),comp2);
		printf("Case #%d:", t);
		for ( int i = 0 ; i < N ; i++ ) {
			printf(" %.2lf %.2lf", P[i].x, P[i].y);
		}
		puts("");
	}
	return 0;
}
