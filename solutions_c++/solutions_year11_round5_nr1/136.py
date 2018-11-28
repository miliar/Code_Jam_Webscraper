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

int W, L, U, lo[100][2], hi[100][2], G;

double acurve(int pt[][2], int len, double rhs){
	double res=0;
	for(int i=1; i<len; i++){
		if(pt[i][0]<=rhs){
			res+=(pt[i][0]-pt[i-1][0])/2.*(pt[i][1]+pt[i-1][1]);
		}else{
			double yval=((rhs-pt[i-1][0])*pt[i][1]+(pt[i][0]-rhs)*pt[i-1][1])/(pt[i][0]-pt[i-1][0]);
			res+=(rhs-pt[i-1][0])/2.*(yval+pt[i-1][1]);
			break;
		}
	}
	return res;
}

double area(double rhs){
	return acurve(hi, U, rhs)-acurve(lo, L, rhs);
}

void eval(){
	scanf("%d %d %d %d", &W, &L, &U, &G);
	for(int i=0; i<L; i++)
		scanf("%d %d", &lo[i][0], &lo[i][1]);
	for(int i=0; i<U; i++)
		scanf("%d %d", &hi[i][0], &hi[i][1]);
	double ar=area(W);
	for(int i=1; i<G; i++){
		double goal=ar*i/G;
		double lo=0, hi=W;
		for(int i=0; i<50; i++){
			double mid=(lo+hi)/2;
			if(area(mid)<goal)
				lo=mid;
			else
				hi=mid;
		}
		printf("%.7lf\n", (lo+hi)/2);
	}
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": "<<endl;
		eval();
	}
	return 0;
}
