#include <string>
#include <sstream>
#include <iostream>
#include <math.h>
#include <fstream>
#include <vector>
using namespace std;

// bool isFilled(){}

// bool hasWon(char c)// x for x, o for o
// {}

int analyze(string board[4])
{
	int result; // 1-oWon, 2-xWon, 3- draw, 4- gamenotCompleted
	//check horizontals
	for(int i=0; i<4 ; i++)
	{
		const char first= board[i][0]; 
		if(first == 'T')
		{
			const char first1 = board[i][1];
			if((first1 != '.') && (board[i][0] == first1 || board[i][0] == 'T') && 
							(board[i][2] == first1 || board[i][2] == 'T') &&
							(board[i][3] == first1 || board[i][3] == 'T') )
			{
				cout<<"winner on column "<<i<<endl;
				if(board[i][1] == 'X')
				{
					return 2;
				}
				else if(board[i][1] == 'O')
				{
					return 1;
				}
			}
		}
		else if((first != '.') 
			&& (board[i][1] == first 
			|| board[i][1]=='T') && 
							(board[i][2] == first || board[i][2] == 'T') &&
							(board[i][3] == first || board[i][3] == 'T') )
		{	
			cout<<"winner on row "<<i<<endl;
			if(board[i][0] == 'X')
			{
				return 2;
			}
			else if(board[i][0] == 'O')
			{
				return 1;
			}
		}

	}
	//check verticals
	for(int i=0; i<4 ; i++)
	{
		const char first = board[0][i];
		if(first == 'T')
		{
			const char first1 = board[1][i];
			if((first1 != '.') && (board[0][i] == first1 || board[0][i] == 'T') && 
							(board[2][i] == first1 || board[2][i] == 'T') &&
							(board[3][i] == first1 || board[3][i] == 'T') )
			{
				cout<<"winner on column "<<i<<endl;
				if(board[1][i] == 'X')
				{
					return 2;
				}
				else if(board[1][i] == 'O')
				{
					return 1;
				}
			}
		}
		else if((first != '.') && (board[1][i] == first || board[1][i] == 'T') && 
							(board[2][i] == first || board[2][i] == 'T') &&
							(board[3][i] == first || board[3][i] == 'T') )
		{
			cout<<"winner on column "<<i<<endl;
			if(board[0][i] == 'X')
			{
				return 2;
			}
			else if(board[0][i] == 'O')
			{
				return 1;
			}
			else if(board[1][i] == 'X')
			{
			return 2;
			}
			else if(board[1][i] == 'O')
			{
				return 1;
			}
		}
	}
	//check diagonals
	const char first = board[0][0];
	if(first == 'T')
		{
			const char first1 = board[1][1];
			if((first1 != '.') && (board[0][0] == first1 || board[0][0] == 'T') && 
							(board[2][2] == first1 || board[2][2] == 'T') &&
							(board[3][3] == first1 || board[3][3] == 'T') )
			{
				cout<<"winner on diagonal 1 "<<endl;
				if(board[1][1] == 'X')
				{
					return 2;
				}
				else if(board[1][1] == 'O')
				{
					return 1;
				}
			}
		}
		else if((first != '.') && (board[1][1] == first || board[1][1] == 'T') && 
							(board[2][2] == first || board[2][2] == 'T') &&
							(board[3][3] == first || board[3][3] == 'T') )
	{
		cout<<"winner on diagonal 1 "<<endl;
		if(board[0][0] == 'X')
		{
			return 2;
		}
		else if(board[0][0] == 'O')
		{
			return 1;
		}
		else if(board[1][1] == 'X')
		{
			return 2;
		}
		else if(board[1][1] == 'O')
		{
			return 1;
		}
		
	}

	const char first1 = board[0][3];
	if(first == 'T')
		{
			const char first1 = board[1][2];
			if((first1 != '.') && (board[0][3] == first1 || board[0][3] == 'T') && 
							(board[2][1] == first1 || board[2][1] == 'T') &&
							(board[3][0] == first1 || board[3][0] == 'T') )
			{
				cout<<"winner on diagonal 2 "<<endl;
				if(board[1][2] == 'X')
				{
					return 2;
				}
				else if(board[1][2] == 'O')
				{
					return 1;
				}
			}
		}
		else 
	if((first1 != '.') && (board[1][2] == first1 || board[1][2] == 'T') && 
							(board[2][1] == first1 || board[2][1] == 'T') &&
							(board[3][0] == first1 || board[3][0] == 'T') )
	{
		cout<<"winner on diagonal 2 "<<endl;
			if(board[3][0] == 'X')
			{
				return 2;
			}
			else if(board[3][0] == 'O')
			{
				return 1;
			}
			else if(board[2][1] == 'X')
			{
				return 2;
			}
			else if(board[2][1] == 'O')
			{
				return 1;
			}
	
	}
	//check for draw or unfinished game
	bool gameFinished = true;
	for (int i = 0; i < 4; ++i)
	{
		size_t found = board[i].find(".");
		if(found != -1)
			gameFinished = false;
	}
	if(gameFinished == true)
		return 3;
	else return 4;
}

int main()
{
	string line;
	ifstream myfile("in.txt");
	ofstream outFile;
  	outFile.open ("out.txt");
// get # testcases
  	getline (myfile,line);
	int numCases= atoi(line.c_str());
	cout<<numCases<<endl;
	for(size_t i = 1; i<= numCases;i++)//numCases; i++)
	{
		//readboard
		string board[4];
		for(int j=0;j<4;j++)
			getline (myfile,board[j]);

		int result = analyze(board);
		cout<<"res:"<<result<<endl;
		outFile<<"Case #"<<i<<": ";
		if(result == 1)
		{
			outFile<<"O won"<<endl;}
		else if(result == 2)
		{
			outFile<<"X won"<<endl;}
		else if(result == 3)
		{
			outFile<<"Draw"<<endl;}
		else
		{
			outFile<<"Game has not completed"<<endl;}
		//read empty string 	
		getline (myfile,line);
	}
	outFile.close();
	myfile.close();
	return 0;
}