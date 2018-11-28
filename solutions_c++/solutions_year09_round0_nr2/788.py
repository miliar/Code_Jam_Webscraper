#include <stdio.h>
#include <iostream>
using namespace std;

#define m0 110

const int dx[] = { 0, -1, 1, 0};
const int dy[] = {-1,  0, 0, 1};

int map[m0][m0];
char ans[m0][m0];
int dest[m0][m0];
int dir[m0][m0];
int w, h;

bool valid(int y, int x){
	if (x < 0 || x >= w) return(false);
	if (y < 0 || y >= h) return(false);
	return(true);
}

void init(){
	int i, j;

	cin >> h >> w;
	for (i = 0; i < h; i++){
		for (j = 0; j < w; j++){
			cin >> map[i][j];
			ans[i][j] = ' ';
			dest[i][j] = -1;
		}
	}
}

void calcdir(){
	int i, j, k, p;

	for (i = 0; i < h; i++){
		for (j = 0; j < w; j++){
			p = -1; 

			for (k = 0; k < 4; k++){
				int ii = i + dy[k];
				int jj = j + dx[k];

				if (!valid(ii, jj) || map[ii][jj] >= map[i][j]) continue;

				if (p == -1 || map[ii][jj] < map[i + dy[p]][j + dx[p]]) p = k;
			}

			dir[i][j] = p;
		}
	}
}

int solve(int i, int j){
	if (dest[i][j] != -1){
		return(dest[i][j]);
	}

	if (dir[i][j] == -1){
		dest[i][j] = i * w + j;
		return(dest[i][j]);
	}

	int ii = i + dy[dir[i][j]];
	int jj = j + dx[dir[i][j]];

	dest[i][j] = solve(ii, jj);
	return(dest[i][j]);
}

void update(char ch, int des){
	int i, j;
	for (i = 0; i < h; i++){
		for (j = 0; j < w; j++){
			if (dest[i][j] == des) 
				ans[i][j] = ch;
		}
	}
}

void calc(){
	int i, j;
	char ch = 'a' - 1;

	calcdir();

	for (i = 0; i < h; i++){
		for (j = 0; j < w; j++){
			dest[i][j] = solve(i, j);
		}
	}

	for (i = 0; i < h; i++){
		for (j = 0; j < w; j++){
//			if (dir[i][j] == -1){
				if (ans[i][j] == ' '){
					ch++;
					update(ch, dest[i][j]);
				}
//			}
		}
	}
}

void print(){
	int i, j;
	for (i = 0; i < h; i++){
		for (j = 0; j < w; j++){
			if (j > 0) cout << ' ';
			cout << ans[i][j];
		}
		cout << endl;
	}
}


int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int i, t;

	cin >> t;
	for (i = 1; i <= t; i++){
		init();
		printf("Case #%d: \n", i);
		calc();
		print();
	}


	return 0;
}