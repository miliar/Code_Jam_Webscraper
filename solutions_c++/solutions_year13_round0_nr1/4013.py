#include <iostream>
#include<string>
using namespace std;

void main()
{

	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int num=0;
	cin >> num;

	for(int i=0;i<num;i++)
	{
		string input;
		char board [4][4];

		//adding input in 2-d array board
		for (int k=0;k<4;k++)
		{
			cin>>input;

			for(int j=0;j<4;j++)
			{
				board[k][j]=input.at(j);
			}
		}

		bool win = false;
		bool nCompleted = false;

		//looking at the array
		for(int row=0;row<4;row++)
		{
			int t=0;
			int x=0;
			int o=0;

			for(int col=0;col<4;col++)
			{
				if(board[row][col]=='X')
				{
					x +=1;
				}
				if(board[row][col]=='O')
				{
					o+=1;
				}
				if(board[row][col]=='T')
				{
					t+=1;
				}
				if(board[row][col]=='.')
				{
					nCompleted=true;
				}
			}
			//for a row:

			if(x+t ==4)
			{
				cout << "Case #" << i+1 << ": "<<"X won" << endl;
				win=true;
				break;
			}
			if(o+t ==4)
			{
				cout << "Case #" << i+1 << ": "<<"O won" << endl;
				win=true;
				break;
			}

		}

		//when finished go to second test case.
		if(win==true)
		{
			//string enter;
			//cin>>enter;
			continue;
		}

		//for a col
		for(int row=0;row<4;row++)
		{
			int t=0;
			int x=0;
			int o=0;

			for(int col=0;col<4;col++)
			{
				if(board[col][row]=='X')
				{
					x +=1;
				}
				if(board[col][row]=='O')
				{
					o+=1;
				}
				if(board[col][row]=='T')
				{
					t+=1;
				}
				if(board[col][row]=='.')
				{
					nCompleted=true;
				}
			}
			//for a row:

			if(x+t ==4)
			{
				cout << "Case #" << i+1 << ": "<<"X won" << endl;
				win=true;
				break;
			}
			if(o+t ==4)
			{
				cout << "Case #" << i+1 << ": "<<"O won" << endl;
				win=true;
				break;
			}

		}

		if(win==true)
		{
			//string enter;
			//cin>>enter;
			continue;
		}

		//for diagonal
		int t=0;
		int x=0;
		int o=0;

		for(int row=0;row<4;row++)
		{
			if(board[row][row]=='X')
				{
					x +=1;
				}
				if(board[row][row]=='O')
				{
					o+=1;
				}
				if(board[row][row]=='T')
				{
					t+=1;
				}
				/*if(board[row][row]=='.')
				{
					nCompleted=true;
				}*/
		}
		//string enter;
		if(x+t ==4)
			{

				cout << "Case #" << i+1 << ": "<<"X won" << endl;
				//cin>>enter;
				continue;
			}
		if(o+t ==4)
			{
				cout << "Case #" << i+1 << ": "<<"O won" << endl;
				//cin>>enter;
				continue;
			}

		//Opposite Diagonal
		 t=0;
		 x=0;
		 o=0;

		for(int row=0;row<4;row++)
		{
			if(board[row][3-row]=='X')
				{
					x +=1;
				}
				if(board[row][3-row]=='O')
				{
					o+=1;
				}
				if(board[row][3-row]=='T')
				{
					t+=1;
				}
				/*if(board[row][3-row]=='.')
				{
					nCompleted=true;
				}*/
		}
		 
		if(x+t ==4)
			{

				cout << "Case #" << i+1 << ": "<<"X won" << endl;
				//cin>>enter;
				continue;
			}
		if(o+t ==4)
			{
				cout << "Case #" << i+1 << ": "<<"O won" << endl;
				//cin>>enter;
				continue;
			}


		//Analyzing

		//no win
		if(nCompleted)
		{
			cout << "Case #" << i+1 << ": "<<"Game has not completed" << endl;
			//cin>>enter;
			continue;
		}

		//or draw
		cout << "Case #" << i+1 << ": "<<"Draw" << endl;
		//cin>>enter;
	}


}