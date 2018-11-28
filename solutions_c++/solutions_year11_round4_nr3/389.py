#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

const int N = 1000010;
int prime[N];
bool pr[N];
LL n;
int ind;

int ileq(LL p, LL duz){
	LL x = p;
	LL odp = 0;
	p = p*p;
	while(p <= duz){
		odp++;
		p *= x;
	}
	return odp;
}

void sito(){
	ind =0 ;
	FOR(i,2,N-1)
		pr[i] = true;
	for(int i = 2;i*i < N;i++)
		if(pr[i]){
			for(int j = i*i ; j<N;j+=i)
				pr[j] = false;
		}
	REP(i,N)
		if(pr[i]){
			prime[ind++] = i;
		}
}

main(){
	sito();
	int t;
	scanf("%d",&t);
	FOR(q,1,t){
		scanf("%lld",&n);
		int wyn = 0;
		if(n == 1) wyn = 0;
		else if(n==2) wyn = 1;
		else{
			wyn = 1;
			for(int i=0;(LL)prime[i]*prime[i] <= n; i++){
				wyn += ileq(prime[i], n);
			}
		}
		printf("Case #%d: %d\n",q,wyn);
	}
	return 0;
}
