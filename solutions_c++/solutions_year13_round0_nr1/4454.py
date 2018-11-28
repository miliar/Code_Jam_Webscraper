#include<cstdio>
#include<iostream>
#include<string>
using namespace std;

char b[4][4];

// Return: 0 if O win, 1 if X win, 2 if draw, 3 if incomplete.
int solve(){
	int ecnt = 0;
	int tr = -1, tc = -2;

	for(int i = 0; i < 4; i++){
		string line;
		getline(cin, line);
		for(int j = 0; j < 4; j++){
			b[i][j] = line[j];
			if(line[j] == '.') ecnt++;
			else if(line[j] == 'T') tr = i, tc = j;
		}
	}

	//Check rows
	for(int i = 0; i < 4; i++){
		int no = 0, nx = 0;
		for(int j = 0; j < 4; j++){
			if(b[i][j] == '.') break;
			else if(b[i][j] == 'O') no++;
			else if(b[i][j] == 'X') nx++;
		}
		if((no == 3 && tr == i) || no == 4) return 0;
		else if((nx == 3 && tr == i) || nx == 4) return 1;
	}

	//Check cols
	for(int j = 0; j < 4; j++){
		int no = 0, nx = 0;
		for(int i = 0; i < 4; i++){
			if(b[i][j] == '.') break;
			else if(b[i][j] == 'O') no++;
			else if(b[i][j] == 'X') nx++;
		}
		if((no == 3 && tc == j) || no == 4) return 0;
		else if((nx == 3 && tc == j) || nx == 4) return 1;
	}

	//Check diags
	int no = 0, nx = 0;
	for(int i = 0; i < 4; i++){
		if(b[i][i] == '.') break;
		else if(b[i][i] == 'O') no++;
		else if(b[i][i] == 'X') nx++;
	}
	if(no == 4 || (no == 3 && tr == tc)) return 0;
	else if(nx == 4 || (nx == 3 && tr == tc)) return 1;

	no = nx = 0;
	for(int i = 0; i < 4; i++){
		if(b[i][3-i] == '.') break;
		else if(b[i][3-i] == 'O') no++;
		else if(b[i][3-i] == 'X') nx++;
	}
	if(no == 4 || (no == 3 && tr+tc == 3)) return 0;
	else if(nx == 4 || (nx == 3 && tr+tc == 3)) return 1;

	//If neither X nor O win, then if no empty cell --> draw, otherwise --> incomplete
	if(ecnt == 0) return 2;
	else return 3;
}

void answer(int n, int t){
	cout << "Case #" << t << ": ";
	if(n == 0) cout << "O won";
	else if(n == 1) cout << "X won";
	else if(n == 2) cout << "Draw";
	else if(n == 3) cout << "Game has not completed";
	else cerr << "Invalid!";
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	cin.ignore();
	for(int t = 1; t <= T; ++t){
		int ret = solve();
		answer(ret, t);
		if(t < T) cout << "\n";
		cin.ignore();
	}
	return 0;
}
