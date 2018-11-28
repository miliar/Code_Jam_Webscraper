// codejam.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <cstring>
#include <string>
#include <set>
#include <queue>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int T;
char board[4][4];

int main()
{
	cin>>T;
	for(int i=0; i<T; i++)
	{
		bool dot = false;
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				cin>>board[j][k];
				if(board[j][k]=='.')
					dot = true;
			}
		}
		int rowCount[4][3];
		int colCount[4][3];
		int diagCount[2][3];
		for(int j=0; j<4; j++){
			rowCount[j][0] = rowCount[j][1] = rowCount[j][2] = 0;
			colCount[j][0] = colCount[j][1] = colCount[j][2] = 0;
			if(j<2)
				diagCount[j][0] = diagCount[j][1] = diagCount[j][2] = 0;
		}
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				if(board[j][k]=='X'){
					rowCount[j][0]++;
					colCount[k][0]++;
					if(j==k)
						diagCount[0][0]++;
					if(j+k==3)
						diagCount[1][0]++;
				}
				if(board[j][k]=='O'){
					rowCount[j][1]++;
					colCount[k][1]++;
					if(j==k)
						diagCount[0][1]++;
					if(j+k==3)
						diagCount[1][1]++;
				}
				if(board[j][k]=='T'){
					rowCount[j][2]++;
					colCount[k][2]++;
					if(j==k)
						diagCount[0][2]++;
					if(j+k==3)
						diagCount[1][2]++;
				}
			}
		}

		int count[10][3];
		for(int j=0; j<4; j++){
			for(int k=0; k<3; k++){
				count[j][k] = rowCount[j][k];
			}
		}
		for(int j=0; j<4; j++){
			for(int k=0; k<3; k++){
				count[j+4][k] = colCount[j][k];
			}
		}
		for(int j=0; j<2; j++){
			for(int k=0; k<3; k++){
				count[j+8][k] = diagCount[j][k];
			}
		}
		bool done = false;
		for(int j=0; j<10; j++){
			if(count[j][0]==4 || (count[j][0]==3 && count[j][2]==1)){
				printf("Case #%d: X won\n",i+1);
				done = true;
				break;
			}
			else if(count[j][1]==4 || (count[j][1]==3 && count[j][2]==1)){
				printf("Case #%d: O won\n",i+1);
				done = true;
				break;
			}
		}
		if(!done){
			if(dot){
				printf("Case #%d: Game has not completed\n",i+1);
			}
			else{
				printf("Case #%d: Draw\n",i+1);
			}
		}
	}

	return 0;
}

