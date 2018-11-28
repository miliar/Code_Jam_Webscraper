#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

#define rep(i,st,ed) for (int i=st; i<ed; i++)
#define foreach(it,s) for (__typeof(s.begin()) it=s.begin(); it!=s.end(); ++it)

const int MAXN=100001;
const int INF=0x3f3f3f3f;
const double eps=1e-8;

const int dir[4][2]={{1,0},{0,1},{1,1},{1,-1}};

int ca;
string a[4];

void init(){
	rep(i,0,4) cin>>a[i];
}

bool is_oever(){
	rep(i,0,4) rep(j,0,4) if (a[i][j]=='.') return false;
	return true;
}

bool range(int x, int y){
	return 0<=x && x<4 && y>=0 && y<4;
}

int count(int x, int y, int k, char ch){
	int ret=0,nx=x,ny=y;
	while (range(nx,ny)){
		ret+=ch==a[nx][ny] || a[nx][ny]=='T';
		nx+=dir[k][0],ny+=dir[k][1];
	}
	nx=x-dir[k][0],ny=y-dir[k][1];
	while (range(nx,ny)){
		ret+=ch==a[nx][ny] || a[nx][ny]=='T';
		nx-=dir[k][0],ny-=dir[k][1];
	}
	return ret;
}

bool is_win(char ch){
	rep(i,0,4) rep(j,0,4) rep(k,0,4){
		if (count(i,j,k,ch)>=4) return true;
	}
}

void solve(){
	bool over=is_oever();
	bool X=is_win('X'),O=is_win('O');
	if (X) cout<<"X won"<<endl; else
	if (O) cout<<"O won"<<endl; else 
	if (over) cout<<"Draw"<<endl; else cout<<"Game has not completed"<<endl;
}

int main(){
	freopen("A.out","w",stdout);
	cin>>ca;
	rep(i,0,ca){
		cout<<"Case #"<<i+1<<": ";
		init();
		solve();
	}
	return 0;
}

