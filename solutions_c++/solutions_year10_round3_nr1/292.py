#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
using namespace std;
typedef pair<int,int> ii;
typedef vector<ii> vii;


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
		freopen("Aa.txt","r",stdin);
	#endif
	int nt = getnum<int>();

	for(int tc = 1; tc <= nt; ++tc){
		unsigned N = getnum<unsigned>();
		vii P(N);
		int nin = 0;
		for(int j = 0; j < N; ++j){
			P[j].first = getnum<int>();
			P[j].second = getnum<int>();
			for(int k = 0; k < j; ++k){
				if( P[k].first < P[j].first && P[k].second > P[j].second ||
					P[k].first > P[j].first && P[k].second < P[j].second )
					nin++;
			}
		}
		printf( "Case #%d: %d\n", tc, nin);
	}
}
