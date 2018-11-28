#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;

#define PB push_back
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<ll> VLL;

const int MAX=1000010;
VLL primes;

map<ll,int> prime2ind;
int n;
VI parent,rank;

ll a,b,p;

int get(int a) { if(parent[a]==a) return a; return parent[a]=get(parent[a]); }

void unite(int a,int b) {
//	printf("unite %lld and %lld\n",::a+a,::a+b);
	a=get(a),b=get(b);
	if(a==b) return;
	if(rank[a]>=rank[b]) parent[b]=a; else parent[a]=b;
	if(rank[a]==rank[b]) ++rank[a];
}

void update(int nr,ll prime) {
//	printf("updating %lld %lld\n",a+nr,prime);
	int ind;
	if(prime2ind.count(prime)) {
		ind=prime2ind[prime];
	} else {
		prime2ind[prime]=n;
		parent.PB(n); rank.PB(0);
		ind=n++;
	}
	unite(nr,ind);
}

void run(int casenr) {
	scanf("%lld%lld%lld",&a,&b,&p);
	prime2ind.clear(); n=b-a+1;
	parent=VI(n); rank=VI(n,0); REP(i,n) parent[i]=i;
	
	assert(primes.back()>n);
	REPSZ(i,primes) if(primes[i]>=p) {
		ll first=(a+primes[i]-1)/primes[i]*primes[i];
		for(ll second=first+primes[i];second<=b;second+=primes[i]) unite(first-a,second-a);
	}
/*	for(ll x=a;x<=b;++x) {
		ll y=x;
		REPSZ(i,primes) {
			if(primes[i]*primes[i]>y) break;
			if(y%primes[i]==0) {
				if(primes[i]>=p) update(x-a,primes[i]);
				do { y/=primes[i]; } while(y%primes[i]==0);
			}
		}
		if(y>=p) update(x-a,y);
	} */
	int ret=0; REP(i,n) if(parent[i]==i) ++ret;
	printf("Case #%d: %d\n",casenr,ret);
}

void precalc() {
	vector<bool> isprime(MAX+1,1); isprime[0]=isprime[1]=0;
	FORE(i,2,MAX) if(isprime[i]) { primes.PB(i); for(int j=i+i;j<=MAX;j+=i) isprime[j]=0; }
}

int main() {
	precalc();
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
}
