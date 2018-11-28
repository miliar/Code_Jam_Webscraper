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

const int mn = 53;
int n,k;
char grid[mn][mn],newg[mn][mn];

int dx[]={1,1,1,0},dy[]={-1,0,1,1};
#define ok(x,y) (x>=0 && x<n && y>=0 && y<n)

void rotate(){
	REP(i,n)	REP(j,n)	newg[j][n-i-1]=grid[i][j];	
	REP(i,n)	REP(j,n)	grid[i][j]='.';
	REP(j,n){
		int p1=n-1,p2=n-1;
		for(;p1>=0;p1--){
			if(newg[p1][j]=='.')	continue;
			grid[p2--][j]=newg[p1][j];
		}	
	}
//	REP(i,n)	cerr<<grid[i]<<endl;
}

bool forms(int i,int j,char c){
	REP(dir,4){
		if(ok(i+(k-1)*dx[dir],j+(k-1)*dy[dir])){
			bool f=1;
			REP(z,k)	if(grid[ i+z*dx[dir] ][ j+z*dy[dir] ]!=c)	f=0;
			if(f)	return 1;
		}	
	}
	return 0;
}

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int Kase=GI;
	FOR(kase,1,Kase+1){
		n=GI,k=GI;
		REP(i,n)	scanf("%s",grid[i]);
		printf("Case #%d: ",kase);
		rotate();
		bool bb=0,br=0;
		REP(i,n)	REP(j,n){
			if(forms(i,j,'B'))	bb=1;
		}
		REP(i,n)	REP(j,n){
			if(forms(i,j,'R'))	br=1;
		}
		if(bb && br)	cout<<"Both"<<endl;
		if(bb && !br)	cout<<"Blue"<<endl;
		if(!bb && br)	cout<<"Red"<<endl;
		if(!bb && !br)	cout<<"Neither"<<endl;
		cerr<<"Completed "<<kase<<endl;
	}
	
	cerr<<"Completed all"<<endl;
	while(1);
	return 0;
}
