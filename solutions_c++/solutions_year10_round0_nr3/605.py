#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

typedef unsigned long long int Int;
inline bool isdig(int a){return unsigned(a-'0') < 10;}
template<class T> static inline T getnum(){
   unsigned i; T j;
   do i = getchar(); while(!isdig(i));
   j = i-'0';  i=getchar() ;
   while(isdig(i)){ j = (j<<1)+(j<<3)+(i-'0'); i = getchar(); }
   return j;
}

Int g[1000], e[1000], t[1000], r[1000], R, K, G, res;
int N;

int main(int argc, char *argv[]){
	#ifndef ONLINE_JUDGE
		if( argc > 1 && argv[1][0] == 's')
			freopen("Cs2.txt","r",stdin),freopen("Cs2.out","w",stdout);
		else if( argc > 1 && argv[1][0] == 'b')
			freopen("Cb.txt","r",stdin),freopen("Cb.out","w",stdout);
		else
			freopen("C.txt","r",stdin);
	#endif
	int nt = getnum<int>();
	for(int jj = 1; jj <= nt; ++jj){
		R = getnum<unsigned>();
		K = getnum<unsigned>();
		N = getnum<unsigned>();
		G = 0;
		for(int k = 0; k < N; ++k){
			g[k] = getnum<unsigned>();
			G+=g[k];
		}
		if( G <= K ){
			res = G*R;
		} else {
			res = 0;
			memset( e, 0, N*sizeof(Int) );
			memset( t, 0, N*sizeof(Int) );
			memset( r, 0, N*sizeof(Int) );
			Int ga = 0, gt = 0, rt = 0;
			int j = 0, i = 0;
			bool stop=false;
			while( e[i] == 0){
				Int gc = 0;
				while( (gc += g[j]) <= K ){
					if( ++j == N ){
						stop = true;
						j = 0;
					};
				}
				gc -= g[j];
				ga += gc;
				r[i]++, rt++;
				if( rt == R ){
					res = gt+ga;
					goto end;
				}
				if( stop){
					t[i] = j;
					e[i] += ga;
					gt += ga;
					i = j;
					ga = 0;
					stop = false;
				}
			}
			gt = 0, rt = 0;
			int ib = i; // the cycle starts here
			i = 0;
			if( ib != 0 ){
				do res += e[i], R-= r[i], i = t[i];  while( i != ib );
			}
			do gt += e[i], rt += r[i], i = t[i]; while( i != ib);
			res += (R/rt) * gt;
			R = R%rt;
			if( res == 0 ) i = 0;
			while( R > 0 ){
				if( R >= r[i] ){
					res+= e[i], R-= r[i]; i = t[i];
				} else break;
			}
			while( R > 0 ){
				Int gc = 0;
				while( (gc += g[i]) <= K ){
					if( ++i == N ){
						i = 0;
					};
				}
				gc -= g[i];
				res += gc; R--; gc = 0;
			}
		}
		end:
		printf( "Case #%d: %lld\n", jj,res);
	}
}
