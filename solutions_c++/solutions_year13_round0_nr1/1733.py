#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <string> 
#include <iomanip> 
#include <cstdio> 
#include <cctype> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <cstring> 

using namespace std; 

#define PI 3.141592653589793238 
#define _e 2.71828183 
#define EPS 0.0000000001 
#define INF 1999888777 

#define pb push_back 
#define MSG(a) cout << #a << " = " << a << endl; 
#define is_digit(c) ('0' <= (c) && (c) <= '9') 

typedef vector <int> VI; 
typedef vector <string> VS; 
typedef vector <double> VD; 

#define DRAW 0
#define O 1
#define X 2

#define ROW 0
#define COL 1

char a[5][5];

FILE *fin;
FILE *fout; 

bool checkOver(){
	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++){
			if (a[i][j] == '.') return false;
		}
	}
	return true;
}

void output(int ans){
	if (ans == O) fprintf(fout, "O won\n");
	else if (ans == X) fprintf(fout, "X won\n");
	else fprintf(fout, "Draw\n");
}

bool f(int i, int j, char c){
	if (a[i][j] == 'T') return true;
	return c == a[i][j];
}

int win(int idx, int type){
	int x = 0, o = 0;
	for (int i = 0; i < 4; i++){
		if (type == ROW){
			x += f(idx, i, 'X');
			o += f(idx, i, 'O');
		}
		else if (type == COL){
			x += f(i, idx, 'X');
			o += f(i, idx, 'O');
		}
	}

	if (x == 4) return X;
	else if (o == 4) return O;
	else return DRAW;
}

int winD(int type){
	int x = 0, o = 0;

	for (int i = 0; i < 4; i++){
		if (type == 0){
			x += f(i, i,'X');
			o += f(i, i, 'O');
		}
		else if (type == 1){
			x += f(3 - i, i, 'X');
			o += f(3 - i, i, 'O');
		}
	}

	if (x == 4) return X;
	else if (o == 4) return O;
	else return DRAW;
}

int main(){
	fin = fopen("XO.in", "r");
	fout = fopen("XO.out", "w");

	int t;
	fscanf(fin, "%d", &t);

	for (int test = 1; test <= t; test++){
		for (int i = 0; i < 4; i++){
			fscanf(fin, "%s", a[i]);
		}

		fprintf(fout, "Case #%d: ", test);

		{
			int ansRow = DRAW, ansCol = DRAW;
			for (int i = 0; i < 4; i++){
				int tmp = win(i, ROW);
				if (tmp != DRAW) ansRow = tmp;
				tmp = win(i, COL);
				if (tmp != DRAW) ansCol = tmp;
			}
			int ansD1 = winD(0);
			int ansD2 = winD(1);
				
			if (ansRow != DRAW) output(ansRow);
			else if (ansCol != DRAW) output(ansCol);
			else if (ansD1 != DRAW) output(ansD1);
			else if (ansD2 != DRAW) output(ansD2);
			else if (checkOver()) output(DRAW);
			else fprintf(fout, "Game has not completed\n");
		}
	}
	
	fclose(fin);
	fclose(fout);

//	system("pause");
	return 0;
}