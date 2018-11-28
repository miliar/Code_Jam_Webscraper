#include<cstdio>
#include<vector>
#include<list>
#include<queue>
#include<stack>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>
#include<cstdlib>
#include<time.h>
#include<iostream>
#include<map>
#include<set>
using namespace std;
#define REP(i,n) for(int i=0;i<(n); ++i)
#define FOREACH(it,V) for(typeof((V).begin()) it = (V).begin(); it!=(V).end(); ++it)
vector<double> tmp;
const double eps = 0.0000003;
double D;
bool check(double d){
	double limit = -1000000000;
	FOREACH(it,tmp){
		if(limit+D>*it+d+eps){
			//printf("return false\n");
			return false;
			}
		limit = max(limit+D, *it-d);
		//printf("%lf %lf %lf\n", limit, *it, D);
	}
	return true;
}
int main(){
	double res,P,a,b,c;
	int z,C,V; scanf("%d", &z); REP(jj,z) {
		scanf("%d%lf", &C, &D);
		while(C--){
			scanf("%lf%d", &P, &V);
			REP(i,V) tmp.push_back(P);
		}
		a = 0; b = 4000000;
		while(b-a>=eps){
			//printf("%.9lf %.9lf %.9lf %.9lf\n", a, b, b-a, eps);
			c = (a+b)/2;
			if(check(c)) b = c;
			else a = c;
		}
		printf("Case #%d: %.9lf\n", jj+1, c);
		tmp.clear();
		//printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
	}
	return 0;
}

