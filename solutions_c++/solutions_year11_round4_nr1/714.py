#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;


int nCase=1, T;

int X, S, R, t, N;
struct Edge {
	int B, E, W;
	Edge() {}
	Edge(int b, int e, int w) : B(b), E(e), W(w) {
	}
	
	bool operator<(const Edge& e2) const {
		return this->B < e2.B;
	}
};

bool cmp ( const Edge& e1, const Edge& e2 ) {
	return e1.W < e2.W;
}

Edge E[2048];

void getInput() {
	scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
	R -= S;
	for(int i=0;i<N;++i) {
		int b, e, w;
		scanf("%d%d%d", &b, &e, &w);
		E[i] = Edge(b, e, w+S);
	}
}

double calc() {
	int NN = N;
	sort(E, E+N);
	int lastEnd = 0;
	for(int i=0;i<N;++i) {
		if( E[i].B != lastEnd ) {
			E[NN++] = Edge(lastEnd, E[i].B, S);
		}
		lastEnd = E[i].E;
	}
	if ( lastEnd != X ) {
		E[NN++] = Edge( lastEnd, X, S);
	}
	sort(E, E+NN, cmp);
	
	double tt = (double)t;
	double useTime = 0;
	for(int i=0;i<NN;++i) {
		double sp = E[i].W+R;
		double d = E[i].E - E[i].B;
		double cost = d/sp;
		if ( cost < tt ) {
			tt -= cost;
			useTime += cost;
		} else {
			double remDis = d - sp*tt;
			useTime += tt + remDis/E[i].W;
			tt = 0;
		}
	}
	return useTime;
}

int main()
{
	scanf("%d", &T);
	while(T-->0) {
        getInput();


		printf( "Case #%d: %.7f\n", nCase++, calc());
	}
	return 0;
}
