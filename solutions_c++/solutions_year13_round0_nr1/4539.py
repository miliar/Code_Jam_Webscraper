#include <iostream>
#include <fstream>
#include <string>
#include <math.h>


using namespace std;

int main()
{
	fstream fin("A.in",ios::in);
	fstream fout("A.out",ios::out);
	int tc;
	fin>>tc;
	int Case = 0;

	while (tc--)
	{
		Case++;
		bool Xwin = false;
		bool Owin = false;
		bool draw = false;
		bool completed = true;

		char board[4][4];
		char ch;
		for (int i = 0; i< 4; i++)
		{
			for(int j = 0; j<4; j++)
			{
				fin>>ch;
				board[i][j] = ch;
				
				if(ch == '.')
					completed = false;
			}
		}
		//10 state should be checked! :D

		//X won
		//XXXX

		for (int i = 0; i<4; i++)
		{
			Xwin = false;
			int counter = 0;

			for (int j = 0; j<4;j++)
			{
				if(board[i][j]=='X'||board[i][j]=='T')
				{
					counter++;
				}
			}
			if (counter == 4)
			{
				Xwin = true;
				break;
			}
		}
		if(Xwin)
		{
			fout<< "Case #"<<Case<<": "<<"X won"<<endl;
			continue;
		}

		/*
		X
		X
		X
		X
		*/
		for (int j = 0; j<4; j++)
		{
			Xwin = false;
			int counter = 0;

			for (int i = 0; i<4;i++)
			{
				if(board[i][j]=='X'||board[i][j]=='T')
				{
					counter++;
				}
			}
			if (counter == 4)
			{
				Xwin = true;
				break;
			}
		}
		if(Xwin)
		{
			fout<< "Case #"<<Case<<": "<<"X won"<<endl;
			continue;
		}

		/*
		X
		*X
		**X
		***X
		*/
		Xwin = false;
		int counter = 0;
		for (int i = 0; i < 4; i++)
		{
			if(board[i][i]=='X'||board[i][i]=='T')
			{
				counter++;
			}
		}
		if (counter == 4)
			Xwin = true;
		if(Xwin)
		{
			fout<< "Case #"<<Case<<": "<<"X won"<<endl;
			continue;
		}
		/*
		***X
		**X
		*X
		X
		*/
		Xwin = false;
		counter = 0;
		for (int i = 0; i < 4; i++)
		{
			if(board[i][3-i]=='X'||board[i][3-i]=='T')
			{
				counter++;
			}
		}
		if (counter == 4)
			Xwin = true;
		if(Xwin)
		{
			fout<< "Case #"<<Case<<": "<<"X won"<<endl;
			continue;
		}



		//O won!
		//OOOO

		for (int i = 0; i<4; i++)
		{
			Owin = false;
			int counter = 0;

			for (int j = 0; j<4;j++)
			{
				if(board[i][j]=='O'||board[i][j]=='T')
				{
					counter++;
				}
			}
			if (counter == 4)
			{
				Owin = true;
				break;
			}
		}
		if(Owin)
		{
			fout<< "Case #"<<Case<<": "<<"O won"<<endl;
			continue;
		}

		/*
		O
		O
		O
		O
		*/
		if(!Owin)
		{
			for (int j = 0; j<4; j++)
			{
				Owin = false;
				int counter = 0;

				for (int i = 0; i<4;i++)
				{
					if(board[i][j]=='O'||board[i][j]=='T')
					{
						counter++;
					}
				}
				if (counter == 4)
				{
					Owin = true;
					break;
				}
			}
		}

		if(Owin)
		{
			fout<< "Case #"<<Case<<": "<<"O won"<<endl;
			continue;
		}

		/*
		O
		*O
		**O
		***O
		*/
		Owin = false;
		counter = 0;

		for (int i = 0; i < 4; i++)
		{
			if(board[i][i]=='O'||board[i][i]=='T')
			{
				counter++;
			}
		}
		if (counter == 4)
			Owin = true;
		if(Owin)
		{
			fout<< "Case #"<<Case<<": "<<"O won"<<endl;
			continue;
		}
		/*
		***O
		**O
		*O
		O
		*/
		Owin = false;
		counter = 0;
		for (int i = 0; i < 4; i++)
		{
			if(board[i][3-i]=='O'||board[i][3-i]=='T')
			{
				counter++;
			}
		}
		if (counter == 4)
			Owin = true;
		if(Owin)
		{
			fout<< "Case #"<<Case<<": "<<"O won"<<endl;
			continue;
		}

		if(completed)
			fout<< "Case #"<<Case<<": "<<"Draw"<<endl;
		else
			fout<< "Case #"<<Case<<": "<<"Game has not completed"<<endl;
			
	}
}