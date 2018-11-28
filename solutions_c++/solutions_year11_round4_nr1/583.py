// solution by Peter Ondruska

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstring>

#include <iostream>
#include <sstream>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <utility>
#include <numeric>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;
typedef long long ll;

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORTO(i,a,b)  for(int i=(a);i<=(b);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)
#define FORDTO(i,a,b) for(int i=(a);i>=(b);i--)
#define FOREACH(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)

#define DEBUG(x) cout<<'>'<<#x<<':'<<x<<endl
#define SIZE(X) int(X.size())

int C;

ll X, W, R, N;
double T;

typedef pair<ll,ll> PLL;

int main() {
	scanf("%d", &C);
    FORTO(c,1,C) {
		scanf("%lld %lld %lld %lf %lld", &X, &W, &R, &T, &N);
		if (R < W) T = 0;
		vector<PLL> Esk;
		ll SumLen = 0;
		FOR(i,N) {
			ll B, E, S;
			scanf("%lld %lld %lld", &B, &E, &S);
			Esk.push_back(PLL(S+W,E-B));
			SumLen += E-B;
		}
		
		Esk.push_back(PLL(W,X-SumLen));
		R -= W;
		sort(Esk.begin(),Esk.end());
		
		double t = 0.0;
		
		FOR(i,SIZE(Esk)) {
			double boost = (Esk[i].first + R);
			double Dist = T * boost;
			Dist = min(Dist,double(Esk[i].second));
			T -= Dist / boost;
			
			t += Dist / boost + (Esk[i].second-Dist) / Esk[i].first;
		}
		
		printf("Case #%d: %.9lf\n", c, t);
	}
	return 0;
}
