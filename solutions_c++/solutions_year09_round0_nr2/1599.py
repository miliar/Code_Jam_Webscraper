#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<cmath>
#include<string>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<vector>
#include<bitset>
#include<queue>
#include<stack>
#include<utility>
#include<list>
#include<set>
#include<map>
 
using namespace std;

#define eps 1e-9
#define INF INT_MAX
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).end(),(v).begin()

#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v))
#define CLEAR(t) memset((t),0,sizeof(t))

#define MAX 105
int NN=-1,NORTH=0,WEST=1,EAST = 2,SOUTH=3;
int H,W;
int maze[MAX][MAX];
int con[MAX][MAX];
int memo[MAX][MAX];

int getcon(int fil, int col){
	int vN,vW,vE,vS;
	vN=vW=vE=vS=INT_MAX;
	if(fil-1>=0) vN = maze[fil-1][col];
	if(fil+1<H) vS = maze[fil+1][col];
	if(col-1>=0) vW = maze[fil][col-1];
	if(col+1<W) vE = maze[fil][col+1];
	int val = min(min(min(vE,vS),vW),vN);
	if(val>=maze[fil][col]) return NN;
	if(val == vN) return NORTH;
	if(val == vW) return WEST;
	if(val == vE) return EAST;
	return SOUTH;
}
void dfs(int fil, int col, int color){
	if(memo[fil][col]>-1) return;
	memo[fil][col]=color;
	//para el hijo
	if(con[fil][col]==NORTH) dfs(fil-1,col,color);
	else if(con[fil][col]==WEST) dfs(fil,col-1,color);
	else if(con[fil][col]==EAST) dfs(fil,col+1,color);
	else if(con[fil][col]==SOUTH) dfs(fil+1,col,color);

	//para los padres
	if(fil-1>=0 && con[fil-1][col]==SOUTH) dfs(fil-1,col,color);	
	if(fil+1<H && con[fil+1][col]==NORTH) dfs(fil+1,col,color);
	if(col-1>=0 && con[fil][col-1]==EAST) dfs(fil,col-1,color);
	if(col+1<W && con[fil][col+1]==WEST) dfs(fil,col+1,color);
}
void run1(int caso){
	
	cin >>H>>W;
	CLEAR(maze);
	CLEAR(con);
	REP(i,H) REP(j,W) cin >>maze[i][j];
	REP(i,H) REP(j,W){
		con[i][j] = getcon(i,j);
	}
	memset(memo,-1,sizeof(memo));
	int act = 0;
	REP(i,H)REP(j,W){
		if(memo[i][j]==-1)
			dfs(i,j,act++);
	}	
	cout << "Case #"<<caso<<": "<<endl;
	REP(i,H){
		REP(j,W){
			if(j>0) cout <<" ";
			cout << (char)(memo[i][j]+'a');			
		}
		cout <<endl;
	}	
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}