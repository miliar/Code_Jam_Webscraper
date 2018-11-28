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

#define MAXD 5678
#define MAXL 20

int L, D, N;
// words
char W[MAXD][MAXL];
// sample
char S[10000];
// pattern
bool P[MAXL][26];

int main() {
	scanf("%d %d %d", &L, &D, &N);
	FOR(i,D) scanf("%s", W[i]);
	FOR(k,N) {
		scanf("%s", S);
		int Len = strlen(S);
		bool open = false;
		int j = 0;
		FOR(i,L) FOR(j,26) P[i][j] = false;
		FOR(i,Len) {
			if (isalpha(S[i]))
				P[j][S[i]-'a'] = true;
			else if (S[i] == '(')
				open = true;
			else if (S[i] == ')')
				open = false;
			if (!open) j++;
		}
		int Match = 0;
		FOR(i,D) {
			bool ok = true;
			FOR(j,L) ok &= P[j][W[i][j]-'a'];
			if (ok) Match++;
		}
		printf("Case #%d: %d\n", k+1, Match);
	}
	return 0;
}
