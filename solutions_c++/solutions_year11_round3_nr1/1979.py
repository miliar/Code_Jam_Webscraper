#include<iostream>
#include<cstdio>
#include<vector>
#include<list>
#include<map>
#include<cmath>
#include<cstdlib>
using namespace std;
#define EPS 0.000001
#define FOR(i,N) for(int i=0;i<N;i++)
#define FORE(i,N) for(int i=1;i<=N;i++)
#define isInt(a) (fabs((a - (int)a))<EPS)
#define lenght(x,y,z) sqrt(x*x+y*y+z*z)
#define max(a,b)  a>b?a:b
#define min(a,b)  a<b:b:a
#define isBlue(a) a=='#'

int main(void){
	int T, R, C;
	cin >> T;
	FORE(tc,T){
		printf("Case #%d:\n",tc);
		cin >> R >> C;
		char t[52][52];
		FOR(i,R) 
			FOR(j,C)
				cin >> t[i+1][j+1];
		FOR(j,C) t[0][j] = t[R+1][j] = '.';
		FOR(i,C) t[i][0] = t[C+1][0] = '.';
		int possible = true;
		for(int i=1;i<=R && possible; i++)
			for(int j=1;j<=C;j++){
				if(t[i][j] == '#'){
					if( isBlue(t[i][j+1]) && isBlue(t[i+1][j]) && isBlue(t[i+1][j+1]) ){
						t[i][j] = '/'; t[i][j+1] = '\\';
						t[i+1][j] = '\\' ; t[i+1][j+1] = '/';
					}else possible = false;
				}
			}
		if(possible){
			FORE(i,R){
				FORE(j,C)	
					cout << t[i][j];
				printf("\n");
			}
		}else printf("Impossible\n");
	}
	return 0;
}
