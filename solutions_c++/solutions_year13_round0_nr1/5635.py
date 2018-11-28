#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;


char board[4][4];
int T,i,j,Tn,ts1,ts2,counter1,counter2,dots;
string line;

char diagonals(){
	counter1 = counter2 = ts1 = ts2 = 0;
	char c1 = board[0][0];
	if(c1 == 'T'){
		ts1++;
		c1 = board[1][1];
	}else{
		counter1++;
	}
	char c2 = board[0][3];
	if(c2 == 'T'){
		ts2++;
		c2 = board[1][2];
	}else{
		counter2++;
	}

	for(i=1;i<4;i++){
		if(board[i][i] == c1){
			counter1++;
		}
		if(board[i][i] == 'T'){
			ts1++;
		}
		if(board[i][3-i] == c2){
			counter2++;
		}
		if(board[i][3-i] == 'T'){
			ts2++;
		}
	}
	if(counter1+ts1 == 4)
		return c1;
	else if(counter2+ts2 == 4)
		return c2;
	else
		return '.';
}

char square(){
	
	char c1,c2;
	for(i=0;i<4;i++){
		counter1 = counter2 = ts1 = ts2 = 0;
		c1 = board[i][0];
		if(c1 == 'T'){
			ts1++;
			c1 = board[i][1];
		}else{
			counter1++;
		}
			
		c2 = board[0][i];
		if(c2 == 'T'){
			ts2++;
			c2 = board[1][i];
		}else{
			counter2++;
		}

		for(j=1;j<4;j++){
			if(board[i][j] == c1)
				counter1++;
			if(board[i][j] == 'T')
				ts1++;
			if(board[j][i] == c2)
				counter2++;
			if(board[j][i] == 'T')
				ts2++;
		}
		if(counter1+ts1 == 4)
			return c1;
		else if(counter2+ts2 == 4)
			return c2;
	}
	return '.';
}

int main(){


	string status[4];
	status[0] = "X won";
	status[1] = "O won";
	status[2] = "Draw";
	status[3] = "Game has not completed";

	cin>>T;
	Tn = T;

	while(T--){
		dots = 0;
		for(i=0;i<4;i++){
			cin>>line;
			for(j=0;j<4;j++){
				board[i][j] = line[j];
				if(line[j] != '.'){
					dots++;
				}
			}
		}
		


		char diag = diagonals();
		if(diag == 'X')
			printf("Case #%d: %s\n",Tn-T,status[0].c_str());
		else if(diag == 'O')
			printf("Case #%d: %s\n",Tn-T,status[1].c_str());
		else{
			char squ = square();
			if(squ == 'X')
				printf("Case #%d: %s\n",Tn-T,status[0].c_str());
			else if(squ == 'O')
				printf("Case #%d: %s\n",Tn-T,status[1].c_str());
			else if(dots == 16)
				printf("Case #%d: %s\n",Tn-T,status[2].c_str());
			else
				printf("Case #%d: %s\n",Tn-T,status[3].c_str());
		} 
	}
	return 0;
}