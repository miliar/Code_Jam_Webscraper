#include <cstdio>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>

using namespace std;

double X[3];
double Y[3];
double R[3];

int main(){
	int tc, tcN;
	
	scanf("%d", &tcN);
	for(tc=1; tc<=tcN; ++tc){
		int N;
		scanf("%d", &N);
		for(int i=0; i<N; ++i)
			scanf("%lf %lf %lf", &X[i], &Y[i], &R[i]);
		if(N == 1){
			printf("Case #%d: %.10lf\n", tc, R[0]);
		}else if(N == 2){
			printf("Case #%d: %.10lf\n", tc, max(R[0], R[1]));
		}else{
			double best = 1e10;
			for(int i=0; i<3; ++i){
				int a = (i+1)%3;
				int o = (i+2)%3;
				double dx = X[a] - X[o];
				double dy = Y[a] - Y[o];
				best = min(best, .5*(sqrt(dx*dx + dy*dy) + R[a] + R[o]));
			}
			for(int i=0; i<3; ++i)
				best = max(best, R[i]);
			printf("Case #%d: %.10lf\n", tc, best);
		}
	}
}
