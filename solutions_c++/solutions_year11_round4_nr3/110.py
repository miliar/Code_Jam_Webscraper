#include <algorithm>
#include <cstdlib>
#include <cstdarg>
#include <cassert>
#include <cstring>
#include <complex>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>

using namespace std;

typedef long long i64;
typedef long double d64;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()

#define pb push_back
#define mp make_pair

#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}

#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )

#ifdef WIN32
#define INT64 "%I64d"
#else
#define INT64 "%lld"
#endif
const int maxn = 2*1000*1000;
//int p[123];
i64 prime[maxn];
int er[maxn];
int main(){
	/*
	int n;
	scanf("%d",&n);
	forn(i,n) p[i] = i+1;
	int mincost = 1e9;
	int maxcost = -1;
	do{
		forn(i,n) printf("%d%c",p[i],"  "[i+1==n]);
		int res = 1;
		forn(i,n){
			while(1){
				int ok = 1;
				forn(j,i+1) ok&=(res%p[j])==0;
				if(ok) break;
				res++;
			}
		}
		printf("%d\n",res);
		mincost = min(res,mincost);
		maxcost = max(res,maxcost);
	}while(next_permutation(p,p+n));
	printf("%d %d %d\n",maxcost,mincost,maxcost-mincost);
	*/
	int T;
	memset(er,0,sizeof er);
	for(i64 i = 2 ; i < maxn ; i++ ){
		if(!er[i]){
			i64 j = i*i;
			while(j<maxn) er[j]=1,j+=i;
		}
	}
	int sizepr = 0;
	for(int i = 2 ; i < maxn ; i++ ) if(!er[i]) prime[sizepr++] = i;
	//for(int i = 0 ; i < sizepr ; i++ ) eprintf("%lld%c",prime[i]," \n"[i+1==100]);
	scanf("%d",&T);
	for(int tid = 1 ; tid <= T ; tid++ ){
		i64 n; scanf("%lld",&n);
		i64 res = 1;
		if(n!=1){
			for(int i = 0 ; i < sizepr ; i++ ){
				if(prime[i]*prime[i]>n) break;
				int k = 0;
				i64 p = prime[i];
				while(prime[i]*p<=n){
					k++;
					p*=prime[i];
				}
				res+=k;
			}
		}else{
			res = 0;
		}
		printf("Case #%d: %lld\n",tid,res);
	}
	return 0;
}
