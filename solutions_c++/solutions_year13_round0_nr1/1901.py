#include <iostream>
#include <vector>

using namespace std;

bool row(int row, vector<string> &t, char c){
	for(int i=0; i<4; i++) if( t[row][i] != c && t[row][i] != 'T' ) return false;
	return true;
}

bool col(int col, vector<string> &t, char c){
	for(int i=0; i<4; i++) if( t[i][col] != c && t[i][col] != 'T' ) return false;
	return true;
}

bool diag1(vector<string> &t, char c){
	for(int i=0; i<4; i++) if( t[i][i] != c && t[i][i] != 'T' ) return false;
	return true;
}

bool diag2(vector<string> &t, char c){
	for(int i=0; i<4; i++) if( t[i][3-i] != c && t[i][3-i] != 'T' ) return false;
	return true;
}

string go(vector<string> &t){
	if( diag1(t, 'O') || diag2(t, 'O') ) return "O won";
	if( diag1(t, 'X') || diag2(t, 'X') ) return "X won";
	for(int i=0; i<4; i++){
		if( row(i, t, 'O') || col(i, t, 'O') ) return "O won";
		if( row(i, t, 'X') || col(i, t, 'X') ) return "X won";
	}

	bool sthEmpty = false;
	for(int i=0; i<4; i++) for(int j=0; j<4; j++){
		 if( t[i][j] == '.' ) sthEmpty = true;
	}

	if( sthEmpty ){
		return "Game has not completed";
	} else {
		return "Draw";
	}
}

int ileTestow;

int main(){

	scanf("%d", &ileTestow);

	for(int q=1; q<=ileTestow; q++){
		string tmp;
		vector<string> t;

		for(int a=0; a<4; a++){
			cin >> tmp;
			t.push_back(tmp);
		}
		
		cout << "Case #" << q << ": " << go(t) << endl;
	}
	
	return 0;
}
