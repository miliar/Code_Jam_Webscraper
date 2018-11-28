#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;

inline bool isdig(int a){return unsigned(a-'0') < 10;}
template<class T> static inline T getnum(){
   unsigned i; T j;
   do i = getchar(); while(!isdig(i));
   j = i-'0';  i=getchar() ;
   while(isdig(i)){ j = (j<<1)+(j<<3)+(i-'0'); i = getchar(); }
   return j;
}

char str[200];
int main(int argc, char *argv[]){
	#ifndef ONLINE_JUDGE
		freopen("Aa.txt","r",stdin);
	#endif
	int nt = getnum<int>();
	for(int j = 1; j <= nt; ++j){
		int N = getnum<int>();
		int mn = 1000001;
		int sum = 0;
		int x = 0;
		for(int i = 0; i < N; ++i){
			int k = getnum<int>();
			x ^= k;
			sum+=k;
			if( k < mn ) mn = k;
		}
		printf( "Case #%d: ", j);
		if( x == 0 ){
			printf( "%d\n", sum-mn );
		} else 
			printf( "NO\n");
	}
	return 0;
}
