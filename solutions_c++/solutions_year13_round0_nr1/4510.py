#include <iostream>
#include <string>
using namespace std;

char map[4][4];

string compute(){
	int x_won = 0;
	int o_won = 0;

	int x_c = 0, o_c = 0, t_c = 0;
	int _dot = 0;

	for (int i = 0 ; i < 4 ; i ++)
		for (int j = 0 ; j < 4 ; j++)
			if (map[i][j]=='.') _dot++;
		
	for (int i = 0 ; i < 4 ; i ++){
		x_c = 0; o_c = 0; t_c = 0;
		for (int j = 0 ; j < 4 ; j++){
			if (map[i][j]=='O') o_c++;
			if (map[i][j]=='X') x_c++;
			if (map[i][j]=='T') t_c++;
		}
		if (o_c == 4 || (o_c==3 && t_c==1)) o_won++;
		if (x_c == 4 || (x_c==3 && t_c==1)) x_won++;
	}

	for (int i = 0 ; i < 4 ; i ++){
		x_c = 0; o_c = 0; t_c = 0;
		for (int j = 0 ; j < 4 ; j++){
			if (map[j][i]=='O') o_c++;
			if (map[j][i]=='X') x_c++;
			if (map[j][i]=='T') t_c++;
		}
		if (o_c == 4 || (o_c==3 && t_c==1)) o_won++;
		if (x_c == 4 || (x_c==3 && t_c==1)) x_won++;
	}

	x_c = 0; o_c = 0; t_c = 0;
	for (int i = 0 ; i < 4 ; i ++){
		if (map[i][i]=='O') o_c++;
		if (map[i][i]=='X') x_c++;
		if (map[i][i]=='T') t_c++;
	}
	if (o_c == 4 || (o_c==3 && t_c==1)) o_won++;
	if (x_c == 4 || (x_c==3 && t_c==1)) x_won++;

	x_c = 0; o_c = 0; t_c = 0;
	for (int i = 0 ; i < 4 ; i ++){
		if (map[i][3-i]=='O') o_c++;
		if (map[i][3-i]=='X') x_c++;
		if (map[i][3-i]=='T') t_c++;
	}
	if (o_c == 4 || (o_c==3 && t_c==1)) o_won++;
	if (x_c == 4 || (x_c==3 && t_c==1)) x_won++;

	if (o_won < x_won) return "X won";
	if (o_won > x_won) return "O won";
	if (o_won == x_won && _dot == 0) 
		return "Draw";
	return "Game has not completed";
}

int main(){
	int n;
	cin >> n;

	for (int c = 1 ; c <= n ; c ++){
		for (int i = 0 ; i < 4 ; i ++){
			for (int j = 0 ; j < 4 ; j ++){
				cin >> map[i][j];
			}
		}

		cout << "Case #" <<c <<": " << compute() << endl;
	}


	return 0;
}