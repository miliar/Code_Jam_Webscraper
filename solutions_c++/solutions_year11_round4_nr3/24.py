#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
#include <cassert>
using namespace std;  

#define PB push_back  
#define MP make_pair  
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
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<VPII> VVPII;

VI primes;

void run(int casenr) {
	ll n; cin>>n;
	int ret=0;
	if(n>=2) ++ret;
	REPSZ(i,primes) {
		ll at=primes[i]; int p=1;
		while(at<=n/primes[i]) at*=primes[i],++p;
		ret+=p-1;
	}
	printf("Case #%d: %d\n",casenr,ret);
}

void precalc() {
	const int MAX=1000000;
	VI isprime(MAX,1); isprime[0]=isprime[1]=0;
	REPE(i,MAX) if(isprime[i]) { primes.PB(i); for(int j=i+i;j<=MAX;j+=i) isprime[j]=false; }
	assert((ll)MAX*MAX>=1000000000000LL);
}

int main() {
	precalc();
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
	return 0;
}

 
