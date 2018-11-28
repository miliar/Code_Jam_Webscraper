#include <iostream>
#include <cstdio>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <memory.h>
#include <algorithm>
#include <cstdlib>
#include <cassert>
#include <sstream>
#include <fstream>
using namespace std;


#define pb push_back
#define mp make_pair

typedef long long li;
typedef vector<li> vi;
typedef pair<int, int> pi;
double solve();
int main() {
	freopen("input", "r", stdin);
	freopen("output","w", stdout);
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	string s;
	getline(cin,s);
	cout<<fixed;
	cout.precision(30);
	for(int i=1;i<=t;++i){
		cout<<"Case #"<<i<<": ";
		cout<<solve();
		cout<<'\n';
	}
	return 0;
}
int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};
struct state{
	int i,j;
	double res;
	state(int i, int j, double res):i(i),j(j),res(res){
	}
	
	bool operator < (const state& b) const{
		return res < b.res || (res == b.res && (1000 * i + j < 1000*b.i + b.j));
	}
};
double solve(){
	int n,m,h;
	cin>>h>>n>>m;
	int f[101][101];
	int c[101][101];
	double res[101][101];
	for(int i=0;i<n;++i){
		for(int j=0;j<m;++j){
			cin>>c[i][j];
			res[i][j]=1e18;
		}
	}
	
	for(int i=0;i<n;++i){
		for(int j=0;j<m;++j){
			cin>>f[i][j];
		}
	}
	
	res[0][0] = 0;
	
	set<state> q;
	
	q.insert(state(0,0,res[0][0]));
	
	while(!q.empty()){
		state curState = *q.begin();
		q.erase(q.begin());
		
		if(curState.i == n-1 && curState.j == m-1) 
			return curState.res;
		
		for(int i=0;i<4;++i){
			int ni = curState.i + dx[i];
			int nj = curState.j + dy[i];
			if(ni<0 || ni>=n || nj<0 || nj>=m) 
				continue;
			double startTime = max(curState.res, (h - c[ni][nj] + 50)/10.0);
			
			int cc = min(c[curState.i][curState.j], c[ni][nj]);
			int ff = max(f[curState.i][curState.j], f[ni][nj]);
			if(cc - ff < 50)
				continue;
			double waterLevel = h - 10 * startTime;
			double finishTime = startTime + 10;
			if(waterLevel >= f[curState.i][curState.j] + 20 - 1e-8)
				finishTime = startTime + 1;
			if(startTime == 0)
				finishTime = 0;
			//cout<<curState.i<<' '<<curState.j<<' '<<startTime<<' '<<waterLevel<<' '<<finishTime<<endl;
			if(finishTime < res[ni][nj]){
				q.erase(state(ni,nj, res[ni][nj]));
				res[ni][nj] = finishTime;
				q.insert(state(ni,nj, res[ni][nj]));
			}
			
		}
		
	}
	
	
	
	assert(false);
	return 0;
}