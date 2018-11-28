#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cmath>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;

const int mn=102;
int m,n;
char seenid;
int grid[mn][mn];
char ans[mn][mn];

#define ok(x,y) (x>=0 && x<m && y>=0 && y<n)

int dx[]={-1,0,0,1},dy[]={0,-1,1,0};

char go(int x,int y){
	char & ret=ans[x][y];
	if(ret!='0')	return ret;
	int mi=grid[x][y],mk=-1;
	REP(k,4){
		int x1=x+dx[k],y1=y+dy[k];
		if(!ok(x1,y1))	continue;
		if(grid[x1][y1]<mi){
			mi=grid[x1][y1];
			mk=k;
		}
	}
	if(mk==-1){
		ret=seenid++;
		return ret;
	}
	return ret=go(x+dx[mk],y+dy[mk]);
}

int main(){
	
	int Kase=GI;
	FOR(kase,1,Kase+1){
		seenid='a';
		m=GI,n=GI;
		REP(i,m)	REP(j,n)	grid[i][j]=GI;
		REP(i,m)	REP(j,n)	ans[i][j]='0';
		printf("Case #%d:\n",kase);
		REP(i,m){
			REP(j,n)		printf("%c ",go(i,j));
			printf("\n");
		}
	}
	
	
	return 0;
}
