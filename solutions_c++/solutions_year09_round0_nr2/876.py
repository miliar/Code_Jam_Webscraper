#include <iostream>
#include <vector>
using namespace std;

int abs(int n) {
	if(n < 0)
		return -n;
	return n;
}

vector< vector<int> > panel;
vector< vector<char> > sol;
vector< vector<bool> > vis;
char temp;

char dfs(int x, int y) {
	vis[x][y] = true;
	int ym , xm ;
	int dif = 0;
	for(int i = -1; i <= 1; i++)
		for(int j = -1; j <= 1; j++)
			if(abs(i) != abs(j))
				if(dif < panel[x][y] - panel[x+i][y+j]) {
					xm = i;
					ym = j;
					dif = panel[x][y] - panel[x+i][y+j];
				}
	if(dif == 0) {
		sol[x][y] = temp;
		return temp;
	}

	if(vis[x+xm][y+ym]) {
		char tmp = sol[x+xm][y+ym];
		sol[x][y] = tmp;
		return tmp;
	}
	else {
		sol[x][y] = dfs(x+xm, y+ym);
		return sol[x][y];
	}
	
}

int main() {
	int T;
	cin >> T;
	for(int nacho = 1; nacho <= T; nacho++) {
		int H, W;
		cin >> H >> W;
		temp = 'a';
		panel = vector< vector<int> >(H+2, vector<int>(W+2, 1000000));
		sol = vector< vector<char> >(H+2, vector<char>(W+2));
		vis = vector< vector<bool> >(H+2, vector<bool>(W+2, false));
		for(int i = 1; i <= H; i++)
			for(int j = 1; j <= W; j++)
				cin >> panel[i][j];
		
		for(int i = 1; i <= H; i++)
			for(int j = 1; j <= W; j++)
				if(!vis[i][j]) {
					char hlp = dfs(i, j);
					if(hlp == temp)
						temp++;
				}
		
		cout << "Case #" << nacho << ":" << endl;
		for(int i = 1; i <= H; i++) {
			for(int j = 1; j <= W; j++) {
				cout << sol[i][j];
				if(j != W)
					cout << " ";
			}
			cout << endl;
		}
	}
	return 0;
}
