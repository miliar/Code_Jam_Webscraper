#include <array>
#include <iostream>

using namespace std;

char checkDraw(const array<array<char,4>,4>&);
char checkRows(const array<array<char,4>,4>& , char);
char checkCols(const array<array<char,4>,4>& , char);
char checkDias(const array<array<char,4>,4>& , char);


int main(void){
	int testCases, TestNumber;
	cin >> testCases;
	TestNumber = testCases;
	while(testCases--){
		string line;
		array<array<char,4>,4> lGrid;
		for(int i = 0; i < 4; i++){
			cin >> line;
			lGrid[i][0] = line[0];
			lGrid[i][1] = line[1];
			lGrid[i][2] = line[2];
			lGrid[i][3] = line[3];
		}
		if(checkRows(lGrid, 'X')){
			cout << "Case #" << TestNumber - testCases << ": X won" << endl;
			continue;
		}
		if(checkRows(lGrid, 'O')){
			cout << "Case #" << TestNumber - testCases << ": O won" << endl;
			continue;
		}
		if(checkCols(lGrid, 'X')){
			cout << "Case #" << TestNumber - testCases << ": X won" << endl;
			continue;
		}
		if(checkCols(lGrid, 'O')){
			cout << "Case #" << TestNumber - testCases << ": O won" << endl;
			continue;
		}
		if(checkDias(lGrid, 'X')){
			cout << "Case #" << TestNumber - testCases << ": X won" << endl;
			continue;
		}
		if(checkDias(lGrid, 'O')){
			cout << "Case #" << TestNumber - testCases << ": O won" << endl;
			continue;
		}
		if(checkDraw(lGrid)){
			cout << "Case #" << TestNumber - testCases << ": Draw" << endl;
		}
		else{
			cout << "Case #" << TestNumber - testCases << ": Game has not completed" << endl;
		}
	}
}

char checkRows(const array<array<char,4>,4>& pGrid, char c){
	for(int i = 0; i < 4; i++){
		if( pGrid[i][0] == c  || pGrid[i][0] == 'T')
			if( pGrid[i][1] == c  || pGrid[i][1] == 'T')
				if( pGrid[i][2] == c  || pGrid[i][2] == 'T')
					if( pGrid[i][3] == c  || pGrid[i][3] == 'T')
						return true;
	}
	return false;
}

char checkCols(const array<array<char,4>,4>& pGrid, char c){
	for(int i = 0; i < 4; i++){
		if( pGrid[0][i] == c  || pGrid[0][i] == 'T')
			if( pGrid[1][i] == c  || pGrid[1][i] == 'T')
				if( pGrid[2][i] == c  || pGrid[2][i] == 'T')
					if( pGrid[3][i] == c  || pGrid[3][i] == 'T')
						return true;
	}
	return false;
}

char checkDias(const array<array<char,4>,4>& pGrid, char c){
	if(pGrid[0][0] == c  || pGrid[0][0] == 'T')
		if(pGrid[1][1] == c  || pGrid[1][1] == 'T')
			if(pGrid[2][2] == c  || pGrid[2][2] == 'T')
				if(pGrid[3][3] == c  || pGrid[3][3] == 'T')
					return true;
	if(pGrid[0][3] == c  || pGrid[0][3] == 'T')
		if(pGrid[1][2] == c  || pGrid[1][2] == 'T')
			if(pGrid[2][1] == c  || pGrid[2][1] == 'T')
				if(pGrid[3][0] == c  || pGrid[3][0] == 'T')
					return true;
	return false;
}

char checkDraw(const array<array<char,4>,4>& pGrid){
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(pGrid[i][j] == '.'){
				return false;
			}
		}
	}
	return true;
}