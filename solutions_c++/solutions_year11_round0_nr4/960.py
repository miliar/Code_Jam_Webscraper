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
typedef long double ld;
ld anty[1007];
void liczanty(){
	anty[1]=1.0;
	for(int i=2;i<1007;i++){
		anty[i]=anty[i-1]/((ld)(i));
	}
}
ld dp2[1007][1007];
bool found2[1007][1007];
ld trafi(int ile,int zilu){
	if (ile>zilu) return 0.0;
	if (!ile) return anty[zilu];
	if (found2[ile][zilu]) return dp2[ile][zilu];
	found2[ile][zilu]=true;
	dp2[ile][zilu]=anty[zilu]*trafi(ile-1,zilu-1)+(1-anty[zilu])*trafi(ile,zilu-1);
	return dp2[ile][zilu];
}
ld dp[1007];
bool found[1007];
ld wyn(int posortuj){
	if (found[posortuj]) return dp[posortuj];
	dp[posortuj]=0.0;
	found[posortuj]=true;
	for(int i=1;i<=posortuj;i++){
		dp[posortuj]+=1.0+wyn(posortuj-i)*trafi(i,posortuj);
	}
	printf("dp[%d]=%Lf\n",posortuj,dp[posortuj]);
	return dp[posortuj];
}
int t,n,tab[1007],il;
void czysc(){
	REP(i,1007) found[i]=false;
	found[0]=true; dp[0]=0.0; found[1]=true; dp[1]=0.0;
	found2[1][1]=true;
	dp2[1][1]=1.0;
}
int main(){
	liczanty();
	czysc();
	scanf("%d",&t);
	REP(nr,t){
		printf("Case #%d: ",nr+1);
		scanf("%d",&n);
		il=0;
		REP(i,n){ scanf("%d",&tab[i]); tab[i]--; if (tab[i]!=i) il++; }
		printf("%Lf\n",(ld)(il));
	}
}
