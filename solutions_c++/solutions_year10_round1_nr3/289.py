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

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;

bool iswinning(int a,int b){
	if(a<b)	swap(a,b);
	if(a>=2*b)	return 1;
	return !iswinning(b,a-b);	
}

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int Kase=GI;
	FOR(kase,1,Kase+1){
		
		int a1=GI,a2=GI,b1=GI,b2=GI;
		LL ans=0;
		FOR(a,a1,a2+1)	FOR(b,b1,b2+1){
			ans+=iswinning(a,b);
		}
		printf("Case #%d: ",kase);
		cout<<ans<<endl;
		cerr<<"Completed "<<kase<<endl;
	}
	
	cerr<<"Completed all"<<endl;
	while(1);
	return 0;
}
