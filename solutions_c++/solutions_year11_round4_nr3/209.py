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
vector<int> p;
int jaka[1000007];
void wrzuc(int x){
	int tm;
//	printf("wrzucam %d\n",x);
	for(int i=0;p[i]*p[i]<=x;i++){
		if (!(x%p[i])){
			tm=0;
			while(!(x%p[i])){
				x/=p[i];
				tm++;
			}
			jaka[p[i]]=max(jaka[p[i]],1);
//			printf("jaka[%d]=%d\n",p[i],jaka[p[i]]);
		}
	}
	if(x>1) {
		jaka[x]=max(jaka[x],1);
	}
}
void prim(int x){
	for(int i=0;p[i]*p[i]<=x;i++)
		if (!(x%p[i])) return;
	p.PB(x);
}
int t,mn,mx,tmm;
LL n;
int wjakiej(LL x,LL y){
	LL tm=1LL; int res=-1;
	while(tm<=y){ tm*=(LL)x; res++; }
	return res;
}
int main(){
	scanf("%d",&t);
	p.PB(2);
	for(int i=3;i<1000015;i++) prim(i);
	REP(nr,t){
		printf("Case #%d: ",nr+1);
		scanf("%lld",&n);
		if (n==1){ printf("0\n"); continue; }
		mn=0; mx=1;
		for(int i=0;(LL)(p[i])*(LL)(p[i])<=n;i++){
			tmm=wjakiej(p[i],n);
		//	printf("%d w %d\n",p[i],tmm);
			mn+=!!tmm;
			mx+=tmm;
		}
		printf("%d\n",mx-mn);
	}
}
