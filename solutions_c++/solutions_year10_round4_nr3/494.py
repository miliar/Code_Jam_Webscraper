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

const int mr = 12, mv=300;
int r;
bool a[mv][mv], b[mv][mv];

bool update(){
	bool ret=1;
	REP(i,mv)	REP(j,mv)	if(a[i][j]==1)	{ret=0;break;}
	if(ret)	return 0;
	REP(i,mv)	b[0][i]=b[i][0]=0;
	FOR(i,1,mv)	FOR(j,1,mv){
		b[i][j]=a[i][j];
		if(a[i][j]==1 && a[i-1][j]==0 && a[i][j-1]==0)	b[i][j]=0;
		if(a[i][j]==0 && a[i-1][j]==1 && a[i][j-1]==1)	b[i][j]=1;
	}
	REP(i,mv)	REP(j,mv)	a[i][j]=b[i][j];
	return 1;
}

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int Kase=GI;
	FOR(kase,1,Kase+1){
		
		r=GI;
		memset(a,0,sizeof(a));
		REP(i,r){
			int x1=GI,y1=GI,x2=GI,y2=GI;
			FOR(i,x1,x2+1)	FOR(j,y1,y2+1)	a[i+100][j+100]=1;	
		}
		printf("Case #%d:",kase);
		int ans=0;
		while(1){
			if(update())	ans++;
			else	break;	
		}
		printf(" %d\n",ans);
		cerr<<"Completed "<<kase<<endl;
	}
	
	cerr<<"Completed all"<<endl;
	while(1);
	return 0;
}
