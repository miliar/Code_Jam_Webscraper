#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional> 
#include <numeric>
using namespace std;
#define foreach(i,v) for(__typeof((v).end()) i=(v).begin();i!=(v).end();++i)
#define rforeach(i,v) for(__typeof((v).rend()) i=(v).rbegin();i!=(v).rend();++i)
#define FOR(i,b,e) for(int i=(b);i<(e);++i)
#define FORE(i,b,e) for(int i=(b);i<=(e);++i)
#define debug(x) cerr << #x << " = " << (x) << "\n"
typedef long long LL;

int main(){
	int t;
	cin >> t;
	FORE(z,1,t){
		int n, d;
		cin >> n >> d;
		int p[n], c[n];
		FOR(i,0,n)
			cin >> p[i] >> c[i];
		double lo = 0, hi = 1e18;
		FOR(y,0,500){
//		while (hi-lo>1e-9){
			double m = (lo+hi)/2;
			double left=p[0]-3*m-3*d;
			bool gd = true;
			FOR(i,0,n)
				FOR(r,0,c[i]){
					left += d;
					if (p[i]-m>=left) left=p[i]-m;
					else if (p[i]>=left) left=left;
					else if (p[i]+m>=left) left=left;
					else gd=false;
				}
			if (gd) hi=m;
				else lo=m;
		}
		printf("Case #%d: %.12f\n",z,lo);
	}
	return 0;
}
