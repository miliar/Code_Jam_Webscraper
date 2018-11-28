#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
using namespace std;

inline bool isdig(int a){return unsigned(a-'0') < 10;}
inline bool isdletter(int a){return unsigned(a-'0') < 10 || unsigned(a-'a') <= 'z'-'a' || a == '/' ;}
template<class T> static inline T getnum(){
   unsigned i; T j;
   do i = getchar(); while(!isdig(i));
   j = i-'0';  i=getchar() ;
   while(isdig(i)){ j = (j<<1)+(j<<3)+(i-'0'); i = getchar(); }
   return j;
}
string getstr(){
	char bf[1000]; int i,j=0;
	do i = getchar(); while(!isdletter(i));
	while(isdletter(i)){ bf[j++] = i; i = getchar(); }
	bf[j]=0;
	return string(bf);
}


int main(int argc, char *argv[]){
	#ifndef ONLINE_JUDGE
		freopen("Ab.txt","r",stdin);
	#endif
	int nt = getnum<int>();
	char bf[1000];

	for(int j = 1; j <= nt; ++j){
		unsigned N = getnum<unsigned>();
		unsigned M = getnum<unsigned>();
		set<string> S; S.insert( "/" );
		vector<string> T(M);
		for(int n = 0; n < N; ++n){
			string s = getstr();
			S.insert(s);
		}
		for(int n = 0; n < M; ++n){
			T[n] = getstr();
		}
		int nins = 0;
		for( int n = 0; n < M; ++n){
			string &q = T[n];
			if( S.count( q ) == 0 ){
				set<string>::iterator it = S.lower_bound( q );
				string p = *--it;
				int li = 0, m = min(p.size(), q.size()), i;
				bool end = true;
				for(i = 0; i < m; ++i){
					if( p[i] != q[i] ){
						end = false;
						break;
					} else if( p[i] == '/' )
						li = i;
				}
				if( end && q[i] == '/' ) li = m;
				for(int j = li+1; j <= q.size(); ++j){
					if( j == q.size() || q[j] == '/' ){
						string w = q.substr(0,j);
						S.insert( w );
						nins++;
					}
				}
			}
		}
		printf( "Case #%d: %d\n", j, nins);
	}
}
