#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define ALL(cont) cont.begin(), cont.end()

using namespace std;

typedef long long ll;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vl;
typedef vector<double> vd;

int main()
{
	int T;
	cin >> T;
	REP(t,T)
	{
		int K;
		cin >> K;
		vii d(K, vi(K));
		REP(i,2*K-1)FOR(j,max(0,i-K+1),min(i+1,K)) cin >> d[i-j][j];
		
		vi v(2*K-1, 1),h(2*K-1, 1);
		REP(i,K)REP(j,K)REP(k,K)
		{
			if(i+k < K && j+k < K && d[i][j] != d[i+k][j+k])
				h[i+j+k] = 0;
			if(i-k >=0 && j+k < K && d[i][j] != d[i-k][j+k])
				v[K-1-i+j+k] = 0;
		}
		int a=K,b=K;
		REP(i,2*K-1) if(v[i] == 1) a = min(a, abs(i-K+1));
		REP(i,2*K-1) if(h[i] == 1) b = min(b, abs(i-K+1));
		int c = K+a+b;
		printf("Case #%d: %d\n", t + 1, c*c - K*K);
	}
	
	return 0;
}
