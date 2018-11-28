#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <sstream>
#include <iomanip>

using namespace std;
#define INF 2000000000

typedef long long ll;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

vector<vector<int> > Ts,T;

int c;
int H,W;
int dx[]={-1,0,0,1},dy[]={0,-1,1,0};

bool val(int i, int j){
	if(i < 0 || j < 0 || i >= H || j >= W) return 0;
	return 1;
}

void dfs(int i, int j){
	if(!val(i,j)) return;
	Ts[i][j] = c;
	for(int k=0;k<4;k++) if(val(i+dx[k],j+dy[k])){
		int dagua=-1,minh = T[i+dx[k]][j+dy[k]];
		for(int p=0;p<4;p++) if(val(i+dx[k]+dx[p],j+dy[k]+dy[p]) && T[i+dx[k]+dx[p]][j+dy[k]+dy[p]] < minh) 
						dagua=p,minh=T[i+dx[k]+dx[p]][j+dy[k]+dy[p]];
		if(dagua==0) dagua=3;
		else if(dagua==3) dagua=0;
		else if(dagua==1) dagua=2;
		else if(dagua==2) dagua=1;
		if(dagua==k) dfs(i+dx[k],j+dy[k]);
	}
}

int main(){
	int Tc;
	cin >> Tc;
	for(int t=1;t<=Tc;t++){
		cout << "Case #" << t << ":" << endl;
		cin >> H >> W;
		T = vector<vector<int> > (H,vector<int>(W));
		for(int i=0;i<H;i++) for(int j=0;j<W;j++) cin >> T[i][j];

		Ts = vector<vector<int> > (H,vector<int>(W,-1));
		c=0;

		while(1){
			bool sig=0;
			for(int i=0;i<H;i++) for(int j=0;j<W;j++) if(Ts[i][j]==-1){
				bool v=1;
				for(int k=0;k<4;k++) if(val(i+dx[k],j+dy[k]) && T[i+dx[k]][j+dy[k]] < T[i][j]) v=0;
				if(v){ dfs(i,j); c++; sig=1; }
			}
			if(!sig) break;
		}

		char cs = 'a';
		map<int,char> cambio;

		for(int i=0;i<Ts.size();i++){ for(int j=0;j<Ts[i].size();j++){
			if(!cambio.count(Ts[i][j])) cambio[Ts[i][j]] = cs++;
			cout << cambio[Ts[i][j]];
			if(j!=Ts[i].size()-1) cout << " ";
			}	
		cout << endl; }
	}
}
