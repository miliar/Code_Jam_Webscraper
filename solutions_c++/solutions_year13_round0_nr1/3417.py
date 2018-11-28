//
//  ticktacktomek.cpp
//  
//
//  Created by Alex Sorafumo on 13/04/13.
//
//

#include <iostream>

using namespace std;

int main(){
	int numCases, casesTested = 0, status;
	int xCount, oCount;
	char grids[1001][4][4];
	cin >> numCases;
	cin.get();
		//Get all case information
	while(casesTested < numCases){
			//cout << "Case: " << casesTested + 1 << endl;
		for (int y = 0; y < 4; y++) {
			cin.getline(grids[casesTested][y], 5);
				//cout << grids[casesTested][y] << endl;
		}
		cin.get();
			//cout << endl;
		casesTested++;
	}
	casesTested = 0;
		//Output Case Results
	while(casesTested < numCases){
		status = 1;
		xCount = 0;
		oCount = 0;
			//Check vertical
		for (int y = 0; y < 4; y++) {
			xCount = 0;
			oCount = 0;
			for (int x = 0; x < 4; x++) {
				if(grids[casesTested][y][x] == 'O')
					oCount++;
				else if(grids[casesTested][y][x] == 'X')
					xCount++;
				else if(grids[casesTested][y][x] == 'T'){
					xCount++;
					oCount++;
				}
				else
					status = 0;
			}
			if (xCount == 4){
				status = 2;
				break;
			}
			else if (oCount == 4){
				status = 3;
				break;
			}
		}
		if (status < 2) {
				//Check Horizontal
			for (int x = 0; x < 4; x++) {
				xCount = 0;
				oCount = 0;
				for (int y = 0; y < 4; y++) {
					if(grids[casesTested][y][x] == 'O')
						oCount++;
					else if(grids[casesTested][y][x] == 'X')
						xCount++;
					else if(grids[casesTested][y][x] == 'T'){
						xCount++;
						oCount++;
					}
				}
				if (xCount == 4){
					status = 2;
					break;
				}
				else if (oCount == 4){
					status = 3;
					break;
				}
			}
		}
		if (status < 2) {
			xCount = 0;
			oCount = 0;
				//Check Diagonal
			for (int i = 0; i < 4; i++) {
				if(grids[casesTested][i][i] == 'O')
					oCount++;
				else if(grids[casesTested][i][i] == 'X')
					xCount++;
				else if(grids[casesTested][i][i] == 'T'){
					xCount++;
					oCount++;
				}
			}
			if (xCount == 4){
				status = 2;
			}
			else if (oCount == 4){
				status = 3;
			}
		}
		if (status < 2) {
			xCount = 0;
			oCount = 0;
				//Check Diagonal
			for (int i = 0; i < 4; i++) {
				if(grids[casesTested][i][3 - i] == 'O')
					oCount++;
				else if(grids[casesTested][i][3 - i] == 'X')
					xCount++;
				else if(grids[casesTested][i][3 - i] == 'T'){
					xCount++;
					oCount++;
				}
			}
			if (xCount == 4){
				status = 2;
			}
			else if (oCount == 4){
				status = 3;
			}
		}
		cout << "Case #" << casesTested + 1 << ": ";
		switch (status) {
			case 1:
				cout << "Draw\n" << endl;
				break;
			case 2:
				cout << "X won\n" << endl;
				break;
			case 3:
				cout << "O won\n" << endl;
				break;
			default:
				cout << "Game has not completed\n" << endl;
				break;
		}
		casesTested++;
	}
	return 0;
}