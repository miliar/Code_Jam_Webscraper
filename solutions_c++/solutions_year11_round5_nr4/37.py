#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

#define REP(AA,BB) for(int AA=0; AA<(BB); ++AA)
#define FOR(AA,BB,CC) for(int AA=(BB); AA<(CC); ++AA)
#define FC(AA,BB) for(__typeof((AA).begin()) BB=(AA).begin(); BB!=(AA).end(); ++BB)
#define SZ(AA) ((int)((AA).size()))
#define ALL(AA) (AA).begin(), (AA).end()
#define PB push_back
#define MP make_pair

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LL;
typedef long double LD;

char buf[210];

int main(void) {
	int T; scanf("%d", &T);
	FOR(t,1,T+1) {
		scanf("%s", buf); int n=strlen(buf);
		VI gdzie; LL X=0;
		REP(i,n) {
			X<<=1;
			if(buf[i]=='1')
				++X;
			else if(buf[i]=='?')
				gdzie.PB(n-i-1);
		}
		int m=SZ(gdzie); LL res=-1;
		REP(i,(1<<m)) {
			LL tmp=X;
			REP(j,m) {
				if(i&(1<<j))
					tmp|=(1LL<<gdzie[j]);
			}
			LL s=sqrt(0.0+tmp);
			if(s*s==tmp) {
				res=tmp;
				break;
			}
		}
		buf[n]=0;
		for(int i=n-1, j=0; i>=0; --i, ++j)
			buf[j]=(res&(1LL<<i))?'1':'0';
		printf("Case #%d: %s\n", t, buf);
	}
	return 0;
}
				
