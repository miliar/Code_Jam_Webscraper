#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<list>
#include<queue>
#include<cmath>
#include<functional>
#include<algorithm>
#define INF (1<<29)
#define EPS 1e-10
#define rep(i,n) for(int i=0;i<(n);i++)
using namespace std;

char board[4][5];
bool win(char p){
	int c;
	rep(y,4){
		c=0;
		rep(x,4){
			if(board[y][x]==p||board[y][x]=='T')c++;
		}
		if(c==4)return true;
	}
	rep(x,4){
		c=0;
		rep(y,4){
			if(board[y][x]==p||board[y][x]=='T')c++;
		}
		if(c==4)return true;
	}
	c=0;
	rep(i,4)if(board[i][i]==p||board[i][i]=='T')c++;
	if(c==4)return true;
	c=0;
	rep(i,4)if(board[i][3-i]==p||board[i][3-i]=='T')c++;
	if(c==4)return true;
	return false;
}
int main(){
	int n;
	cin>>n;
	rep(i,n){
		char *ans;
		rep(i,4)cin>>board[i];
		if(win('O'))ans="O won";
		else if(win('X'))ans="X won";
		else{
			int c=0;
			rep(y,4)rep(x,4)if(board[y][x]=='.')c++;
			if(c)ans="Game has not completed";
			else ans="Draw";
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}