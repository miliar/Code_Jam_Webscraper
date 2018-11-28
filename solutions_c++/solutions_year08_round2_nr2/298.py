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
#define REP(i,n) for(LL i=0;i<(n);++i)
#define FOR(i,a,b) for(LL i=(a);i<=(b);++i)
#define FORD(i,a,b) for(LL i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define CLR(v,a) memset(v,a,sizeof(v))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define MAX_N 1000100

LL t, n;
LL parent[MAX_N];
bool prime[MAX_N];
set<LL> g;

// grupy sa liczone od A
LL findG(LL a) {
	if (parent[a]==-1) return a;
	return parent[a]=findG(parent[a]);
}

void joinG(LL a, LL b) {
	a=findG(a),b=findG(b);
	if (a==b) return;
	if (rand()%2==0) parent[b]=a;
	else parent[a]=b;
}

int main()
{
	scanf("%lld",&t);
	FOR(T,1,t) {
		LL A,B,P; scanf("%lld%lld%lld",&A,&B,&P);
		n=B-A+1; FOR(i,A,B) parent[i-A]=-1;
		CLR(prime,1);
		FOR(i,2,n) if (prime[i]) {
			if (i>=P) {
				LL poz=A+(i-A%i)%i, last=-1;
				assert(poz%i==0);
				while (poz<=B) {
					if (last!=-1) joinG(last-A,poz-A);
					last=poz;
					poz+=i;
				}
			}
			for (LL j=i+i;j<=n;j+=i)
				prime[j]=false;
		}
		g.clear();
		FOR(i,A,B) g.insert(findG(i-A));
		printf("Case #%lld: %d\n", T, g.size());
	}
	return 0;
}
