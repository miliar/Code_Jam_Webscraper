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

int t,n,lacz,s,r,a,b,w,sum,bie,it;
vector<PII> scie;
double res,czas,zost;
void wrzuc(double dl,int szyb){
//	printf("dlugosc %lf o szybkosci %d\n",dl,szyb);
	res+=(double)(dl)/(double)(szyb);
}
int main(){
	scanf("%d",&t);
	REP(nr,t){
		printf("Case #%d: ",nr+1);
		res=0.0;
		scanf("%d%d%d%d%d",&lacz,&s,&r,&bie,&n);
		sum=0;
		scie.clear();
		REP(i,n){ scanf("%d%d%d",&a,&b,&w); scie.PB(MP(w,b-a)); sum+=b-a; }
		if (lacz!=sum)
			scie.PB(MP(0,lacz-sum));
		sort(ALL(scie));
		czas=(double)(bie);
		it =0;
		while(it < scie.size()){
			if (czas<=0.0000001){
				wrzuc(scie[it].S,scie[it].F+s);
				it++;
				continue;
			}
			if (((double)(scie[it].S)/(double)(scie[it].F+r))<czas){
				czas-=((double)(scie[it].S)/(double)(scie[it].F+r));
				wrzuc(scie[it].S,scie[it].F+r);
			} else {
				wrzuc((double)(scie[it].F+r)*czas,scie[it].F+r);
				zost=(double)(scie[it].F+r)*czas;
				zost=scie[it].S-zost;
				wrzuc(zost,scie[it].F+s);
				czas=0.0;
			}
			it++;
		}
		printf("%.9lf\n",res);
	}
}
