#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int T;
int A[4][4];
string s;
bool draw;

bool ch(int p, int r){
	for(int i=0;i<4;i++){
		if(A[r][i]!=p && A[r][i]) return false;
	}
	return true;
}

bool cv(int p, int c){
	for(int i=0;i<4;i++){
		if(A[i][c]!=p && A[i][c]) return false;
	}
	return true;
}

bool cd1(int p){
	for(int i=0;i<4;i++){
		if(A[i][i]!=p && A[i][i]) return false;
	}
	return true;
}

bool cd2(int p){
	for(int i=0;i<4;i++){
		if(A[i][3-i]!=p && A[i][3-i]) return false;
	}
	return true;
}

bool check(int p){
	if(cd1(p)) return true;
	if(cd2(p)) return true;
	for(int i=0;i<4;i++){
		if(cv(p,i)) return true;
		if(ch(p,i)) return true;
	}
	return false;
}




int main(){

	cin >> T;
	for(int cas=1;cas<=T;cas++){

		draw = true;
		cout << "Case #" << cas << ":";
		for(int i=0;i<4;i++){
			cin >> s;
			for(int j=0;j<4;j++){
				switch(s[j]){
					case 'X': A[i][j] = 1; break;
					case 'O': A[i][j] = 2; break;
					case 'T': A[i][j] = 0; break;
					case '.': A[i][j] = 3; draw = false; break;
				}
			}
		}
		if(check(1)) cout << " X won" << endl;
		else if(check(2)) cout << " O won" << endl;		
		else if(draw) cout << " Draw" << endl;
		else cout << " Game has not completed" << endl;
	}

	return 0;
} 
