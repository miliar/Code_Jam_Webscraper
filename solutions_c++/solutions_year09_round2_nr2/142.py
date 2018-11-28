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
#define CLEAR(x) memset(x,0,sizeof(x))




int main() {
	int T;
	scanf("%d\n", &T);
	FORTO(k,1,T) {
		char N[50];
		CLEAR(N);
		scanf("%s", N);
		int L = strlen(N);
		bool ok = false;
		FOR(i,L-1) if (N[i] < N[i+1]) ok = true;
		if (!ok) {
			FORD(i,L) N[i+1] = N[i];
			N[0] = '0';
			L++;
		}
		next_permutation(N,N+L);
		printf("Case #%d: %s\n", k, N);
	}
	return 0;
}
