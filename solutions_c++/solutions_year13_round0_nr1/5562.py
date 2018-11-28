#include<iostream>
#include<fstream>
#include<string>

using namespace std;

ifstream fin("A-small-attempt2.in");
ofstream fout("A-small-attempt2.out");

int board[4][4] = {0};
string out[4] = {"Draw", "X won", "O won", "Game has not completed"};


int main()
{
	int T = 0;
	char c;
	fin >> T;
	for(int i = 0; i < T; i++){
		int empty = 0;
		int t = 2;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
			    fin >> c;
				if(c=='X'){board[j][k] = 2;}
				else if(c=='O'){board[j][k] = -2;}
				else if(c=='T'){board[j][k] = 1; t = 0;}
				else{board[j][k] = 0; empty = 1;}
			}
		}
		int flag[10] = {0};
		for(int j = 0; j < 4; j++){
			flag[8] += board[j][j];
			flag[9] += board[j][3-j];
			for(int k = 0; k < 4; k++){
				flag[j] += board[j][k];
				flag[4+j] += board[k][j];
			}
		}
		int result=0;
		for(int ix = 0; ix < 10; ix++){
			if(flag[ix] > 6){ result = 1; break;}
			else if(flag[ix] < -4-t){ result = 2; break;}
			else{
				if(1 == empty)
					result = 3;
			}
		}
		fout << "Case #" << i+1 <<": "<< out[result];
		if(i < T-1) fout << endl;
	}
	return 1;
}