// Author: Swarnaprakash
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const int M = 1000005;
const int INF = 0x3f3f3f3f;
const bool debug=true;
const double EPS = 1e-9;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define SZ(x)		((int)((x).size()))
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

int speed[M];

inline bool is_zero(double x) {
	return fabs(x) < EPS;
}

inline void make_zero(double &x) {
	if(x < 0.0 || is_zero(x)) x = 0.0;
}

int main() {
	int tc;
	scanf("%d",&tc);
	for(int t=1;t<=tc;++t) {
		int X,S,R,T,N;
		scanf("%d %d %d %d %d",&X,&S,&R,&T,&N);
		SET(speed,0);
		for(int i=0;i<N;++i) {
			int b,e,w;
			scanf("%d %d %d",&b,&e,&w);
			for(int j=b;j<e;++j) speed[j]=w;
		}
		sort(speed,speed+X);
		double ans=0.0;
		double rem = T;
		for(int i=0;i<X;++i) {
			double fast = speed[i] + R;
			double slow = speed[i] + S;
			double fast_d = min(1.0,fast*rem);
			double slow_d = 1.0 - fast_d;

			make_zero(fast_d);
			make_zero(slow_d);
			ans += fast_d/fast + slow_d/slow;
			rem -=  fast_d/fast;
			make_zero(rem);
		}
		printf("Case #%d: %0.9f\n",t,ans);
	}
	return 0;
}

