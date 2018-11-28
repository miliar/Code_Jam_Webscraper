#include <cstdio>
#include <iostream>
using namespace std;

char m[4][4];

bool check(char c, int idxt, int idyt){
	if(idxt >= 0){
		m[idxt][idyt] = c;
	}

	bool win = false;

	int cntx = 0;
	int cnty = 0;
	for(int i = 0; i < 4; i++){
        cntx = cnty = 0;
		for(int j = 0; j < 4; j++){
			if(c == m[i][j]){
				cntx++;
			}
			if(c == m[j][i]){
				cnty++;
			}
		}
		if(cntx == 4 || cnty == 4)
		  win = true;
	}


	cntx = 0;
	cnty = 0;
	for(int i = 0; i < 4; i++){
		if(c == m[i][i])
			cntx++;
		if(c == m[i][3-i])
			cnty++;
	}
	if(cntx == 4 || cnty == 4)
		win = true;

	if(idxt >= 0){
		m[idxt][idyt] = 'T';
	}

	return win;
}

int main(){
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int cases = 1; cases <= t; cases++){
		int c;
		cout << "Case #" << cases << ": ";
		getchar();
		int cnt = 0;
		int idxt = -1;
		int idyt = -1;
		for(int i = 0; i < 4; i++){
			int j = 0;
			while((c = getchar()) != '\n'){
				m[i][j] = c;
				if(c != '.')
					cnt++;
				if(c == 'T'){
					idxt = i;
					idyt = j;
				}
				j++;
			}
		}

		if(check('X', idxt, idyt)){
			cout << "X won";
		}
		else if(check('O', idxt, idyt)){
			cout << "O won";
		}
		else if(cnt == 16){
			cout << "Draw";
		}
		else
			cout << "Game has not completed";
		cout << endl;
	}
	return 0;
}
