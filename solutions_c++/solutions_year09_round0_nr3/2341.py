#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int tests;

#define H 100
#define W 100
#define INFTY 20000

int h,w;
int level[H+2][W+2];
char map[H+2][W+2];

void read_test(){
	cin >> h >> w;
	for(int x=1; x <= h; x++)
	for(int y=1; y <= w; y++)
		cin >> level[x][y];
	for(int x=0; x <= h+1; x++){
		level[x][0] = INFTY;
		level[x][w+1] = INFTY;
	}
	for(int y=0; y <= w+1; y++){
		level[0][y] = INFTY;
		level[h+1][y] = INFTY;
	}
}

int dx[5] = {-1,0,1,0,0};
int dy[5] = {0,-1,0,1,0};

vector<pair<int,int> > stack;

void solve_test(){
	stack.reserve(10000);
	for(int x=1; x <= h; x++)
	for(int y=1; y <= w; y++)
		map[x][y] = 0;
	char c = 'a';
	for(int _x=1; _x <= h; _x++)
	for(int _y=1; _y <= w; _y++)
	if (map[_x][_y] == 0){
		stack.clear();
		int x = _x, y= _y;
		int lowest_dir, lowest_val;
		do{
			stack.push_back(make_pair(x,y));
			lowest_dir = 4; lowest_val=level[x][y];
			for(int dir = 0; dir < 4; dir++)
				if (level[x+dx[dir]][y+dy[dir]] < lowest_val){
					lowest_val = level[x+dx[dir]][y+dy[dir]];
					lowest_dir = dir;
				}
			x = x + dx[lowest_dir];
			y = y + dy[lowest_dir];
		}while ( lowest_dir != 4 && map[x][y] == 0);
		if (map[x][y] == 0){
			map[x][y] = c++;
		}
		for(int i=0; i < stack.size(); i++)
			map[stack[i].first][stack[i].second] = map[x][y];
	}
}

void dump_sol(int i){
	cout << "Case #" << i << ":" << endl;
	for(int x=1; x <= h; x++)
	for(int y=1; y <= w; y++){
		cout << map[x][y];
		if (y == w)
			cout << endl;
		else 
			cout << " ";
	}
}

int main(){
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
		solve_test();
		dump_sol(i+1);
	}
}
