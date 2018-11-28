#pragma warning(disable : 4996)
#include <cstdio>
#include <cmath>
#include <ctime>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <string>
using namespace std;
typedef std::vector<int> vi;
typedef std::vector<vi> vvi;
typedef std::pair<int,int> ii;
typedef std::vector<ii> vii;
typedef std::vector<string> vs;
typedef std::vector<double> vd;

#define sz(a) int(a.size())
#define REP(i,n) for(int i = 0; i < n; ++i)
#define FOR(i,a) for(int i = 0; i < sz(a); ++i)

inline bool isdig(int a){return unsigned(a-'0') < 10;}
template<class T> static inline T getnum(){
   unsigned i; T j;
   do i = getchar(); while(!isdig(i));
   j = i-'0';  i=getchar() ;
   while(isdig(i)){ j = (j<<1)+(j<<3)+(i-'0'); i = getchar(); }
   return j;
}

int N, T;

char buf[10000000];
char B[4][5];
int R[2][6];
int C[2][6];
int main(int argc, char *argv[]){
	bool out = true;
	#ifndef ONLINE_JUDGE
		FILE *F = fopen("Aa.txt","r");
		freopen("Aa.txt","r",stdin);
		if( out){
			freopen("Out.txt","w",stdout);
		}
	#endif
	int N;
	scanf("%d\n",&N);
	for( int tst = 0; tst < N; ++tst){
		scanf("%s\n",B[0]);
		scanf("%s\n",B[1]);
		scanf("%s\n",B[2]);
		scanf("%s\n",B[3]);
		scanf("\n");
		int nholes = 0;
		for(int r = 0; r < 6; ++r)  R[0][r] = R[1][r] = 0;
		for(int c = 0; c < 4; ++c)  C[0][c] = C[1][c] = 0;
		for(int r = 0; r < 4; ++r){
			for(int c = 0; c < 4; ++c){
				if( B[r][c] == '.'){
					nholes++;
				} else if( B[r][c] == 'T' ){
					R[0][r] ++;
					R[1][r] ++;
					C[0][c] ++;
					C[1][c] ++;
				} else if(B[r][c] == 'X' ){
					R[0][r] ++;
					C[0][c] ++;
				} else if(B[r][c] == 'O' ){
					R[1][r] ++;
					C[1][c] ++;
				}
			}
		}
		for(int r = 0; r < 4; ++r){
			if( B[r][r] == 'T' ){
				R[0][4] ++;
				R[1][4] ++;
			} else if(B[r][r] == 'X' ){
				R[0][4] ++;
			} else if(B[r][r] == 'O' ){
				R[1][4] ++;
			}
			if( B[r][3-r] == 'T' ){
				R[0][5] ++;
				R[1][5] ++;
			} else if(B[r][3-r] == 'X' ){
				R[0][5] ++;
			} else if(B[r][3-r] == 'O' ){
				R[1][5] ++;
			}
		}
		bool Xwin = false, Owin = false;
		for(int r = 0; r < 6; ++r){
			Xwin = Xwin | (R[0][r] == 4);
			Owin = Owin | (R[1][r] == 4);
		}
		for(int r = 0; r < 4; ++r){
			Xwin = Xwin | (C[0][r] == 4);
			Owin = Owin | (C[1][r] == 4);
		}
		printf("Case #%d: ", tst+1);
		if( Xwin){
			printf( "X won\n" );
		} else if( Owin){
			printf( "O won\n" );
		} else if( nholes == 0){
			printf( "Draw\n" );
		} else if( nholes > 0 ){
			printf( "Game has not completed\n" );
		}
	}

	return 0;
}
