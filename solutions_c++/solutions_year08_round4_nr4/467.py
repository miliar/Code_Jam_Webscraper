// solution by Peter Ondruska

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstring>

#include <iostream>
#include <iomanip>
#include <sstream>
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
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long int ll;
typedef long double ld;
typedef pair<ld,ld> PDD;
typedef pair<ll,ll> PLL;

#define FOR(i,n)      for(int i=0;i<n;i++)
#define FORTO(i,a,b)  for(int i=a;i<=b;i++)
#define FORD(i,n)     for(int i=n-1;i>=0;i--)
#define FORDTO(i,a,b) for(int i=b;i>=a;i--)
#define FOREACH(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)

#define DEBUG(x) cout<<'>'<<#x<<':'<<x<<endl
#define $ size()
#define ALL(x) (x).begin(),(x).end()
#define PB push_back

#define MAX 10047

int Compress(char *S) {
	int Len = strlen(S);
	int NewLen = 0;
	FOR(i,Len)
		if (i && S[i-1] != S[i]) 
			NewLen++;
	return NewLen+1;
}

int main() {
	int C;
	scanf("%d", &C);
	FORTO(c,1,C) {
		int K, P[5];
		char S[1024];
		scanf("%d %s", &K, S);
		int Len = strlen(S);
		FOR(i,K) P[i] = i;
		int Min = INT_MAX;
		do {
			char X[1024];
			FOR(i,Len/K)
				FOR(j,K)
					X[i*K+j] = S[i*K+P[j]];
			X[Len] = 0;
			Min = min(Min,Compress(X));
		} while (next_permutation(P,P+K));
		printf("Case #%d: %d\n", c, Min);
	}
	return 0;
}
