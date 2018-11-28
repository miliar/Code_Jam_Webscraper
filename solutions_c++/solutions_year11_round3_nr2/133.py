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

int Cases;
ll L, T, N, C;

#define MAXN 1000047

ll A[MAXN];

int main() {
	scanf("%d", &Cases);
    FORTO(c,1,Cases) {
    	scanf("%lld %lld %lld %lld", &L, &T, &N, &C);
    	ll Sum = 0;
    	FOR(i,C) {
    		scanf("%lld", &A[i]);
    		A[i] *= 2;
    		Sum += A[i];
		}
    	FOR(i,N-C) {
    		A[C+i] = A[i];
    		Sum += A[C+i];
    	}
    	
    	ll Min = 2*Sum;
    	
    	ll ISum = 0;
    	ll SumQ = 0;
    	priority_queue<ll> Q;
    	
    	FORD(i,N) {
    		// check
    		ll Delta = Sum-ISum;
    		ll Left  = min(A[i],Delta-T); // do konca useku - speedup
    		
    		if (Left >= 0 && L != 0) { // hotovo pred dorazenim do ciela
    			Min = min(Min, 2*(Sum-SumQ-Left) + 1*(SumQ+Left));
    		}
    		
    		// update
    		SumQ += A[i];
    		ISum += A[i];
    		
    		Q.push(-A[i]);
    		if (SIZE(Q) >= L) {
    			SumQ += Q.top();
    			Q.pop();
    		}
    		
    	}
    	
    	printf("Case #%d: %lld\n", c, Min/2);
	}
	return 0;
}

