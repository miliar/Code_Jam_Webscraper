/* autor: Marek Rogala */
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define SIZE(x) ((int)x.size())
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

int const MAXN=1010;

int n,r;
LL k;
int tab[MAXN];


LL zrob(){
	scanf("%d%lld%d",&r,&k,&n);
	LL sum=0;
	REP(i,n){	scanf("%d",tab+i); sum+=tab[i];}
	if(sum<=k) return sum*r;
	
	int a=0,b=-1;
	
	LL wyn=0;
	
	FOR(i,1,r){
	
		sum=0;
		while(sum+tab[(b+1)%n]<=k){
			b++;
			b%=n;
			sum+=tab[b];
		}
		
		if(sum == 0){
			//juz sie nie posuniemy
			return wyn;
		}
		
		wyn += sum;
		
	}
	return wyn;
}

int main() {
	int t;
	scanf("%d", &t);
	REP(i,t) cout<<"Case #"<<1+i<<": "<<zrob()<<endl;
	
	return 0;
}

