#include <cstdio>
#include <cmath>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
using namespace std;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPI;
typedef string STR;
typedef vector<STR > VS;

#define FORE(C, I) for(VI::iterator I = C.begin();I!=C.end();++I)
#define REP(I, N) for(int I=0;I<(N);++I)
#define FOR(I, A, B) for(int I=A;I<=B;++I)
#define FORD(I, A, B) for(int I=(A); I>=(B);--I)
#define ALL(C) C.begin(), C.end()
#define FS first
#define SE second

const int MAXN = 60;

int Xs[MAXN], V[MAXN];
bool ok[MAXN];
int cok;
int ret=0,done=0;
int N,K,B,T;
int C;

int main()
{
	scanf("%d", &C);
	FOR(cas, 1, C)
	{
		scanf("%d%d%d%d", &N, &K, &B, &T);
		cok=ret=done=0;
		
		REP(i, N)
		{
			scanf("%d", Xs+i);
		}
		REP(i, N)
		{
			scanf("%d", V+i);
			ok[i] = ( ( (double) B-Xs[i] )/V[i]) <= T;
// 			printf("OK %d: %lf\n", i, ((double) B-Xs[i] )/V[i]);
			cok += ok[i];
		}
		
		if(cok<K)
		{
			printf("Case #%d: IMPOSSIBLE\n", cas);
		} else
		{
			FORD(i, N-1, 0)
			{
				if(done >= K) break;
				
				if(ok[i])
				{
					FOR(ii, i, N-1)
						ret += !ok[ii];
					++done;
				}
			}
			printf("Case #%d: %d\n", cas, ret);
		}
	}
	return 0;
}