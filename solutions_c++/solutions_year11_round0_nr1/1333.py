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

// g[100][100][100]
const int maxn = 101*101*101;
const int maxm = 200;
const i64 inf  = 1LL<<50;

i64 g[maxn];
int butt[maxm];
int robo[maxm];

int check(int pos){
	return 0<=pos&&pos<100;
}
int code(int act,int first,int second){
	return (act*101+first)*100+second;
}
void rcode(int code,int &act,int &first,int &second){
	second = code%100;
	code/=100;
	first = code%101;
	code /= 101;
	act = code;
}
void solve(int caseID){
	forn(i,maxn) g[i] = inf;
	int n;
	assert(scanf("%d",&n)==1);
	forn(i,n){
		char str[10];
		int but;
		assert(scanf("%s%d",str,&but)==2);
		robo[i] = str[0]=='O';
		butt[i] = but-1;
	}
	g[code(0,0,0)]=0;
	queue<int> pq;
	pq.push(code(0,0,0));
	while(!pq.empty()){
		int pf,ps,cc;
		int npf,nps,ncc;
		int tmp = pq.front();
		pq.pop();
		rcode(tmp,cc,pf,ps);
//		eprintf("(%d,%d,%d)\n",cc,pf,ps);
		if(cc==n) continue;
		for( int df = -1 ; df <= 1 ; df++ ){
			for(int ds = -1 ; ds <= 1 ; ds++ ){
				if(check(pf+df)&&check(ps+ds)){
					ncc = cc;
					npf = pf + df;
					nps = ps + ds;
					int temp;
					if(npf==pf&&butt[cc]==npf&&robo[cc]) ncc++;
					if(nps==ps&&butt[cc]==nps&&!robo[cc]) ncc++;
					if(g[temp=code(ncc,npf,nps)]>g[tmp]+1){
						g[temp]=g[tmp]+1;
						pq.push(temp);
					}
				}
			}
		}
	}
	i64 res = inf;
	forn(i,maxm)
		forn(j,maxm) res = min(res,g[code(n,i,j)]);
	printf("Case #%d: %lld\n",caseID,res);
}

int main(){
	int T;
	assert(scanf("%d",&T)==1);
	forn(i,T) solve(i+1);
	return 0;
}
