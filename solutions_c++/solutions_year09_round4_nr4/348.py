#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<sstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;

#define LET(x,a) 	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	IFOR(it,v.begin(),v.end())
#define FOR(i,a,b)  	for(int i=(int)(a) ; i < (int)(b);++i)
#define REP(i,n) 	FOR(i,0,n)
#define PB		push_back
#define MP 		make_pair
#define EPS		1e-9
#define INF 2000000000

typedef vector<int>	VI;
typedef long long	LL;
typedef pair<int,int>	PI;

typedef long double LD;

int x11[1000],y11[1000],r1[1000];

int main(){
	int t;
	cin>>t;
	FOR(cas,1,t+1){
		cout<<"Case #"<<cas<<": ";
		int n;
		cin>>n;
		REP(i,n){
			int x,y,r;
			cin>>x>>y>>r;
			x11[i]=x;y11[i]=y;r1[i]=r;
		}
		if(n==1){
			printf("%.6Lf\n",(LD)r1[0]);
			continue;
		}
		if(n==2){
			printf("%.6Lf\n",(LD)max(r1[0],r1[1]));
			continue;
		}
		LD min1=INF;
		REP(i,3)REP(j,3)if(i!=j){
			int k=3-i-j;
			LD ans = r1[i]+r1[j];
			ans+=sqrtl((x11[i]-x11[j])*(x11[i]-x11[j])+(y11[i]-y11[j])*(y11[i]-y11[j]));
			ans/=2.0;
			min1=min(min1,max(ans,(LD)r1[k]));
		}
		printf("%.6Lf\n",min1);
	}
}

