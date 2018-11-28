#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int a[4][4];

void reset(){
	for(int i=0; i<4;i++)
		for(int j=0;j<4;j++)
			a[i][j];
}


int main(){
	int tests;
	cin >> tests;
	int i = tests;
	loop:
	if(i==0) return 0;
	i--;
		
		int isDraw=0;

		//reset
		reset();

		//input in matrix
		for(int j=0; j<4; j++) {
			for(int k=0; k<4; k++) {
				char m;
				cin >> m;
				if(m == '.') {
					isDraw++;
				}
				a[j][k] = m;
			}
		}

		//check horizontally 
		for(int j=0; j<4; j++) {
			int counterX = 0;
			int counterO = 0;
			for( int k=0; k<4; k++) {
				int temp = a[j][k];
				if(temp=='X') {
					counterX++;
				}else if(temp=='O') {
					counterO++;
				}else if(temp=='T'){
					counterX++;
					counterO++;
				}
			}
			if(counterX == 4) {
				cout << "Case #" << (tests-i) << ": X won" << endl;
				goto loop;
			}else if(counterO == 4) {
				cout << "Case #" << (tests-i) << ": O won" << endl;
				goto loop;
			}
		}

		//check vertically
		for(int j=0; j<4; j++) {
			int counterX = 0;
			int counterO = 0;
			for( int k=0; k<4; k++) {
				int temp = a[k][j];
				if(temp=='X') {
					counterX++;
				}else if(temp=='O') {
					counterO++;
				}else if(temp=='T'){
					counterX++;
					counterO++;
				}
			}
			if(counterX == 4) {
				cout << "Case #" << (tests-i) << ": X won" << endl;
				goto loop;
			}else if(counterO == 4) {
				cout << "Case #" << (tests-i) << ": O won" << endl;
				goto loop;
			}
		}

		//check left diagonal
		int counterX = 0;
		int counterO = 0;
		for(int j=0; j<4; j++) {
			int temp = a[j][j];
			if(temp=='X') {
				counterX++;
			}else if(temp=='O') {
				counterO++;
			}else if(temp=='T'){
				counterX++;
				counterO++;
			}
		}
		if(counterX == 4) {
			cout << "Case #" << (tests-i) << ": X won" << endl;
			goto loop;
		}else if(counterO == 4) {
			cout << "Case #" << (tests-i) << ": O won" << endl;
			goto loop;
		}

		//check right diagonal
		counterX = 0;
		counterO = 0;
		for(int j=0; j<4; j++) {
			int temp = a[3-j][j];
			if(temp=='X') {
				counterX++;
			}else if(temp=='O') {
				counterO++;
			}else if(temp=='T'){
				counterX++;
				counterO++;
			}
		}
		if(counterX == 4) {
			cout << "Case #" << (tests-i) << ": X won" << endl;
			goto loop;
		}else if(counterO == 4) {
			cout << "Case #" << (tests-i) << ": O won" << endl;
			goto loop;
		}

		if(isDraw == 0) {
			cout << "Case #" << (tests-i) << ": Draw" << endl;
		}else{
			cout << "Case #" << (tests-i) << ": Game has not completed" << endl;
		}

 		goto loop;
	return 0;
}