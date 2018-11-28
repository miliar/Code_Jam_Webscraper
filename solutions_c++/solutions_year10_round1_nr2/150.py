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

#define MAXN 123
#define INF 1000000
int T[MAXN][256];

int main() {
	int C;
	scanf("%d", &C);
	FORTO(t,1,C) {
		int D, I, M, N, A;
		scanf("%d %d %d %d", &D, &I, &M, &N);
		FORTO(k,1,N) {
			scanf("%d", &A);
			
			// zahodim
			FOR(i,256) T[k][i] = T[k-1][i]+D;
			
			FOR(i,256) {
				// insertnem to ako i
				FOR(j,256) if (abs(i-j) <= M) {
					T[k][i] = min(T[k][i],T[k-1][j]+abs(A-i));
				}
			}
			
			int B[256]; FOR(i,256) B[i] = T[k][i];
			
			FOR(i,256) {
				// nieco insertnem za to az na i
				FOR(j,256) if (M != 0) {
					int diff = (abs(i-j)+M-1)/M;
					T[k][i] = min(T[k][i], B[j]+I*diff);
				}
			}
		}
		
		int Min = INF;
		FOR(i,256)
			Min = min(Min,T[N][i]);
		printf("Case #%d: %d\n", t, Min);
	}
	return 0;
}
