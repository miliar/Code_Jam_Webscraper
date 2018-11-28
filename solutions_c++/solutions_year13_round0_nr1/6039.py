#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

string g[4];

bool won(char ch){

	bool w = false;

	for(int i = 0; i < 4; i++){
		bool all_ch = true;
		for(int j = 0; j < 4; j++){
			if(g[i][j] == 'T') continue;
			if(g[i][j] != ch) all_ch= false;
		}

		w |= all_ch;
	}

	for(int i = 0; i < 4; i++){
		bool all_ch = true;
		for(int j = 0; j < 4; j++){
			if(g[j][i] == 'T') continue;
			if(g[j][i] != ch) all_ch= false;
		}

		w |= all_ch;
	}

	bool diagonal = true;
	for(int i = 0; i < 4; i++){
		if(g[i][i] == 'T') continue;
		if(g[i][i] != ch) diagonal = false;
	}

	w |= diagonal;

	diagonal = true;

	for(int i = 0; i < 4; i++){
		if(g[i][3-i] == 'T') continue;
		if(g[i][3-i] != ch) diagonal = false;
	}

	w |= diagonal;

	return w;
}


bool draw(){

	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(g[i][j] == '.') return false;
		}
	}

	return true;
}
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
	int T; cin >> T;
	for(int t = 1; t <= T; t++){
		for(int i = 0; i < 4; i++){
			cin >> g[i];
		}

		cout << "Case #" << t << ": " ;
		if(won('X')){
			cout << "X won";
		}else if(won('O')){
			cout << "O won";
		}else if(draw()){
			cout << "Draw";
		}else {
			cout << "Game has not completed";
		}
		cout << endl;
	}

	return 0;
}
