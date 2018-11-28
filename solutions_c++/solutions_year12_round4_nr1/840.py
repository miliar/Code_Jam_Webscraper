#pragma warning(disable : 4996)
#include <cstdio>
#include <cmath>
#include <ctime>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <string>
using namespace std;
typedef std::vector<int> vi;
typedef std::vector<vi> vvi;
typedef std::pair<int,int> ii;
typedef std::vector<ii> vii;
typedef std::vector<string> vs;
typedef std::vector<double> vd;

#define sz(a) int(a.size())
#define REP(i,n) for(int i = 0; i < n; ++i)
#define FOR(i,a) for(int i = 0; i < sz(a); ++i)

inline bool isdig(int a){return unsigned(a-'0') < 10;}
template<class T> static inline T getnum(){
   unsigned i; T j;
   do i = getchar(); while(!isdig(i));
   j = i-'0';  i=getchar() ;
   while(isdig(i)){ j = (j<<1)+(j<<3)+(i-'0'); i = getchar(); }
   return j;
}

int N, T;
int  B[100001];

int main(int argc, char *argv[]){
	bool out = true;
	#ifndef ONLINE_JUDGE
		freopen("d:/home/code/GCJ/Aa.txt","r",stdin);
		if( out){
			freopen("d:/home/code/GCJ/Out.txt","w",stdout);
		}
	#endif
	int nt = getnum<int>();
	for(int numt = 1; numt <= nt; ++numt){
		int N = getnum<int>();
		memset(B,-1,sizeof(B));
		vi d(N), l(N);
		for(int i = 0; i < N; ++i){
			int dd = getnum<int>();
			int ll = getnum<int>();
			d[i] = dd, l[i] = ll;
		}
		int D = getnum<int>();
		printf( "Case #%d: ", numt);
		bool ok = false;
		int c = 0;
		B[0] = min(d[0],l[0]);
		if( 2*B[0] >= D ){
			ok = true;
			goto end;
		}
		for(int i = 0; i < N; ++i){
			int  lon = B[i];
			if( lon < 0 ) break;
			for(int j = i+1; j < N; ++j){
				if( d[j]-d[i] > lon )
					break;
				int len = std::min( d[j]-d[i], l[j] );
				if( len >= B[j] )
					B[j] = len;
				if( d[j] + len >= D){
					ok = true;
					goto end;
				}
			}
		}
end:
		if( ok ) printf("YES\n");
		else     printf("NO\n");

		fflush(stdout);
	}
	return 0;
}
