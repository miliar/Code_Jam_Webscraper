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

int t,tab[107],n,l,h;
bool ok(int x){
	REP(i,n) if ((x%tab[i]) && (tab[i]%x)) return false;
	return true;
}
bool odp;
int main(){
	scanf("%d",&t);
	REP(nr,t){
		printf("Case #%d: ",nr+1);
		scanf("%d%d%d",&n,&l,&h);
		REP(i,n){ scanf("%d",&tab[i]); }
		odp=false;
		for(int i=l;i<=h;i++){
			if (ok(i)){
				odp=true;
				printf("%d\n",i);
				break;
			}
		}
		if (!odp) printf("NO\n");
	}
}
