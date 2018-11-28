#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iterator>
#include <queue>
#include <cstring>

#define pb push_back
#define VI vector<int>
#define VS vector<string>
#define sz(v) v.size()
#define len(s) s.length()
#define full(v) v.begin(),v.end()

#define repx(i,x,n) for(int i=x;i<n;i++)
#define rep(i,n) repx(i,0,n)

typedef long long ll;

const int INF = 1<<30;

using namespace std;

int main(void){
	int t;
	cin>>t;
	int cnt=1;
	while(t--){
		VS board;
		string s;
		rep(i,4){
			cin>>s;
			board.pb(s);
		}		
		int o=0,x=0,f=0,f1=0;
		VS boardx=board;
		VS boardo=board;
		rep(i,4){
			rep(j,4){
				if(board[i][j]=='T'){
					boardx[i][j]='X';
					boardo[i][j]='O';
					f=1;
					break;
				}
				if(board[i][j]=='.')f1=1;
			}
			if(f){
				f=0;
				break;
			}
		}
		
		//rows
		if(count(full(boardx),"XXXX")>=1) x=1;
		if(count(full(boardo),"OOOO")>=1) o=1;
		//cols
		rep(i,4){
			if(boardx[0][i]=='X'&&boardx[1][i]=='X'&&boardx[2][i]=='X'&&boardx[3][i]=='X')x=1;
			if(boardo[0][i]=='O'&&boardo[1][i]=='O'&&boardo[2][i]=='O'&&boardo[3][i]=='O')o=1;
		}
		if(boardx[0][0]=='X'&&boardx[1][1]=='X'&&boardx[2][2]=='X'&&boardx[3][3]=='X')x=1;
		if(boardx[0][3]=='X'&&boardx[1][2]=='X'&&boardx[2][1]=='X'&&boardx[3][0]=='X')x=1;
		if(boardo[0][0]=='O'&&boardo[1][1]=='O'&&boardo[2][2]=='O'&&boardo[3][3]=='O')o=1;
		if(boardo[0][3]=='O'&&boardo[1][2]=='O'&&boardo[2][1]=='O'&&boardo[3][0]=='O')o=1;
		
		if(x==1)cout<<"Case #"<<cnt++<<": X won\n";		
		else if(o==1)cout<<"Case #"<<cnt++<<": O won\n";
		else if(f1==1)cout<<"Case #"<<cnt++<<": Game has not completed\n";		
		else cout<<"Case #"<<cnt++<<": Draw\n";				
	}
	return 0;
}
