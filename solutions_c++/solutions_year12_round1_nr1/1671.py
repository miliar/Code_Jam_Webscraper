#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
using namespace std;
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)

typedef long long ll;
#define INF (1<<29)

int dpow(int n){
	int ret=1;
	for(int i=1;i<n;i++)ret*=10;
	return ret;
}

int main(){
	int t, tc, i, j, a, b;
	double p[110000], pp[2][110000];
	cin >> t;
	REP(tc,t){
		double ret=300000., su=1., tmp;
		cin >> a >> b;
		REP(i,a){
			cin >> p[i];
			su*=p[i];
		}
		double db=(double)b, da=(double)a;
		double x=db-da+1., y=x+db+1.;
		ret=su*x+(1.-su)*y;
		ret=min(ret,db+2.);
		REP(i,a){
			x+=2.;
			y+=2.;
			su=su/p[a-i-1];
			tmp=su*x+(1.-su)*y;
			ret=min(ret,tmp);
		}
		printf("Case #%d: %lf",tc+1,ret);
		puts("");
	}
	return 0;
}

