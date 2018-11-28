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
const int maxn = 512;
char board[maxn][maxn];

pair<i64,i64> dpC[maxn][maxn],dpR[maxn][maxn];

i64 D;
pair<i64,i64> getC(int c,int r){
	if(c<0||r<0) return mp(0LL,0LL);
	if(dpC[c][r].first!=-1) return dpC[c][r];
	dpC[c][r] = mp(0LL,0LL);
	pair<i64,i64> pa,pb,pc;
	pa = getC(c,r-1);
	pb = getC(c-1,r);
	pc = getC(c-1,r-1);
	dpC[c][r].first=  pa.first + pb.first - pc.first + (D+board[c][r]-'0')*c;
	dpC[c][r].second= pa.second + pb.second - pc.second + D+board[c][r]-'0';
	return dpC[c][r];
}

pair<i64,i64> getR(int c,int r){
	if(c<0||r<0) return mp(0LL,0LL);
	if(dpR[c][r].first!=-1) return dpR[c][r];
	dpR[c][r] = mp(0LL,0LL);
	pair<i64,i64> pa,pb,pc;
	pa = getR(c,r-1);
	pb = getR(c-1,r);
	pc = getR(c-1,r-1);
	dpR[c][r].first=  pa.first + pb.first - pc.first + (D+board[c][r]-'0')*r;
	dpR[c][r].second= pa.second + pb.second - pc.second + D + board[c][r]-'0';
	return dpR[c][r];
}

pair<i64,i64> goodC(int cb,int rb,int ce,int re){
	pair<i64,i64> a,b,c,d;
	a = getC(cb-1,rb-1);
	b = getC(cb-1,re);
	c = getC(ce,rb-1);
	d = getC(ce,re);
	a.first = a.first - b.first - c.first + d.first;
	a.second = a.second - b.second - c.second + d.second;
	return a;
}

pair<i64,i64> goodR(int cb,int rb,int ce,int re){
	pair<i64,i64> a,b,c,d;
	a = getR(cb-1,rb-1);
	b = getR(cb-1,re);
	c = getR(ce,rb-1);
	d = getR(ce,re);
	a.first = a.first - b.first - c.first + d.first;
	a.second = a.second - b.second - c.second + d.second;
	return a;
}

int R,C;
int main(){
	int T;
	scanf("%d",&T);
	for(int tid = 1 ; tid <= T ; tid++ ){
		scanf("%d%d%lld",&R,&C,&D);
		forn(i,R) scanf("%s",board[i]);
		forn(i,R) forn(j,C) dpC[i][j] = dpR[i][j] = mp(-1LL,-1LL);
		//getC(R-1,C-1);
		//getR(R-1,C-1);
		int res = 0;
		forn(i,R){
			forn(j,C){
				for(int k = 3 ; i + k <= R && j + k <= C; k++ ){
					int ok = 0;
					i64 cz = i  + i + k - 1;
					i64 rz = j  + j + k - 1;
					pair<i64,i64> a,b,c;
					a = goodC(i+1,j,i+k-2,j+k-1);
					b = goodC(i,j+1,i,j+k-2);
					c = goodC(i+k-1,j+1,i+k-1,j+k-2);
					a.first = a.first + b.first + c.first;
					a.second = a.second + b.second + c.second;
					if(cz*a.second==2LL*(a.first)) ok++;
					a = goodR(i+1,j,i+k-2,j+k-1);
					b = goodR(i,j+1,i,j+k-2);
					c = goodR(i+k-1,j+1,i+k-1,j+k-2);
					a.first = a.first + b.first + c.first;
					a.second = a.second + b.second + c.second;
					if(rz*a.second==2LL*(a.first)) ok++;
					if(ok==2) res = max(res,k);
				}
			}
		}
		eprintf("%d\n",tid);
		printf("Case #%d: ",tid);
		if(res==0){
			printf("IMPOSSIBLE\n");
		}else{
			printf("%d\n",res);
		}
	}
	return 0;
}
