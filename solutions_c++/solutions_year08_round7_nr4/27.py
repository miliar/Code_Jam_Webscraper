#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>

using namespace std;

int R,C;
char board[20][20];

struct Position {
	int x, y;
	bool visited[6][6];
}
start;

int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

bool judge(Position& p) {
	for(int d=0; d<8; d++) {
		Position q;
		q.x = p.x + dx[d];
		q.y = p.y + dy[d];
		memcpy(q.visited, p.visited, sizeof(q.visited));
		q.visited[p.x][p.y] = true;
		if(board[q.x][q.y] != '#' && !p.visited[q.x][q.y] && !judge(q))
			return true;
	}
	return false;
}

int main(int argc, char* argv[]) {
	int n;
	cin >>n;
	for(int i=0; i<n; i++) {
		cin >>R >>C;
		memset(board, '#', sizeof(board));
		for(int x=1; x<=R; x++) {
			cin >>board[x]+1;
			board[x][C+1] = '#';
		}
		for(int x=0; x<=R+1; x++) {
			for(int y=0; y<=C+1; y++) {
				cerr <<board[x][y];
				if(board[x][y] == 'K') {
					start.x = x;
					start.y = y;
				}
			}
			cerr <<endl;
		}
		cout <<"Case #" <<i+1 <<": ";
		memset(start.visited, false, sizeof(start.visited));
		if(judge(start))
			cout <<"A" <<endl;
		else
			cout <<"B" <<endl;
	}
	return 0;
}