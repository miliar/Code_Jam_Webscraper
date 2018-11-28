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

int t,n,c,tab[1000007],l;
LL tim,res,doj[1000007],cal,tm;
int main(){
	scanf("%d",&t);
	REP(nr,t){
		printf("Case #%d: ",nr+1);
		scanf("%d%lld%d%d",&l,&tim,&n,&c);
		REP(i,c) scanf("%d",&tab[i]);
		for(int i=c;i<n;i++) tab[i]=tab[i%c];
	//	printf("Debug: ");
		res=0;
		REP(i,n) res+=2*tab[i];
		cal=res;
		for(int i=0;i<n;i++){
			doj[i+1]=doj[i]+2*tab[i];
		}
	//	REP(i,n+1) printf("%d ",doj[i]);
	//	printf("\ncal%lld\n",cal);
		if (!l){
			printf("%lld\n",res);
			continue;
		}
		if (l==1){
			REP(i,n){
				if (doj[i] >= tim)
					res=min(res,cal-tab[i]);
				else {
					if (tim< doj[i+1]){
						res=min(res,cal-((doj[i+1]-tim)/2));
					}
				}
			}
			printf("%lld\n",res);
			continue;
		}
		if (l==2){
			REP(i,n){
				for(int j=i+1;j<n;j++){
					if (doj[i]>=tim) {
						tm=-tab[i];
					} else {
						if (tim < doj[i+1])
							tm=-((doj[i+1]-tim)/2);
						else tm=0;
					}
					if (doj[j]+tm >= tim)
						res=min(res,cal+tm-tab[j]);
					else {
						if (tim < doj[j+1]+tm){
							res=min(res,cal+tm-(doj[j+1]+tm-tim)/2);
						}
					}
				}
			}
			printf("%lld\n",res);
		}
	}
}
