// Headers {{{
#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,j,k) for(int i=(j); i<=(k); ++i)
#define FORD(i,j,k) for(int i=(j); i>=(k); --i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ST first
#define ND second
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define SQR(a) ((a)*(a))
#define debug(x) cerr << #x << " = " << x << '\n'
template<typename Q> inline int size(Q a) { return a.size(); }
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<pair<int,int> > VPII;
typedef unsigned long long ULL;
typedef long long LL;
typedef pair<int,int> PII;
const int INF=1000000000;
// }}}

int FU[1000005];
int rank[1000005];
LL A,B,P;

int sito[1000005];
int primes[1000000],l;

vector<LL> fac[1000005];
LL liczba[1000005];
vector<LL> wieksze;

int FUfind(int x) {
	if(FU[x]==x) return x;
	FU[x]=FUfind(FU[x]);
	return FU[x];
}

void FUunion(int x,int y) {
	if(rank[x]==rank[y]) {
		FU[x]=y;
		++rank[y];
	} else if(rank[x]>rank[y]) FU[y]=x;
	else FU[x]=y;
}

int main() {
	FOR(i,2,1000000) if(!sito[i]) {
		primes[l++]=i;
		for(int j=2; j*i<=1000000; ++j) sito[j*i]=1;
	}
	int ntc;
	scanf("%d",&ntc);
	REP(tc,ntc) {
		scanf("%lld%lld%lld",&A,&B,&P);
		REP(i,int(B-A+1)) {
			FU[i]=i;
			rank[i]=0;
			fac[i].clear();
		}
		wieksze.clear();
		for(LL i=A; i<=B; ++i) liczba[i-A]=i;
		REP(i,l) {
			LL p=primes[i];
			LL start=(A+p-1)/p;
			start*=p;
			for(;start<=B;start+=p) {
				while(liczba[start-A]%p==0) {
					liczba[start-A]/=p;
				}
				fac[start-A].push_back(p);
			}
		}
		for(LL i=A; i<=B; ++i) if(liczba[i-A]>1) fac[i-A].push_back(liczba[i]);
		for(LL i=A; i<=B; ++i) REP(j,size(fac[i-A])) if(fac[i-A][j]>=P) wieksze.push_back(fac[i-A][j]);
		sort(ALL(wieksze));
		unique(ALL(wieksze));
		REP(i,size(wieksze)) {
			LL p=wieksze[i];
		//	printf("robie liczbe %lld\n",p);
			LL start=(A+p-1)/p;
			start*=p;
			start+=p;
			for(;start<=B;start+=p) FUunion(FUfind(start-A),FUfind(start-p-A));
		}
		int res=0;
		REP(i,int(B-A+1)) {
		//	printf("i=%d res=%d\n",i,res);
			res+=(FU[i]==i);
		}
		printf("Case #%d: %d\n",tc+1,res);
	}
	return 0;
}
