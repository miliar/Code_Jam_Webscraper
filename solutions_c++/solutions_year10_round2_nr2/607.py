#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
using namespace std;
typedef vector<int> vi;
typedef vector<double> vd;
inline bool isdig(int a){return unsigned(a-'0') < 10;}
template<class T> static inline T getnum(){
   unsigned i; T j;
   do i = getchar(); while(!isdig(i));
   j = i-'0';  i=getchar() ;
   while(isdig(i)){ j = (j<<1)+(j<<3)+(i-'0'); i = getchar(); }
   return j;
}

int main(int argc, char *argv[]){
	#ifndef ONLINE_JUDGE
		freopen("Bb.txt","r",stdin);
	#endif
	int nt = getnum<int>();
	char bf[1000];

	for(int j = 1; j <= nt; ++j){
		unsigned N = getnum<unsigned>();
		unsigned K = getnum<unsigned>();
		unsigned B = getnum<unsigned>();
		unsigned T = getnum<unsigned>();


		vector<unsigned> X(N), V(N);
		for(int i = 0; i < N; ++i)
			X[i] = getnum<unsigned>();
		for(int i = 0; i < N; ++i)
			V[i] = getnum<unsigned>();
		int nsw = 0;
		int nst = 0;
		for(int i = N-1; i >= 0; --i){
			if( X[i] + V[i]*T >= B ){
				nsw += nst;
				if(--K == 0) break;
			} else {
				nst++;
			}
		}
		if( K > 0)
			printf( "Case #%d: IMPOSSIBLE\n", j);
		else
			printf( "Case #%d: %d\n", j, nsw);
	}
}
