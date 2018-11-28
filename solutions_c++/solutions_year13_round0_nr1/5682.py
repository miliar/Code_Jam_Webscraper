#include <iostream>
using namespace std;

bool isEqual(char a, char b){
	if((a == b) && a!='.') return true;
	else if((a!='.' && b=='T') || (a == 'T') && (b != '.'))
		return true;
	else{
		return false;
	}
}

char winnerFound(char a, char b, char c, char d){
	if(isEqual(a, b) && isEqual(b, c) && isEqual(c, d)){
		if(a == 'X') return 'X';
		if(a == 'O') return 'O';
	}
	else{
		return 'N';
	}

}

void solve(int test){
	char b[4][4];
	int completed = true;
	char winner = 'N';
	for(int i=0; i<4; i++){
		cin >> b[i][0] >> b[i][1] >> b[i][2] >> b[i][3];
		//cout << b[i][0] << b[i][1] << b[i][2] << b[i][3] << endl;
		if(b[i][0] == '.'|| b[i][1] == '.' || b[i][2] == '.' || b[i][3] == '.'){
			completed = false;
		}
	}

	for(int i=0; i<4; i++){
		winner = winnerFound(b[i][0], b[i][1], b[i][2], b[i][3]);
		if(winner == 'X' || winner == 'O'){
			cout << "Case #" << test << ": " << winner << " won" << endl;
			return;
		}
	} 

	for(int i=0; i<4; i++){
		winner = winnerFound(b[0][i], b[1][i], b[2][i], b[3][i]);
		if(winner == 'X' || winner == 'O'){
			cout << "Case #" << test << ": " << winner << " won" << endl;
			return;
		}
	}
	winner = winnerFound(b[0][0], b[1][1], b[2][2], b[3][3]);
	if(winner == 'X' || winner == 'O'){
			cout << "Case #" << test << ": " << winner << " won" << endl;
			return;
	}
	winner = winnerFound(b[0][3], b[1][2], b[2][1], b[3][0]);
	if(winner == 'X' || winner == 'O'){
			cout << "Case #" << test << ": " << winner << " won" << endl;
			return;
	}

	if(completed){
		cout << "Case #" << test << ": " << "Draw" <<  endl;
		return;
	}
	else{
		cout << "Case #" << test << ": " << "Game has not completed" << endl;
	}
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests = 0;
	scanf("%d", &tests);
	for(int i=1; i <= tests; ++i){
		solve(i);
	}
}