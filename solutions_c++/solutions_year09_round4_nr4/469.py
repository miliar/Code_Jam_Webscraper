#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<sstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;

#define LET(x,a) 	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	IFOR(it,v.begin(),v.end())
#define FOR(i,a,b)  	for(int i=(int)(a) ; i < (int)(b);++i)
#define REP(i,n) 	FOR(i,0,n)
#define PB		push_back
#define MP 		make_pair
#define EPS		1e-9
#define INF 2000000000

typedef vector<int>	VI;
typedef long long	LL;
typedef pair<int,int>	PI;
int main() {
	int t;
	scanf("%d",&t);
	for (int kases = 1; kases <= t; ++ kases) { 
		cout << "Case #"<<kases <<": ";
		int n;
		scanf("%d",&n);
		int x[100],y[100],r[100];
		REP(i,n) scanf("%d%d%d",&x[i],&y[i],&r[i]);
		if ( n == 1) {
			printf("%.6Lf\n",(long double)r[0]);
			continue;
		}
		if( n== 2) {
			int m = max(r[0],r[1]);
			printf("%.6Lf\n",(long double)m);
			continue;
		}
		int rm = 0;
		for ( int i = 0 ; i < 3; ++i) rm = max(rm,r[i]);
		long double ans = 1000000000.00;
		for ( int i = 0 ; i < 3; ++i ) {
			for (int j = i + 1 ; j < 3 ; ++j) {
				long double dist = (x[i] - x[j])*(x[i] - x[j]) + (y[i] - y[j])*(y[i] - y[j]);
				dist = sqrtl(dist);
				dist += r[i] + r[j];
				dist /= 2;
				if (dist < rm) dist = rm;
				
				if ( ans > dist ) ans = dist;
			}
		}
		printf("%.6Lf\n",ans);
	}
return 0;
}

