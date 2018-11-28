#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <complex>
#include <stack>
#include <memory.h>
#ifdef NEV_DEBUG
#include <ctime>
#endif
using namespace std;

const int SIZE = 32;
const double pi = 3.1415926535897932384626433832795;


typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int uint;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef LL matrix[SIZE][SIZE];

#define sz size()
#define mp mAAke_pAAir
#define pb push_back
#define ALL(AA) (AA).begin(), (AA).end()
#define FOR(i,AA,b) for(int i=(AA),_b(b); i<_b; ++i)
#define RFOR(i,AA,b) for(int i=(AA)-1,_b(b); i>=_b; --i)
#define CLR(AA,b) memset(AA,b,sizeof(AA))
#define CPY(AA,b) memcpy(AA,b,sizeof(AA))
#define sqr(AA) ((AA)*(AA))
#define MIN(AA,b) ((AA)<(b)?(AA):(b))

char ch[1<<20];
string gs() {scanf("%s",ch); return string(ch);}
string gl() {gets(ch); return string(ch);}
template <class T>
T gcd(T a, T b) { return (!a)?b:gcd(b%a,a); }
void error(){ int yyy=0; cout << 7/yyy; }

int AA[512][512];
char CCC[1024];

int X,Y,D;

int S[512][512];
int SL[512][512];
int SR[512][512];
int SU[512][512];
int SD[512][512];

inline int sum(int x1, int x2, int y1, int y2) {
	return S[x2][y2]
		-((x1)?S[x1-1][y2]:0)
		-((y1)?S[x2][y1-1]:0)
		+((x1 && y1)?S[x1-1][y1-1]:0);
}

inline int sumL(int x1, int x2, int y1, int y2) {
	return SL[x2][y2]
		-((x1)?SL[x1-1][y2]:0)
		-((y1)?SL[x2][y1-1]:0)
		+((x1 && y1)?SL[x1-1][y1-1]:0)
		
		- sum(x1,x2,y1,y2)*(512-y2-1);
}
inline int sumR(int x1, int x2, int y1, int y2) {
	return SR[x2][y2]
		-((x1)?SR[x1-1][y2]:0)
		-((y1)?SR[x2][y1-1]:0)
		+((x1 && y1)?SR[x1-1][y1-1]:0)
		
		- sum(x1,x2,y1,y2)*y1;
}

inline int sumU(int x1, int x2, int y1, int y2) {
	return SU[x2][y2]
		-((x1)?SU[x1-1][y2]:0)
		-((y1)?SU[x2][y1-1]:0)
		+((x1 && y1)?SU[x1-1][y1-1]:0)
		
		- sum(x1,x2,y1,y2)*(512-x2-1);
}

inline int sumD(int x1, int x2, int y1, int y2) {
	return SD[x2][y2]
		-((x1)?SD[x1-1][y2]:0)
		-((y1)?SD[x2][y1-1]:0)
		+((x1 && y1)?SD[x1-1][y1-1]:0)
		
		- sum(x1,x2,y1,y2)*x1;
}

int brut(int x1, int y1, int K) {
	double x0=1.0*(x1+x1+K-1)/2.0;
	double y0=1.0*(y1+y1+K-1)/2.0;
	double rx=0.0;
	double ry=0.0;
	FOR(x,x1,x1+K)FOR(y,y1,y1+K){
		if ((x==x1 || x==x1+K-1) && (y==y1 || y==y1+K-1)) continue;
		rx+=(1.0*x-x0)*AA[x][y];
		ry+=(1.0*y-y0)*AA[x][y];
	}
	return (abs(rx)<1e-9 && abs(ry)<1e-9);
}

void solve() {
	scanf("%d%d%d",&X,&Y,&D);
	FOR(i,0,X) {
		scanf("%s",CCC);
		FOR(j,0,Y) {
			AA[i][j]=(CCC[j]-'0');
		}
	}
	CLR(S,0);
	FOR(i,0,X) FOR(j,0,Y) {
		S[i][j]=AA[i][j];
		if (i) S[i][j]+=S[i-1][j];
		if (j) S[i][j]+=S[i][j-1];
		if (i && j) S[i][j]-=S[i-1][j-1];

		SL[i][j]=AA[i][j]*(512-j);
		if (i) SL[i][j]+=SL[i-1][j];
		if (j) SL[i][j]+=SL[i][j-1];
		if (i && j) SL[i][j]-=SL[i-1][j-1];

		SR[i][j]=AA[i][j]*(j+1);
		if (i) SR[i][j]+=SR[i-1][j];
		if (j) SR[i][j]+=SR[i][j-1];
		if (i && j) SR[i][j]-=SR[i-1][j-1];

		SU[i][j]=AA[i][j]*(512-i);
		if (i) SU[i][j]+=SU[i-1][j];
		if (j) SU[i][j]+=SU[i][j-1];
		if (i && j) SU[i][j]-=SU[i-1][j-1];

		SD[i][j]=AA[i][j]*(i+1);
		if (i) SD[i][j]+=SD[i-1][j];
		if (j) SD[i][j]+=SD[i][j-1];
		if (i && j) SD[i][j]-=SD[i-1][j-1];
	}

	RFOR(K,min(X,Y)+1,3) {
		FOR(x,0,X-K+1) FOR(y,0,Y-K+1) {
			/*
			int k=(K-1)>>1;
			int xl=x+k;
			int xr=x+K-1-k;
			int yl=y+k;
			int yr=y+K-1-k;

			int s1=sumL(x,x+K-1,y,yl) - (k+1)*(AA[x][y]+AA[x+K-1][y]);
			int s2=sumR(x,x+K-1,yr,y+K-1) - (k+1)*(AA[x][y+K-1]+AA[x+K-1][y+K-1]);
			
			if (s1!=s2) continue;
			s1=sumU(x,xl,y,y+K-1) - (k+1)*(AA[x][y]+AA[x][y+K-1]);
			s2=sumD(xr,x+K-1,y,y+K-1) - (k+1)*(AA[x+K-1][y]+AA[x+K-1][y+K-1]);
			if (s1!=s2) continue;
			*/
			if (!brut(x,y,K)) continue;

			printf("%d\n",K);
			return ;
		}
	}
	printf("IMPOSSIBLE\n");
}

int main() {
#ifdef NEV_DEBUG
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    clock_t beg = clock();
#else
    //freopen("union.in","r",stdin);
    //freopen("union.out","w",stdout);
#endif

	int tests; scanf("%d",&tests); 
	for(int tn=1; tn<=tests; ++tn){
		fprintf(stderr, "Case #%d ... ",tn);
		printf("Case #%d: ",tn);
		solve();
		fprintf(stderr, "Done\n");
	}

#ifdef NEV_DEBUG
    fprintf(stderr,"*** Total time: %.3lf ***\n",1.0*(clock()-beg)/CLOCKS_PER_SEC);
#endif
    return 0;
}