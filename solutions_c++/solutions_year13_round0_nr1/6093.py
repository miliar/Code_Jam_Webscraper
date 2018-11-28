#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <utility>
#include <string>

using namespace std;

int main(void){

	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T;

	
	cin>>T;


	for(int t = 0; t < T; t++){
		bool isDot = false;
		int givenMat[4][4];
		string str;
		for(int i = 0; i < 4; i++){
			cin>>str;

			for(int j = 0; j < str.size(); j++){
				if(str[j] == 'X'){
					givenMat[i][j] = 1;
				}
				else if(str[j] == 'O'){
					givenMat[i][j] = 2;
				}
				else if(str[j] == 'T'){
					givenMat[i][j] = 3;
				}
				else{
					isDot = true;
					givenMat[i][j] = 0;
				}
			}
			//for(int j = 0; j < 4; j++){
			//	//cin>>givenMat[i][j];
			//	scanf("%c",&givenMat[i][j]);
			//	if(givenMat[i][j] == 'X')
			//		givenMat[i][j] = 1;
			//	else if(givenMat[i][j] == 'O')
			//		givenMat[i][j] = 2;
			//	else if(givenMat[i][j] == 'T')
			//		givenMat[i][j] = 3;
			//	else if(givenMat[i][j] == '.')
			//		isDot = true;
			//}
		}
		
		bool xWin, oWin;
		xWin = oWin = false;

		// scan all the rows
		for(int row = 0; row < 4; row++){
			int temp = 3;
			bool dotEncountered = false;
			for(int col = 0; col < 4; col++){
				if(givenMat[row][col] == 0){
					dotEncountered = true;
					break;
				}
				temp &= givenMat[row][col];
			}

			if(!dotEncountered && temp == 1){
				xWin = true;
				break;
			}
			else if(!dotEncountered && temp == 2){
				oWin = true;
				break;
			}
		}

		if(xWin){
			cout<<"Case #"<<t+1<<": X won"<<endl;
			continue;
		}
		else if(oWin){
			cout<<"Case #"<<t+1<<": O won"<<endl;
			continue;
		}

		// scan all the columns
		for(int col = 0; col < 4; col++){
			int temp = 3;
			bool dotEncountered = false;
			for(int row = 0; row < 4; row++){
				if(givenMat[row][col] == 0){
					dotEncountered = true;
					break;
				}
				temp &= givenMat[row][col];
			}

			if(!dotEncountered && temp == 1){
				xWin = true;
				break;
			}
			else if(!dotEncountered && temp == 2){
				oWin = true;
				break;
			}
		}

		if(xWin){
			cout<<"Case #"<<t+1<<": X won"<<endl;
			continue;
		}
		else if(oWin){
			cout<<"Case #"<<t+1<<": O won"<<endl;
			continue;
		}


		// scan the first diagonal
		int temp = 3;
		bool dotEncountered = false;
		for(int row = 0; row < 4; row++){
			for(int col = 0; col < 4; col++){
				if(row != col)
					continue;
				if(givenMat[row][col] == 0){
					dotEncountered = true;
					break;
				}
				temp &= givenMat[row][col];
			}
		}


		if(!dotEncountered && temp == 1){
			xWin = true;
		}
		else if(!dotEncountered && temp == 2){
			oWin = true;
		}


		if(xWin){
			cout<<"Case #"<<t+1<<": X won"<<endl;
			continue;
		}
		else if(oWin){
			cout<<"Case #"<<t+1<<": O won"<<endl;
			continue;
		}


		// scan the second diagonal
		temp = 3;

		dotEncountered = false;

		for(int row = 0; row < 4; row++){
			for(int col = 3; col >= 0; col--){
				if(row == 3 - col){
					if(givenMat[row][col] == 0){
						dotEncountered = true;
						break;
					}
					temp &= givenMat[row][col];
				}
			}
		}

		if(!dotEncountered && temp == 1){
			xWin = true;
		}
		else if(!dotEncountered && temp == 2){
			oWin = true;
		}

		if(xWin){
			cout<<"Case #"<<t+1<<": X won"<<endl;
			continue;
		}
		else if(oWin){
			cout<<"Case #"<<t+1<<": O won"<<endl;
			continue;
		}

		if(isDot){
			cout<<"Case #"<<t+1<<": Game has not completed"<<endl;
		}
		else{
			cout<<"Case #"<<t+1<<": Draw"<<endl;
		}

	}

	return 0;
}