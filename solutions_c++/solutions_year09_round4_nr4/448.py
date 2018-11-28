#include <cstdio>
#include <cmath>
#include <cassert>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

#define inf 0x3f3f3f3f
#define Eo(x) { cerr << #x << " = " << x << endl;}
double x[300],y[300],r[300];
int ferlon,_,n;
double sqr(double x){ return x*x;}
double rast(int i, int j){
	return sqrt(sqr(x[i]-x[j]) + sqr(y[i] - y[j]));
}
int main(){
	cin >> ferlon;
	for( _=0; _ < ferlon; _++){
		double ans;
		cin >> n;
		for ( int i = 0; i < n; i++)
			cin >> x[i]  >> y[i] >> r[i];
		if ( n == 1) ans = r[0];
		if ( n == 2){
			ans = std::max(r[0],r[1]);
		}
		if ( n == 3){
			ans = inf;
			ans = std::min(ans, std::max(r[0], (rast(1,2) + r[1] + r[2])/2));
			ans = std::min(ans, std::max(r[1], (rast(2,0) + r[2] + r[0])/2));
			ans = std::min(ans, std::max(r[2], (rast(0,1) + r[0] + r[1])/2));
		}

		assert ( n <=3);
		cout << "Case #" << ( _ + 1) << ": ";
		printf("%.10lf\n",ans);
	}
	return 0;
}

