//#include <iostream>
#include <fstream>
#include <queue>
#include <utility>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;
#define fo(i,n) for(int i=0,_n=(n); i<_n; i++)
#define range(i,a,b) for(int i=(a),_b=(b); i<_b; i++)

ifstream cin("in.txt"); ofstream cout("out.txt");
int T;
char grid[5][5];
int main() {
	cin>>T;
	fo(test,T) {
		fo(i,4) cin>>grid[i];
		bool win;
		fo(i,4) {
			win = true;
			fo(j,4) if(grid[i][j] != 'O' && grid[i][j] != 'T') win = false;
			if(win) break;
		}
		if(win) {
			cout<<"Case #"<<test+1<<": O won\n";
			continue;
		}
		fo(i,4) {
			win = true;
			fo(j,4) if(grid[i][j] != 'X' && grid[i][j] != 'T') win = false;
			if(win) break;
		}
		if(win) {
			cout<<"Case #"<<test+1<<": X won\n";
			continue;
		}
		fo(i,4) {
			win = true;
			fo(j,4) if(grid[j][i] != 'O' && grid[i][j] != 'T') win = false;
			if(win) break;
		}
		if(win) {
			cout<<"Case #"<<test+1<<": O won\n";
			continue;
		}
		fo(i,4) {
			win = true;
			fo(j,4) if(grid[j][i] != 'X' && grid[i][j] != 'T') win = false;
			if(win) break;
		}
		if(win) {
			cout<<"Case #"<<test+1<<": X won\n";
			continue;
		}
		win = true;
		fo(i,4) if(grid[i][i] != 'O' && grid[i][i] != 'T') win = false;
		if(win) {
			cout<<"Case #"<<test+1<<": O won\n";
			continue;
		}
		win = true;
		fo(i,4) if(grid[i][i] != 'X' && grid[i][i] != 'T') win = false;
		if(win) {
			cout<<"Case #"<<test+1<<": X won\n";
			continue;
		}
		win = true;
		fo(i,4) if(grid[i][3-i] != 'O' && grid[i][3-i] != 'T') win = false;
		if(win) {
			cout<<"Case #"<<test+1<<": O won\n";
			continue;
		}
		win = true;
		fo(i,4) if(grid[i][3-i] != 'X' && grid[i][3-i] != 'T') win = false;
		if(win) {
			cout<<"Case #"<<test+1<<": X won\n";
			continue;
		}
		win = true;
		fo(i,4) fo(j,4) if(grid[i][j]=='.') win = false;
		if(win) cout<<"Case #"<<test+1<<": Draw\n";
		else cout<<"Case #"<<test+1<<": Game has not completed\n";
	}
}
