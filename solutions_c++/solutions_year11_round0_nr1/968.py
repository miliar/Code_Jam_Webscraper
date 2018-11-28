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
#define MAXV 107
typedef pair<int,int> PII;
typedef long long LL;

int t,n,gdzie,lasto,lastb,res,poso,posb;
char ktory;
int main(){
	scanf("%d",&t);
	REP(nr,t){
		printf("Case #%d: ",nr+1);
		scanf("%d",&n);
		lasto=0; lastb=0; res=0; poso=0; posb=0;
		REP(i,n){ scanf(" %c%d",&ktory,&gdzie); gdzie--;
			if (ktory=='O'){
				lasto+=(abs(poso-gdzie)+1);
				lasto=max(lasto,lastb+1);
				poso=gdzie;
			} else {
				lastb+=(abs(posb-gdzie))+1;
				lastb=max(lastb,lasto+1);
				posb=gdzie;
			}
		}
		printf("%d\n",max(lastb,lasto));
	}
}
