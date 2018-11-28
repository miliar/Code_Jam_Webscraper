#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>

using namespace std;

const double eps = 1e-5;
double x[10], y[10], r[10];
int n;
double dis(int a, int b){
	double dx = x[a]-x[b];
	double dy = y[a]-y[b];
	return sqrt( dx*dx+dy*dy );
}
int main(){
	freopen("D-small-attempt1.in","r",stdin);
	int turn, T;
	cin >> T;
	for(turn=0;turn<T;++turn){
		cin >> n;
		double min = 100000;
		for(int i=0;i<n;++i)	cin >> x[i] >> y[i] >> r[i];
		if( n==3 ){
			for(int i=0;i<n;++i){
				int j = (i+1)%n;
				double tmp = (dis(i,j) + r[i] + r[j])/2.0;
				if( tmp < min )	min = tmp;
			}
			for(int i=0;i<n;++i){
				if( min < r[i] )	min = r[i];
			}
		}else{
			min = -1;
			
			for(int i=0;i<n;++i){
				if( min < r[i] )	min = r[i];
			}
		}
		printf("Case #%d: %.6lf\n",1+turn,min);
	}
	return 0;
}
