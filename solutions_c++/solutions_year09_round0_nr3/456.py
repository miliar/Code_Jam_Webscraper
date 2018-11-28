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

#define MAXL 567
#define MOD 10000

char S[20] = "welcome to code jam";
char W[MAXL];

int N, L, T[20];

int main() {
	scanf("%d\n", &N);
	FOR(k,N) {
		L = strlen(gets(W));
		FOR(i,20) T[i] = 0;
		T[0] = 1;
		FOR(i,L) FORD(j,19)
			if (W[i] == S[j])
				T[j+1] = (T[j+1] + T[j]) % MOD;
		printf("Case #%d: %04d\n", k+1, T[19]);
	}
	return 0;
}
