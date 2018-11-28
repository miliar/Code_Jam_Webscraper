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

const int mp=11;
int mem[1<<mp][mp];
int p;
int m[1<<mp],inp[1<<mp];

int go(int i,int misses){
	if(i>=(1<<p))	return (misses<=m[i-(1<<p)])?0:INF;
	int & ret=mem[i][misses];
	if(ret!=-1)	return ret;	
	ret=min(go(2*i,misses+1)+go(2*i+1,misses+1),INF);
	ret=min(ret,inp[i]+go(2*i,misses)+go(2*i+1,misses));
	return ret;
}

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int Kase=GI;
	FOR(kase,1,Kase+1){
		p=GI;
		REP(i,(1<<p))	m[i]=GI;
		reverse(m,m+(1<<p));
		for(int i=(1<<p)-1;i>=1;i--)	inp[i]=GI;
		printf("Case #%d:",kase);
		int ans=0;
		memset(mem,-1,sizeof(mem));
		ans=go(1,0);
		printf(" %d\n",ans);
		cerr<<"Completed "<<kase<<endl;
	}
	
	cerr<<"Completed all"<<endl;
	while(1);
	return 0;
}
