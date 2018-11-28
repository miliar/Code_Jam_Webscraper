#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;

bool f,comp;
bool ff;
char ans;
char c[5][5];

void check1(int i){
	ff = true;
	for (int j = 1; j < 4; j++){
		if ((c[i][j] != c[i][0]) && (c[i][j] != 'T')){
			ff = false;
			break;
		}
	}
	if (ff){
		f = true;
		ans = c[i][0];
	}
}

void check2(int j){
	ff = true;
	for (int i = 1; i < 4; i++){
		if ((c[i][j] != c[0][j]) && (c[i][j] != 'T')){
			ff = false;
			break;
		}
	}
	if (ff){
		f = true;
		ans = c[0][j];
	}
}

void check3(){
	ff = true;
	for (int i = 1; i < 4; i++){
		if ((c[i][i] != c[0][0]) && (c[i][i] != 'T')){
			ff = false;
			break;
		}
	}
	if (ff){
		f = true;
		ans = c[0][0];
	}
}

void check4(){
	ff = true;
	for (int i = 1; i < 4; i++){
		if ((c[i][3 - i] != c[0][3]) && (c[i][3 - i] != 'T')){
			ff = false;
			break;
		}
	}
	if (ff){
		f = true;
		ans = c[0][3];
	}
}

int main(){
	
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++){
		cin >> c[0];
		cin >> c[1];
		cin >> c[2];
		cin >> c[3];
		printf("Case #%d: ", z); 
		f = false;
		comp = true; // zuihouzaipan
		for (int i = 0;i < 4; i++){
			if (f) break;
			if (c[i][0] != '.'){
				if (c[i][0] == 'T'){
					c[i][0] = 'X';
					check1(i);
					if (f) break;
					c[i][0] = 'O';
					check1(i);
					c[i][0] = 'T';
				}
				else check1(i);
			}
		}
		for (int j = 0;j < 4; j++){
			if (f) break;
			if (c[0][j] != '.'){
				if (c[0][j] == 'T'){
					c[0][j] = 'X';
					check2(j);
					if (f) break;
					c[0][j] = 'O';
					check2(j);
					c[0][j] = 'T';
				}
				else check2(j);
			}
		}

		if (!(f)){
			if (c[0][0] != '.'){
				if (c[0][0] == 'T'){
					c[0][0] = 'X';
					check3();
					if (!(f)){
						c[0][0] = 'O';
						check3();
					}
					c[0][0] = 'T';
				}
				else{
					check3();
				}
			}
		}

		if (!(f)){
			if (c[0][3] != '.'){
				if (c[0][3] == 'T'){
					c[0][3] = 'X';
					check4();
					if (!(f)){
						c[0][3] = 'O';
						check4();
					}
					c[0][3] = 'T';
				}
				else{
					check4();
				}
			}
		}
		
		if (f){
			printf("%c won\n", ans);
		}
		else{
			for (int i = 0; i < 4; i++){
				for (int j = 0; j < 4; j++){
					if (c[i][j] == '.'){
						comp = false;
						break;
					}
				}
				if (! comp) break;
			}
			if (comp){
				printf("Draw\n");
			}
			else{
				printf("Game has not completed\n");
			}
		}

	}

	return 0;
	
}
