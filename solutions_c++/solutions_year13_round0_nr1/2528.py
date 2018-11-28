#include<iostream>
#include<iomanip>
#include<vector>
#include<string>
#include<algorithm>
#include<list>
#include<map>
using namespace std;

int main()
{	
	int t;
	cin>>t;
	for(int k=1; k<=t; k++){
		int s=4, i, j, board[4][4];
		vector<string> in(s);
		string blank;
		getline(cin, blank);
		for(i=0; i<4; i++){
			getline(cin, in[i]);
		}
		for(i=0; i<4; i++){
			for(j=0; j<4; j++){
				board[i][j]=in[i][j];
			}
		}
		char won='A';
		//row check
		for(i=0; i<4; i++){
			if(board[i][0]=='X' || board[i][0]=='T'){
				if(board[i][1]=='X' || board[i][1]=='T')
					if(board[i][2]=='X' || board[i][2]=='T')
						if(board[i][3]=='X' || board[i][3]=='T'){
							won='X';
							break;
						}
			}
			else if(board[i][0]=='O' || board[i][0]=='T'){
					if(board[i][1]=='O' || board[i][1]=='T')
						if(board[i][2]=='O' || board[i][2]=='T')
							if(board[i][3]=='O' || board[i][3]=='T'){
								won='O';
								break;
							}
			}
		}
		//column check
		if(won=='A'){
			for(j=0; j<4; j++){
				if(board[0][j]=='X' || board[0][j]=='T'){
					if(board[1][j]=='X' || board[1][j]=='T')
						if(board[2][j]=='X' || board[2][j]=='T')
							if(board[3][j]=='X' || board[3][j]=='T'){
								won='X';
								break;
							}
				}
				else if(board[0][j]=='O' || board[0][j]=='T'){
						if(board[1][j]=='O' || board[1][j]=='T')
							if(board[2][j]=='O' || board[2][j]=='T')
								if(board[3][j]=='O' || board[3][j]=='T'){
									won='O';
									break;
								}
				}
			}
		}
		//left diagonal
		if(won=='A'){
			if(board[0][0]=='X' || board[0][0]=='T'){
					if(board[1][1]=='X' || board[1][1]=='T')
						if(board[2][2]=='X' || board[2][2]=='T')
							if(board[3][3]=='X' || board[3][3]=='T'){
								won='X';
							}
			}
			else if(board[0][0]=='O' || board[0][0]=='T'){
					if(board[1][1]=='O' || board[1][1]=='T')
						if(board[2][2]=='O' || board[2][2]=='T')
							if(board[3][3]=='O' || board[3][3]=='T')
								won='O';
			}
		}
		//right diagonal
		if(won=='A'){
			if(board[0][3]=='X' || board[0][3]=='T'){
					if(board[1][2]=='X' || board[1][2]=='T')
						if(board[2][1]=='X' || board[2][1]=='T')
							if(board[3][0]=='X' || board[3][0]=='T')
								won='X';
			}else if(board[0][3]=='O' || board[0][3]=='T'){
					if(board[1][2]=='O' || board[1][2]=='T')
						if(board[2][1]=='O' || board[2][1]=='T')
							if(board[3][0]=='O' || board[3][0]=='T')
								won='O';
			}
		}
		//not over
		if(won=='A'){
			for(i=0; i<4; i++){
				for(j=0; j<4; j++){
					if(board[i][j]=='.')
						won='.';
						break;
				}
			}
		}
		if(won=='X')
			cout<<"Case #"<<k<<": "<<won<<" won"<<endl;
		else if(won=='O')
			cout<<"Case #"<<k<<": "<<won<<" won"<<endl;
		else if(won=='.')
			cout<<"Case #"<<k<<": "<<"Game has not completed"<<endl;
		else
			cout<<"Case #"<<k<<": "<<"Draw"<<endl;
		
	}
	return 0;
}