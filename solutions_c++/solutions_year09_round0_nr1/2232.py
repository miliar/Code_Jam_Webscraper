#include<algorithm>
#include<cstring>
#include<cstdio>
#include<vector>
#include<set>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define FOR(x,y,z) for(int x=y;x<=z;++x)
#define FORD(x,y,z) for(int x=y;x>=z;--x)
#define FOReach(x,Z) for(__typeof(Z.begin()) x=Z.begin();x!=Z.end();++x)
#define REP(x,y) for(int x=0;x<y;++x)

#define PB push_back
#define ALL(X) X.begin(),X.end()

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
#define debug(fmt, ...) printf(fmt, ## __VA_ARGS__ )
#else
#define debug(fmt, ...)
#endif


const int MAX = 5000;
const int MAXL = 15;
const int INF = 1000000001;

char W[MAX][MAXL+1];
char T[10000];

bool K[MAXL][26];

int l, d, n;

main() {
	scanf("%d %d %d", &l, &d, &n);
	REP(i,d)
		scanf("%s", W[i]);
	FOR(i,1,n)
	{
		REP(j,l)
			REP(k,26)
				K[j][k] = false;
		scanf("%s", T);
		int len = strlen(T);
		int w = 0;
		for(int j=0,poz=0;j<len;++poz)
		{
			if(T[j] == '(') {
				++j;
				while(T[j] != ')')
				{
					K[poz][T[j]-'a'] = true;
					++j;
				}
				++j;
			}
			else {
				K[poz][T[j]-'a'] = true;
				++j;
			}
		}
		
		REP(j,d)
		{
			bool czy = true;
			REP(k,l)
			{
				if(!K[k][W[j][k]-'a']) {
					czy = false;
					break;
				}
			}
			w += czy;
		}
		printf("Case #%d: %d\n", i, w);
	}
	return 0;
}

