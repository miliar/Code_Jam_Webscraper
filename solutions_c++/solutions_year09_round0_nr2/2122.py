#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

#define DIM 105
#define MAXALT 11111

int map[DIM][DIM];
char ans[DIM][DIM];
char current;
int H, W;

int lowest(int i, int j, int &m, int &n){
	int l = map[i][j];
	m = i; n = j;
	if(l > map[i - 1][j]){
		l = map[i - 1][j];
		m = i - 1; n = j;
	}
	if(l > map[i][j - 1]){
		l = map[i][j - 1];
		m = i; n = j - 1;
	}
	if(l > map[i][j + 1]){
		l = map[i][j + 1];
		m = i; n = j + 1;
	}
	if(l > map[i + 1][j]){
		l = map[i + 1][j];
		m = i + 1; n = j;
	}
	return l;
}

char go(int i, int j){
	if(i == 0 || i > H || j == 0 || j > W )
		return 0;

	if(ans[i][j] != 0)
		return ans[i][j];

	int m, n;
	lowest(i, j, m, n);
	if(i == m && j == n)
		ans[i][j] = current++;
	else
		ans[i][j] = go(m, n);

	return ans[i][j];
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w", stdout);

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		for(int i = 0; i < DIM; i++)
			for(int j = 0; j < DIM; j++){
				map[i][j] = MAXALT;
				ans[i][j] = 0;
			}

		cin >> H >> W;
		for(int i = 1; i <= H; i++)
			for(int j = 1; j <= W; j++)
				cin >> map[i][j];

		current = 'a';
		for(int i = 1; i <= H; i++)
			for(int j = 1; j <= W; j++)
				go(i, j);

		cout << "Case #" << t << ":" << endl;
		for(int i = 1; i <= H; i++){
			for(int j = 1; j <= W; j++){
				if(j > 1)
					cout << ' ';
				cout << ans[i][j];
			}
			cout << endl;
		}
	}

	return 0;
}