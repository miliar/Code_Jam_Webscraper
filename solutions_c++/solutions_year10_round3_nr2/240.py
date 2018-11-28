#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <cmath>
using namespace std;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef long long int qint;


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
		freopen("B.txt","r",stdin);
	#endif
	int nt = getnum<int>();

	for(int tc = 1; tc <= nt; ++tc){
		qint L = getnum<unsigned>();
		qint P = getnum<unsigned>();
		int  C = getnum<unsigned>();
		int ntst = 0, q=0;
		for(qint K = L; K < P;K*=C, q++ );
		for( int t = 1; t < q; t*=2,ntst++);
		printf( "Case #%d: %d\n", tc, ntst );
	}
}
