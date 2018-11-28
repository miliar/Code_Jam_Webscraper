#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;
typedef vector<int> vi;
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
double steps[1001];

int main(int argc, char *argv[]){
	#ifndef ONLINE_JUDGE
		freopen("Aa.txt","r",stdin);
	#endif
	int nt = getnum<int>();
	for(int i = 1; i <= 1000; ++i)
		steps[i] = double(i);
	steps[1] = 0;
	for(int j = 1; j <= nt; ++j){
		int N = getnum<int>();
		vi p; p.push_back(0);
		for(int i = 1; i <= N; ++i){
			p.push_back(getnum<int>());
		}
		vi ciclo(N+1);
		double t = 0.;
		for(int i = 1; i <= N; ++i){
			if( ciclo[i] == 0 ){
				int len = 0, j = i, n =i;
				do n=j, j = p[j], ciclo[n] = 1, len++;
				while( ciclo[j]==0 );
				t+=steps[len];
			}
		}

		printf( "Case #%d: ", j);
		printf( "%d.%06d\n", int(floor(t)), int( (t-floor(t))*1000000+0.5 )); 
	}
	return 0;
}
