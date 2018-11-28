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
const int maxn = 200;
char str[maxn];

int go(int id,i64 n,int d){
	if(id==-1){
		i64 q = (i64)sqrt(n);
//		eprintf("%lld^2==%lld==%lld\n",q,q*q,n);
		if(q*q==n) return 1;
		q++;
		if(q*q==n) return 1;
		q-=2;
		if(q*q==n) return 1;
		return 0;
	}
	if(str[id]=='1') return go(id-1,(1LL<<d)+n,d+1);
	if(str[id]=='0') return go(id-1,n,d+1);
	str[id]='1';
	if(go(id-1,n+(1LL<<d),d+1)) return 1;
	str[id]='0';
	if(go(id-1,n,d+1)) return 1;
	str[id]='?';
	return 0;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int id = 1 ; id <= T ; id++ ){
		scanf("%s",str);
		i64 res = -1;
		int n = strlen(str);
		//reverse(str,str+n);
		go(n-1,0,0);
		//reverse(str,str+n);
		res = 0;
	//	for(int i = n - 1 ; i >= 0 ; i-- ) res=2*res+(str[i]-'0');
	//	eprintf("%lld\n",res);
		printf("Case #%d: %s\n",id,str);
	}
	return 0;
}
