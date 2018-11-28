#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <cctype>
#include <iostream>
#include <cassert>
#include <numeric>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;

#define ALL(a) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define CLR(v,a) memset(v,a,sizeof(v))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

vector< pair<int,int> > tab;

void read_in() {
	tab.clear();
	int n;LL A,B,C,D,M,X,Y;
	scanf("%d%lld%lld%lld%lld%lld%lld%lld",&n,&A,&B,&C,&D,&X,&Y,&M);
	REP(i,n) {
		tab.PB(MP((int)X,(int)Y));
		X=(A*X+B)%M;
		Y=(C*Y+D)%M;
	}
}

int main()
{
	int t;
	scanf("%d",&t);
	FOR(T,1,t) {
		read_in();
		//REP(i,tab.size()) printf("%d %d\n", tab[i].FI, tab[i].SE); printf("\n");
		//tab.clear(); tab.PB(MP(1,1)); tab.PB(MP(1,4)); tab.PB(MP(4,4));
		LL ile[3][3]={},res=0;
		REP(i,tab.size()) ile[tab[i].FI%3][tab[i].SE%3]++;
		FOR(x0,0,2) FOR(y0,0,2)
			FOR(x1,0,2) FOR(y1,0,2)
				FOR(x2,0,2) FOR(y2,0,2)
					if (x0*3+y0<=x1*3+y1&&x1*3+y1<=x2*3+y2&&(x0+x1+x2)%3==0&&(y0+y1+y2)%3==0) {
						LL a=ile[x0][y0],b=ile[x1][y1],c=ile[x2][y2];
						if (x0==x1&&y0==y1&&x0==x2&&y0==y2) {
							res += a*(a-1)*(a-2)/6LL;
						} else if (x0==x1&&y0==y1) {
							res += a*(a-1)/2LL*c;
						} else if (x1==x2&&y1==y2) {
							res += a*b*(b-1)/2LL;
						} else if (x0==x2&&y0==y2) {
							res += a*(a-1)/2LL*b;
						} else 
							res += a*b*c;
					}
		printf("Case #%d: %lld\n", T, res);
	}
	return 0;
}
