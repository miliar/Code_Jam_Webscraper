#include <cstdio>
#include <iostream>
using namespace std;

int t, x0, y0, p = 0, tt;
char a[5][5];

bool check(char c){
	a[x0][y0] = c;
	for (int i = 0; i < 4; i++){
		int kol = 0;
		for (int j = 0; j < 4; j++) if (a[i][j] == c) kol++;
		if (kol == 4) return true;
	}
	for (int i = 0; i < 4; i++){
		int kol = 0;
		for (int j = 0; j < 4; j++) if (a[j][i] == c) kol++;
		if (kol == 4) return true;
	}
	int x, y, kol;
	x = 0;
	y = 0;
	kol = 0;
	for (int i = 0; i < 4; i++){
		if (a[x][y] == c) kol++;
		x++; y++;
	}
	if (kol == 4) return true;
	x = 0;
	y = 3;
	kol = 0;
	for (int i = 0; i < 4; i++){
		if (a[x][y] == c) kol++;
		x++; y--;
	}
	if (kol == 4) return true;
	return false;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout); 
	scanf("%d", &t);
	tt = t;
	while (t > 0){
		t--; p = 0;
		x0 = 4; y0 = 4;
		for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++){
			cin >> a[i][j];
			if (a[i][j] == 'T'){
				x0 = i;
				y0 = j;
			}
			if (a[i][j] == '.') p++;
		}
		if (check('X')){
			cout << "Case #" << tt - t << ": X won" << endl;
		} else if (check('O')){
			cout << "Case #" << tt - t << ": O won" << endl;
		} else if (p == 0){
			cout << "Case #" << tt - t << ": Draw" << endl;
		} else{
			cout << "Case #" << tt - t << ": Game has not completed" << endl;
		}
	}
	return 0;
}