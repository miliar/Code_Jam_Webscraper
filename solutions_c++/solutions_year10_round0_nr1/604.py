#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

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
		freopen("Ab.txt","r",stdin);
	#endif
	int nt = getnum<int>();
	for(int j = 1; j <= nt; ++j){
		unsigned N = getnum<unsigned>();
		unsigned K = getnum<unsigned>();
		bool on = ( K & ((1u<<N)-1) ) == ((1u<<N)-1);
		printf( "Case #%d: ", j);
		if(on)
			printf( "ON\n" );
		else
			printf( "OFF\n" );
	}
}
