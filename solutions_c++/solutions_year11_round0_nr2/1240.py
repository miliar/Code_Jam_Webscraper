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
	typedef std::pair<char,char> cc;
	for(int j = 1; j <= nt; ++j){
		std::map<cc,char> c;
		int C = getnum<int>();
		char c1, c2, c3;
		for(int i = 0; i < C; ++i){
			scanf("%c%c%c ", &c1, &c2, &c3);
			c[cc(c1,c2)]=c3;
			c[cc(c2,c1)]=c3;
		}
		int D = getnum<int>();
		map<char,string> op;
		for(int i = 0; i < D; ++i){
			scanf("%c%c%c ", &c1, &c2, &c3);
			op[c1].push_back(c2);
			op[c2].push_back(c1);
		}

		int N = getnum<int>();
		int p = 0;
		map<char,int> pres;
		for(int i = 0; i < N; ++i){
			scanf("%c", &c1);
			if( p> 0 && c.count(cc(str[p-1],c1)) > 0){
				pres[str[p-1]]--, pres[c1]--;
				str[p-1] = c[cc(str[p-1],c1)];
			} else {
				bool clear = false;
				if( op.count(c1) ){
					string q = op[c1];
					for(int i = 0; i < q.length(); ++i){
						if( pres[q[i]] > 0 )
							clear = true;
					}
				}
				if( clear){
					p = 0;
					pres = map<char,int>();
				} else {
					pres[c1]++;
					str[p++]=c1;
				}
			}
		}
		printf( "Case #%d: ", j);
		printf( "[" );
		for(int i = 0; i < p; ++i){
			if( i > 0)printf( ", ");
			printf( "%c",str[i] );
		}
		printf( "]\n" );
	}
	return 0;
}
