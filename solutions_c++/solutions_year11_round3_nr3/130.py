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

#define MAX 10047

ll Val[MAX];
ll N, Dw, Up;


int main() {
	int T;
    scanf("%d", &T);
    FORTO(t,1,T) {
    	scanf("%lld %lld %lld", &N, &Dw, &Up);
		FOR(i,N) scanf("%lld", &Val[i]);
		ll Freq = -1;
		FORTO(f,Dw, Up) {
			bool ok = true;
			FOR(i,N) ok &= (Val[i]%f == 0 || f%Val[i] == 0);
			if (ok) { Freq = f; break; }
		}
		
		printf("Case #%d: ", t);
		if (Freq == -1)
			printf("NO\n");
		else
			printf("%lld\n", Freq);
	}
	return 0;
}

