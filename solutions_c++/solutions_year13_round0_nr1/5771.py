#include<iostream>
#include<vector>
#include<fstream>
#include<string>
using namespace std;

bool Owon,Xwon;
vector <string> board;
int counter;
int main()
{
	int testCases;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> testCases;
	for (int a=0; a<testCases; a++)
	{
		counter=0;
		Owon=false;
		Xwon=false;
		board.clear();
		string input="";
		for (int aa=0; aa<4; aa++)
		{
			
			cin >> input;
			board.push_back(input);
			for (int abc=0; abc<4;abc++)
				if (input[abc]!='.')
					counter++;
		}
		// check board
		for (int row=0; row<4;row++)
		{
			char test=board[row][0];
			if (test!='.')
			{
				// check for Four in a row
				bool testing=true;
				for (int col=1; col<4; col++)
				{
					if (board[row][col]!=test)
					{
						if (test!='T'&&board[row][col]!='T')
						{
							testing=false;
							break;
						}
						else  if (board[row][col]!='T')
						{
							test=board[row][col];
						}
					}

				}
				if (testing&&test=='X')
					Xwon=true;
				if (testing&&test=='O')
					Owon=true;
			}
		}
		//Check for four in a column
		for (int col=0; col<4;col++)
		{
			char test=board[0][col];
			if (test!='.')
			{
				// check for Four in a row
				bool testing=true;
				for (int row=1; row<4; row++)
				{
					if (board[row][col]!=test)
					{
						if (test!='T'&&board[row][col]!='T')
						{
							testing=false;
							break;
						}
						else if (board[row][col]!='T')
						{
							test=board[row][col];
						}
					}

				}
				if (testing&&test=='X')
					Xwon=true;
				if (testing&&test=='O')
					Owon=true;
			}
		}
	// Check for diagonal
		bool testing=true;
			char test=board[0][0];
		for (int diagonal=0; diagonal<4; diagonal++)
		{
			
			if (board[diagonal][diagonal]!=test)
			{
				// check for Four in a row
			
						if (test!='T'&&board[diagonal][diagonal]!='T')
						{
							testing=false;
							break;
						}
						else if (board[diagonal][diagonal]!='T')
						{
							test=board[diagonal][diagonal];
						}
					

				}
				
			}
		if (testing&&test=='X')
					Xwon=true;
				if (testing&&test=='O')
					Owon=true;
			 testing=true;
			 test=board[0][3];
		for (int diagonal=0; diagonal<4; diagonal++)
		{
			
		if (board[diagonal][3-diagonal]!=test)
			{
				// check for Four in a row
			
						if (test!='T'&&board[diagonal][3-diagonal]!='T')
						{
							testing=false;
							break;
						}
						else if (board[diagonal][3-diagonal]!='T')
						{
							test=board[diagonal][3-diagonal];
						}
					

				}
				
			}
		if (testing&&test=='X')
					Xwon=true;
				if (testing&&test=='O')
					Owon=true;
				printf("Case #%d: ",a+1);
				if (Xwon&&Owon)
					printf("Draw\n");
				else if (Xwon)
					printf("X won\n");
				else if (Owon)
					printf("O won\n");
				else if (counter!=16) printf("Game has not completed\n");
				else printf("Draw\n");
				//cin >> input;
		}

		
	}



