#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<sstream>
#include<algorithm>
#include<map>
#include<queue>
using namespace std;
vector<string> grid;
int dir [][2] = {0,0 , 1,0 , 0,1, 1,1};

void print ( int kase ,  vector<string> ans )
{
 	 cout <<"Case #"<<kase<<":\n";
	for( int i = 0; i < ans.size(); i++, cout <<"\n") cout << ans[i];
	 //cout<<yes;
	 cout <<"\n";
 	 return ;
}

bool canFitRedTile(int x , int y) {
	for (int i = 0; i < 4 ;i++) {
		int dx = x + dir [i][0] , dy = y + dir [i][1];
		if (dx < 0 || dy < 0 || dx >= grid.size() || dy >= grid[0].size()) return false;
		if (grid[dx][dy] != '#') return false;
	}
	return true;
}

void fitRedTile(int x, int y) {
	for (int i = 0; i < 4 ;i++) {
		int dx = x + dir [i][0] , dy = y + dir [i][1];
		if (i ==0 || i == 3) grid[dx][dy] = '/';
		else grid[dx][dy] = '\\';
	}
}

void process() {
	for( int i = 0; i < grid.size(); i++) 
		for (int j = 0; j < grid[i].size(); j++) if (grid [i][j] == '#' && canFitRedTile(i,j)) fitRedTile(i,j);
			
}

bool isPossible() {
	for (int i = 0; i < grid.size(); i++) for (int j = 0; j < grid[i].size(); j++) if (grid[i][j] == '#') return false;
	return true;
}

int main() {
	freopen ("A-large.in","r",stdin);
 	freopen("A-large.out","w",stdout);
	int T, kase = 0; 
	for (cin >> T; T; T--) {
		int R, C;
		string a; 
		grid.clear();
		for(cin>>R>>C; R; R--) cin >> a, grid.push_back(a);
		process();
		if (isPossible()) print(++kase, grid);
		else {
			grid.clear(); grid.push_back("Impossible");
			print(++kase, grid);
		}
	}
}
