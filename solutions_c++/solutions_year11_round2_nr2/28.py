#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

int D, C, P[1000000], N;

bool can(double t){
	double pos=P[0]-t;
	for(int i=1; i<N; i++){
		double next=max(pos+D, P[i]-t);
		if(next>P[i]+t)
			return false;
		pos=next;
	}
	return true;
}

void eval(){
	double lo=0, hi=1e9;
	scanf("%d %d", &C, &D);
	N=0;
	for(int i=0; i<C; i++){
		int p, v;
		scanf("%d %d", &p, &v);
		for(int j=0; j<v; j++)
			P[N++]=p;
	}
	debug(N);
	sort(P, P+N);
	while(hi-lo>1e-7){
		double mid=(lo+hi)/2;
		if(can(mid))
			hi=mid;
		else
			lo=mid;
	}
	printf("%.6lf\n", (lo+hi)/2);
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}
