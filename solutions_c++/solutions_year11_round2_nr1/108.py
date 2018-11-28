#include<algorithm>
#include<cstring>
#include<cstdio>
#include<vector>
#include<queue>
#include<set>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define FOR(x,y,z) for(int x=y;x<=z;++x)
#define FORD(x,y,z) for(int x=y;x>=z;--x)
#define FOReach(x,Z) for(__typeof((Z).begin()) x=(Z).begin();x!=(Z).end();++x)
#define REP(x,y) for(int x=0;x<y;++x)

#define PB push_back
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) ((int)(X).size())
#define CLR(X,x) memset(X, x, sizeof(X))

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
#define debug printf
#else
#define debug(fmt, ...)
#endif


const int MAX = 100;
const int INF = 1000000001;

char A[MAX][MAX+1];

int w[MAX];
int total[MAX];

double ow[MAX];
int ototal[MAX];

double oow[MAX];
int oototal[MAX];

double W[MAX];
double OW[MAX];
double OOW[MAX];

int n;

void skmin() {
	REP(i,n)
		w[i] = 0,
		total[i] = 0,
		ow[i] = 0.0,
		ototal[i] = 0,
		W[i] = 0.0,
		OW[i] = 0.0,
		OOW[i] = 0.0,
		oototal[i] = 0,
		oow[i] = 0.0;
	REP(i,n)
	{
		REP(j,n)
		{
			total[i] += A[i][j] != '.';
			w[i] += A[i][j] == '1';
		}
		W[i] = (double)w[i]/total[i];
	}
	REP(i,n)
	{
		REP(j,n) if(A[j][i] != '.')
		{
			ototal[i]++;
			ow[i] += (A[j][i] == '0' ? (double)w[j]/(total[j]-1) : (double)(w[j]-1)/(total[j]-1));
		}
		OW[i] = ow[i]/ototal[i];
	}
	REP(i,n)
	{
		REP(j,n) if(A[j][i] != '.')
		{
			oototal[i]++;
			oow[i] += OW[j];
		}
		OOW[i] = oow[i]/oototal[i];
	}
}

main() {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d:\n", z);
		scanf("%d", &n);
		REP(i,n)
			scanf("%s", A[i]);
		skmin();
		REP(i,n)
			printf("%.8lf\n", 0.25*W[i] + 0.5*OW[i] + 0.25*OOW[i]);
	}
	return 0;
}

