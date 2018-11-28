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
#include<gmp.h> // http://gmplib.org/
#include<gmpxx.h>
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
PII tab[1007];
bool przec(int x,int y){
	if (tab[x].F<tab[y].F&&tab[x].S>tab[y].S)
		return true;
	if (tab[x].F>tab[y].F&&tab[x].S<tab[y].S)
		return true;
	return false;
}
int t,n,wyn;
int main(){
	scanf("%d",&t);
	REP(nr,t){
		printf("Case #%d: ",nr+1);
		wyn=0;
		scanf("%d",&n);
		REP(i,n) scanf("%d%d",&tab[i].F,&tab[i].S);
		REP(i,n) for(int j=i+1;j<n;j++){
			if( przec(i,j)) wyn++;
		}
		printf("%d\n",wyn);
	}
}
