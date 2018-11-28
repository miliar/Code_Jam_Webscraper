#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;cin>>t;t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9
#define EPS LD(1e-9)
#define DINF LD(1e50)

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;
typedef double LD;

const int mc=202;
int c;
LD d, p[mc];
int v[mc];

bool fn(LD mid){
	LD last=-DINF;
	REP(i,c){
		LD cur=max(p[i]-mid,last+d);
		LD curlast=cur+(v[i]-1)*d;
		if(curlast>p[i]+mid)	return 0;
		last=curlast;
	}	
	return 1;
}

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int Kase=GI;
	FOR(kase,1,Kase+1){
		cin>>c>>d;
		REP(i,c)	cin>>p[i]>>v[i];
		LD lo=0, hi=LD(1e13), mid=(lo+hi)/2;
		REP(times,150){
			if(fn(mid))	hi=mid;
			else	lo=mid;	
			mid=(lo+hi)/2;
		}
		printf("Case #%d: %.10lf\n",kase,mid);
		cerr<<"Completed "<<kase<<endl;
	}
	
	cerr<<"Completed all"<<endl;
	while(1);
	return 0;
}
