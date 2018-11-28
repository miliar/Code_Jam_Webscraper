#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>

#define lld long long int 
#define EOL '\0'

#define N 100002
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define rep(n) for(int i =0;(i)<(int)(n);(i)++)

using namespace std;

char g[4][5];
void read() { 
	rep(4) 
		cin>>g[i];//,cout<<g[i]<<endl;
};

bool haswon(char player) { 
	bool won = false; 
	bool line;
	for(int i=0;i<4;i++,won=won || line) { 
		line = true;
		for(int j=0;j<4;j++) 
			line = line && (g[i][j]==player || g[i][j]=='T');
	}
	for(int i=0;i<4;i++, won = won || line) { 
		line = true;
		for(int j=0;j<4;j++) 
			line = line && ( g[j][i]==player || g[j][i]=='T');
	}
	line = true;
	for(int i=0;i<4;i++) 		
			line = line  && ( g[i][i]==player || g[i][i]=='T');
	won = won || line; 
	line = true;
	for(int i=0;i<4;i++) 		
			line = line  && ( g[i][3-i]==player || g[i][3-i]=='T');
	won = won || line;
	return won;
}

bool compelted() {
	bool complete = true;
	for(int i=0;i<4;i++) 
		for(int j=0;j<4;j++) 
			complete = complete && ( g[i][j] != '.');
	return complete;
}

string solve() { 
	if(haswon('X'))
		return "X won";
	else if(haswon('O'))
		return "O won";
	else if(compelted())
		return "Draw";
	else 
		return "Game has not completed";
}
int main() 
{
	int n;
	freopen("C:\\MyCode\\jam\\Data\\A-large.in", "r",stdin);
	freopen("C:\\MyCode\\jam\\Data\\A-large.out", "w",stdout);
	cin>>n;string s;
	rep(n) 
		read(),cout<<"Case #"<<i+1<<": "<<solve()<<endl;
	return 0;
}