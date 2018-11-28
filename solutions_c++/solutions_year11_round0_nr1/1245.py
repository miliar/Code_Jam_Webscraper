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


char ord[1000];
int bseq[1000];
char bcol[1000];
int N, T;




int main(int argc, char *argv[]){
	#ifndef ONLINE_JUDGE
		freopen("Aa.txt","r",stdin);
	#endif
	int nt = getnum<int>();
	for(int j = 1; j <= nt; ++j){
		int N = getnum<int>();

		int bp=1, op=1;
		int bt=0, ot=0;
		for(int i = 0; i < N; ++i){
			char col; int but;
			scanf("%c %d ", &col, &but);
			if( col == 'O' ){
				ot = std::max( ot + std::abs(but-op)+1,bt+1);
				op = but;
			} else {
				bt = std::max( bt + std::abs(but-bp)+1,ot+1);
				bp = but;
			}
		}
		printf( "Case #%d: ", j);
		printf( "%d\n",std::max(ot,bt) );
	}
	return 0;
}
