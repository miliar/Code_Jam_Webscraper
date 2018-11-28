#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ifstream input;
	ofstream output;
	input.open("A-large.in");
	output.open("output.txt");

	int test_num;
	input>>test_num;

	for(int qwer=0; qwer<test_num; qwer++){
		int board[4][4];
		char temp;
		int char_num = 16;

		// take input
		for(int loop=0; loop<16; loop++){
			input>>temp;
			if(temp == 'O')
				board[loop/4][loop%4] = 1;
			else if(temp == 'X')
				board[loop/4][loop%4] = 2;
			else if(temp == 'T')
				board[loop/4][loop%4] = 10;
			else if(temp == '.'){
				board[loop/4][loop%4] = 0;		
				char_num--;
			}
		}
		//vertical
		int result=0;
		int Ocount;
		int Xcount;
		for(int loop=0; loop<4; loop++){
			Ocount = 0;
			Xcount = 0;
			for(int loop2=0; loop2<4; loop2++){
				if(board[loop][loop2] == 1)
					Ocount++;
				else if(board[loop][loop2] == 2)
					Xcount++;
				else if(board[loop][loop2] == 10){
					Ocount++;
					Xcount++;
				}
			}
			if(Ocount == 4)
				result = 1;
			else if(Xcount == 4)
				result = 2;
		}

		//horizontal
		for(int loop=0; loop<4; loop++){
			Ocount = 0;
			Xcount = 0;
			for(int loop2=0; loop2<4; loop2++){
				if(board[loop2][loop] == 1)
					Ocount++;
				else if(board[loop2][loop] == 2)
					Xcount++;
				else if(board[loop2][loop] == 10){
					Ocount++;
					Xcount++;
				}
			}
			if(Ocount == 4)
				result = 1;
			else if(Xcount == 4)
				result = 2;
		}

		Ocount = 0;
		Xcount = 0;
		for(int loop2=0; loop2<4; loop2++){
			if(board[loop2][3-loop2] == 1)
				Ocount++;
			else if(board[loop2][3-loop2] == 2)
				Xcount++;
			else if(board[loop2][3-loop2] == 10){
				Ocount++;
				Xcount++;
			}
		}
		if(Ocount == 4)
			result = 1;
		else if(Xcount == 4)
			result = 2;

		Ocount = 0;
		Xcount = 0;
		for(int loop2=0; loop2<4; loop2++){
			if(board[loop2][loop2] == 1)
				Ocount++;
			else if(board[loop2][loop2] == 2)
				Xcount++;
			else if(board[loop2][loop2] == 10){
				Ocount++;
				Xcount++;
			}
		}
		if(Ocount == 4)
			result = 1;
		else if(Xcount == 4)
			result = 2;

		if(result == 1)
			output<<"Case #"<<qwer+1<<": "<<"O won"<<endl;
		else if(result == 2)
			output<<"Case #"<<qwer+1<<": "<<"X won"<<endl;
		else if(result == 0){
			if(char_num == 16)
				output<<"Case #"<<qwer+1<<": "<<"Draw"<<endl;
			else
				output<<"Case #"<<qwer+1<<": "<<"Game has not completed"<<endl;
		}

	}

	input.close();

	return 0;
}