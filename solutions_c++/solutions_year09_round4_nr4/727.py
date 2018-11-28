//Jakub Sygnowski
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <sstream>
using namespace std;

#define REP(I,N) for(int I=0;I<(N);++I)
#define FOR(I,A,B) for(int I=(A);I<=(B);++I)
#define FORD(I,A,B) for(int I=(A);I>=(B);--I)
#define VAR(A,B) __typeof(B) A=B
#define FORE(I,X) for(VAR(I,(X).begin());I!=(X).end();++I)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define INF 1000000007
#define sq(A) ((A)*(A))
#define SZ(X) ((int)(X).size())
typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

struct plant{
	int x,y,r;
}tab[50];
int t,n;
long double dist(int a,int b){
	if (a==b) return 2*tab[a].r;
	return sqrt(sq(tab[a].x-tab[b].x)+sq(tab[a].y-tab[b].y))+tab[a].r+tab[b].r;
}
long double res;
int main(){
	scanf("%d",&t);
	REP(nr,t){
		scanf("%d",&n);
		REP(i,n) scanf("%d%d%d",&tab[i].x,&tab[i].y,&tab[i].r);
		if (n==3){
		//0 z 1
		res=max(dist(0,1),dist(2,2));
		//0 z 2
		res=min(res,max(dist(0,2),dist(1,1)));
		//1 z 2
		res=min(res,max(dist(1,2),dist(0,0)));
		}
		else {
			if (n==1) res=(long double)2*tab[0].r;
			else res=(long double)2*max(tab[0].r,tab[1].r);
		}
		printf("Case #%d: %Lf\n",nr+1,res/2);
	
	}
}
