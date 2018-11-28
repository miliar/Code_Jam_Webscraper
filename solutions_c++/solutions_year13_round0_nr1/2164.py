#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <ctime>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cassert>
#include <iostream>

using namespace std;

const double eps = 1e-9;
const int inf = 1e9 + 23;

const int size = 1000;

const int N = 4;

char maze[N][N];

bool check (char x){
	for (int i = 0; i < N; i++){
		bool flag = true;
		for (int j = 0; j < N; j++)
			if (maze[i][j] != x && maze[i][j] != 'T')
				flag = false;
		if (flag)
			return true;
	}
	for (int i = 0; i < N; i++){
		bool flag = true;
		for (int j = 0; j < N; j++)
			if (maze[j][i] != x && maze[j][i] != 'T')
				flag = false;
		if (flag)
			return true;
	}
	bool flag = true;
	for (int i = 0; i < N; i++)
		if (maze[i][i] != x && maze[i][i] != 'T')
			flag = false;
	if (flag)
		return true;
	flag = true;
	for (int i = 0; i < N; i++)
		if (maze[i][N - 1 - i] != x && maze[i][N - 1 - i] != 'T')
			flag = false;
	if (flag)
		return true;
}

void winer (){
	if (check('X')){
		cout << "X won" << endl;
		return;
	}
	if (check('O')){
		cout << "O won" << endl;
		return;
	}
	bool flag = true;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			if (maze[i][j] == '.')
				flag = false;
	if (!flag)
		cout << "Game has not completed" << endl;
	else
		cout << "Draw" << endl;
	return;
}

int main (void){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;

	cin >> n;
	for (int it = 1; it <= n; it++){
		cout << "Case #" << it << ":" << ' ';
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				scanf(" %c", &maze[i][j]);
		winer();
	}

	return 0;
}