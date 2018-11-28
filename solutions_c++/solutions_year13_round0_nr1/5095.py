// Algorithm    :
// Order        :

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
#include <cmath>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <bitset>
#include <list>
#include <complex>
using namespace std;

#define ll long long
#define ld long double

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef complex<double> point;

#define X real()
#define Y imag()
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define L(s) (int)((s).size())
#define C(a,b) memset((a),(b),sizeof(a))
#define all(c) (c).begin(), (c).end()

#define INF (1e15)
#define EPS (1e-9)


vector<vii> win;
char board[4][4];
string out[4];
int non = 0;

void fill() {
	vii temp;
	temp.pb(ii(0,0));
	temp.pb(ii(0,1));
	temp.pb(ii(0,2));
	temp.pb(ii(0,3));
	win.pb(temp);
	
	temp.clear();
	temp.pb(ii(1,0));
	temp.pb(ii(1,1));
	temp.pb(ii(1,2));
	temp.pb(ii(1,3));
	win.pb(temp);
	
	temp.clear();
	temp.pb(ii(2,0));
	temp.pb(ii(2,1));
	temp.pb(ii(2,2));
	temp.pb(ii(2,3));
	win.pb(temp);
	
	temp.clear();
	temp.pb(ii(3,0));
	temp.pb(ii(3,1));
	temp.pb(ii(3,2));
	temp.pb(ii(3,3));
	win.pb(temp);
	
	temp.clear();
	temp.pb(ii(0,0));
	temp.pb(ii(1,0));
	temp.pb(ii(2,0));
	temp.pb(ii(3,0));
	win.pb(temp);
	
	temp.clear();
	temp.pb(ii(0,1));
	temp.pb(ii(1,1));
	temp.pb(ii(2,1));
	temp.pb(ii(3,1));
	win.pb(temp);
	
	temp.clear();
	temp.pb(ii(0,2));
	temp.pb(ii(1,2));
	temp.pb(ii(2,2));
	temp.pb(ii(3,2));
	win.pb(temp);
	
	temp.clear();
	temp.pb(ii(0,3));
	temp.pb(ii(1,3));
	temp.pb(ii(2,3));
	temp.pb(ii(3,3));
	win.pb(temp);
	
	temp.clear();
	temp.pb(ii(0,0));
	temp.pb(ii(1,1));
	temp.pb(ii(2,2));
	temp.pb(ii(3,3));
	win.pb(temp);
	
	temp.clear();
	temp.pb(ii(0,3));
	temp.pb(ii(1,2));
	temp.pb(ii(2,1));
	temp.pb(ii(3,0));
	win.pb(temp);
}

bool EQ(int i) {
	for(int j=0;j<4;j++)
		for(int l=j+1;l<4;l++)
			if(board[win[i][j].fi][win[i][j].se] != board[win[i][l].fi][win[i][l].se] && board[win[i][j].fi][win[i][j].se] != 'T' && board[win[i][l].fi][win[i][l].se] != 'T')
				return false;
	return true;
}

int winning() {
	for(int i=0;i<10;i++) {
		if(EQ(i)) {
			if(board[win[i][0].fi][win[i][0].se] == '.')
				continue;
			if(board[win[i][0].fi][win[i][0].se] == 'X')
				return 0;
			if(board[win[i][0].fi][win[i][0].se] == 'O')
				return 1;
			if(board[win[i][0].fi][win[i][0].se] == 'T') {
				if(board[win[i][3].fi][win[i][3].se] == 'X')
					return 0;
				if(board[win[i][3].fi][win[i][3].se] == 'O')
					return 1;
			}
		}
	}
	if(non == 16)
		return 2;
	return 3;
}

int main () {
	fill();
	out[0] = "X won";
	out[1] = "O won";
	out[2] = "Draw";
	out[3] = "Game has not completed";
	int _te;
	cin >> _te;
	for(int te=1; te<=_te; te++) {
		non = 0;
		for(int i=0;i<16;i++) {
			cin >> board[i/4][i%4];
			if(board[i/4][i%4] != '.')
				non++;
		}
		cout << "Case #" << te << ": " << out[winning()] << endl;
	}
	return 0;
}







