#include <cstdio>
#include <cmath>
#include <map>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <cstdlib>
#include <stack>
#define FOR(i,j,n) for (int i=j;i<n;++i)
#define FORI(i,j,n) for (int i=j;i<=n;++i)
#define FORN(i,n) FOR(i,0,n)
#define sz size()
#define PB(a) push_back(a)
#define foreach(i, c) for( __typeof( (c).rbegin() ) i = (c).rbegin(); i != (c).rend(); ++i )
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define MIN(a,b) (a < b ? a : b)
#define MAX(a,b) (a > b ? a : b)
#define ALL(x) x.begin(), x.end()
#define INF 1<<30

using namespace std;

int N,n,m;
int T[500][500];
int D[500][500];
int D1[500][500];
char B[500][500];

int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
char curr='a';
bool valid(int x,int y){
	return x>=0 && x<n && y>=0 && y<m;
}

char dfs(int x,int y){

	D[x][y]=1;
	int mm=1<<30;
	int bx=x,by=y;
	FORN(i,4){
		int px= x+dir[i][0];
		int py= y+dir[i][1];
		if (valid(px,py) && T[px][py]<T[x][y] && mm>T[px][py] ){
			mm=T[px][py];
			bx=px;
			by=py;
		} 
	}
	
	if (mm!=1<<30){
		if (D[bx][by]){
			return  B[x][y]=B[bx][by];
		}
		else {
			return B[x][y]=dfs(bx,by);
		}
	}
	else {
		B[x][y]=curr++;
		return B[x][y];
	}

}


int main(){

 	cin>>N;

	FORN(__case,N){

	cin>>n>>m;
	FORN(i,n)FORN(j,m)cin>>T[i][j];
	curr='a';
	memset(D,0,sizeof D);
	FORN(i,n)
	 FORN(j,m)
	  if (D[i][j]==0){
		dfs(i,j);
	  }

	printf("Case #%d:\n",__case+1);
	
	FORN(i,n){
	bool e=0;
		FORN(j,m){
			if (e)
				cout<<" ";
			cout<<B[i][j];
			e=1;
		}
	cout<<endl;
	}
	}

	
    


    return 0;
}




