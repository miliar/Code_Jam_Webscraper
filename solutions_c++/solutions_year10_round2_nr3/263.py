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
typedef long long int LL;

#define FORE(C, I) for(VI::iterator I = C.begin();I!=C.end();++I)
#define REP(I, N) for(int I=0;I<(N);++I)
#define FOR(I, A, B) for(int I=A;I<=B;++I)
#define FORD(I, A, B) for(int I=(A); I>=(B);--I)
#define ALL(C) C.begin(), C.end()
#define FS first
#define SE second

int T;
int n;
LL tmp;
int MOD=100003;
const int MAXN = 509;
int t[MAXN][MAXN];

int N[MAXN][MAXN];

int NT(int a, int b)
{
	if(a<=0 || a<b) return 0;
	if(a==b) return 1;
	else return N[a][b];
}

int dl(int a, int b)
{
	if(t[a][b] != -1) return t[a][b];
	if(b<=a) return 0;
	if( a == 0 || a==1 || a+1==b) return 1;
	
	LL tmp=0;
	t[a][b]=0;
	REP(i, a)
	{
		t[a][b] += ((long long) dl(a-i-1, a) * NT(b-a-1, i)) % MOD;
		t[a][b] %= MOD;
	}
// 	printf("dl(%d, %d) = %d\n", a, b, t[a][b]);
	return t[a][b];
}

void netGen()
{
	REP(n, MAXN)
	{
		N[n][0]=N[n][n]=1;
		REP(k, n-1)
			N[n][k+1] = (N[n-1][k] + N[n-1][k+1])%MOD;
	}

}
int main()
{
	netGen();
	REP(i, MAXN) REP(j, MAXN) t[i][j]=-1;
	scanf("%d", &T);
	FOR(przyp, 1, T)
	{
		scanf("%d", &n);
		LL odp = 0;
		FOR(i, 0, n-2) odp = (odp + dl(i, n-1)) % MOD;
		printf("Case #%d: %lld\n", przyp,  odp);
	}
}