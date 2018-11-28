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

int t,wyn,w;
LL C,L,P,strz;
int dp[1007];
bool found[1007];
int rozw(int x){
	if (found[x]) return dp[x];
	if (x<=1) return 0;
	found[x]=true;
	dp[x]=1+rozw(x/2+x%2);
	return dp[x];
}
int main(){
	scanf("%d",&t);
	REP(nr,t){
		printf("Case #%d: ",nr+1);
		scanf("%lld%lld%lld",&L,&P,&C);
		wyn=0,w=0;
		while(L<P){
			wyn++;
			L*=C;
	//		printf("L P%lld  %lld\n",L,P);
		}
	//	printf("wyn=%d\n",wyn);
		printf("%d\n",rozw(wyn));
	}
}
