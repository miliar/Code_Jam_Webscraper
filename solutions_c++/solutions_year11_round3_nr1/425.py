//Jakub Sygnowski
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
//#include<gmp.h> // http://gmplib.org/
//#include<gmpxx.h>
using namespace std;
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define F first
#define S second
#define INF 1000000007
#define PB push_back
#define MP make_pair
typedef pair<int,int> PII;
typedef long long LL;
char tab[56][56];
int t,n,m;
bool wstaw(int x,int y){
	if (x+1>=m || y+1>=n) return false;
	if (tab[x][y+1]=='.' || tab[x+1][y]=='.' || tab[x+1][y+1]=='.') return false;
	tab[x][y]='/'; tab[x][y+1]='\\'; tab[x+1][y]='\\'; tab[x+1][y+1]='/';
	return true;
}
bool odp;
int main(){
	scanf("%d",&t);
	REP(nr,t){
		printf("Case #%d:\n",nr+1);
		scanf("%d%d",&n,&m);
		REP(y,n) REP(x,m) scanf(" %c",&tab[x][y]);
		odp=true;
		REP(y,n) REP(x,m){
			if (tab[x][y]=='#'){
				if (!wstaw(x,y)) odp=false;
			}
		}
		if (!odp) printf("Impossible\n");
		else {
			REP(y,n){ REP(x,m) printf("%c",tab[x][y]); printf("\n"); }
		}
	}
}
