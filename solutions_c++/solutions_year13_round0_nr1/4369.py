#include <iostream>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <math.h>
#include <stack>
#include <queue>
#include <list>

#pragma comment(linker, "/STACK:167772160")

using namespace std;
string s[5];
int f(){
	string x[5];
	for(int i=0; i<4; i++)
		x[i] = s[i];
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			if(x[i][j] == 'T') x[i][j] = 'X';

	if((x[0][0] == x[1][1]) && (x[0][0] == x[2][2]) && (x[0][0] == x[3][3]) &&(x[0][0] == 'X')) return 1;
	if((x[0][3] == x[1][2]) && (x[0][3] == x[2][1]) && (x[0][3] == x[3][0]) &&(x[0][3] == 'X')) return 1;
	for(int i=0; i<4; i++){
		bool ok = 1;
		for(int j=0; j<4; j++)
			if(x[i][j] != 'X') ok = 0;
		if(ok) return 1;
	}
	for(int i=0; i<4; i++){
		bool ok = 1;
		for(int j=0; j<4; j++)
			if(x[j][i] != 'X') ok = 0;
		if(ok) return 1;
	}
///////////////////////////////////////////
	for(int i=0; i<4; i++)
		x[i] = s[i];
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			if(x[i][j] == 'T') x[i][j] = 'O';

	if((x[0][0] == x[1][1]) && (x[0][0] == x[2][2]) && (x[0][0] == x[3][3]) &&(x[0][0] == 'O')) return 2;
	if((x[0][3] == x[1][2]) && (x[0][3] == x[2][1]) && (x[0][3] == x[3][0]) &&(x[0][3] == 'O')) return 2;
	for(int i=0; i<4; i++){
		bool ok = 1;
		for(int j=0; j<4; j++)
			if(x[i][j] != 'O') ok = 0;
		if(ok) return 2;
	}
	for(int i=0; i<4; i++){
		bool ok = 1;
		for(int j=0; j<4; j++)
			if(x[j][i] != 'O') ok = 0;
		if(ok) return 2;
	}
/////
	bool ok = 0;
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			if(x[i][j] == '.') return 3;
	return 4;
}
int main(){
    ifstream cin("out.txt");
	ofstream cout("A_small.txt");
	int T;
	cin >> T;
	int cnt = 0;
	for(int k=0; k<T; k++){
		cnt++;
		cout << "Case #" << cnt << ": ";
		string empty;
		for(int i=0; i<4; i++) cin >> s[i];
//		for(int i=0; i<4; i++) cout << s[i] << endl;
//		cout << endl;
		int ans = f();
		if(ans == 1) cout << "X won\n"; else
			if(ans == 2) cout << "O won\n"; else
				if(ans == 3) cout << "Game has not completed\n"; else
					cout << "Draw\n";
//		cin >> empty;
		cin.get();
	}
	cin.close();
	return 0;
}




