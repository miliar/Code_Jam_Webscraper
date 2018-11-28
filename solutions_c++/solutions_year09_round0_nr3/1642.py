#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
#include <memory.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef double dd;
typedef long double ld;
typedef vector <int > VI;
typedef vector < VI > VVI;
typedef vector < ll > VLL;
typedef vector < dd > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define VAR(V,init) __typeof(init) V=(init)
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define FOREACH(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define ALL(X) (X).begin(),(X).end()
#define CLE(a,b) memset(a,b,sizeof(a))
#define MINN(a,b) ((a)>(b)?(b):(a))
#define MAXX(a,b) ((a)<(b)?(b):(a))
#define PB push_back
#define PF push_front
#define CB pop_back
#define CF pop_front
#define MP make_pair
#define FI first
#define SE second
#define SZ(X) ((int)(X.size()))
#define INF 1000000000
#define INFLL 1000000000000000000ll
int COND = 100;
#define DB(x) ({if(COND){COND--; cerr << __LINE__ << " : " << #x << ": " << x << endl; };})
#define deb(A) //A
//////////////////

#define MAX_L 1000

const int lenp = 19; 
string pat = "welcome to code jam";

int n, t, lent, d[MAX_L + 1][lenp + 1], p = 10000;
char text[MAX_L];

int main()
{
	scanf("%d\n", &t);
	REP(i, t) {
		gets(text);
		lent = strlen(text);
		REP(x, lent + 1)
			REP(y, lenp + 1)
				d[x][y] = 0;
		d[0][0] = 1;
		FOR(x, 1, lent) {
			d[x][0] = d[x - 1][0] % p;
			FOR(y, 1, lenp) {
				d[x][y] = d[x - 1][y];
				if(text[x - 1] == pat[y - 1])
					d[x][y] += d[x - 1][y - 1];
				if(d[x][y] >= p)
					d[x][y] %= p;
			}
		}
		printf("Case #%d: %0*d\n", i + 1, 4, d[lent][lenp] % p);
	}
	return 0;
}
