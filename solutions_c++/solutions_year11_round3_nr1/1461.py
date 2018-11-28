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

char buf[100];
char M[51][51];
int main(int argc, char *argv[]){
	#ifndef ONLINE_JUDGE
		freopen("Aa.txt","r",stdin);
	#endif
	int nt = getnum<int>();

	for(int j = 1; j <= nt; ++j){		
		int R = getnum<int>();
		int C = getnum<int>();
		bool found = true;
		for(int r = 0; r < R; ++r){
			gets(M[r]);
		}
		for(int r = 0; r < R; ++r){
			for(int c = 0; c < C; ++c){
				if(M[r][c] =='#' ){
					char up = '.', left = '.';
					if( r> 0) up = M[r-1][c];
					if( c> 0) left = M[r][c-1];
					bool rstart = up == '.' || up == '2' || up == '3';
					bool cstart = left == '.' || left == '1' || left == '3';
					if( rstart && cstart&& r+1<R && c+1<C ) M[r][c] = '0';
					else if( rstart && left == '0'&&r+1<R ) M[r][c] = '1';
					else if( cstart && up == '0'&&c+1<C ) M[r][c] = '2';
					else if( up == '1' && left == '2') M[r][c] = '3';
					else {
						found = false; goto fail;
					}
				} else {
					if( r>0 && ( M[r-1][c] == '0' || M[r-1][c] == '1') ){
						found = false; goto fail;
					}
					if( c>0 && ( M[r][c-1] == '0' || M[r][c-1] == '2') ){
						found = false; goto fail;
					}
				}
			}
		}

		fail:
		printf( "Case #%d:\n", j);
		if( !found) 
			printf( "Impossible\n");
		else {
			for(int r = 0; r < R; ++r){
				for(int c = 0; c < C; ++c){
					char t ;
					switch( M[r][c]){
						case '.': t = '.'; break;
						case '0': t = '/'; break;
						case '1': t = '\\'; break;
						case '2': t = '\\'; break;
						case '3': t = '/'; break;
					}
					printf( "%c", t);
				}
				printf("\n");
			}
		}
	}
	return 0;
}
