#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	//========read in input==========//
	char* testinput = "c:\\test.txt";
 	char* input = "c:\\A-small-attempt0.in";
 	ifstream fin;
 	fin.open(input,ios_base::binary);
 	//========create output=========//
 	ofstream fout;
	fout.open("output_f.txt");
 	//==========test case==========//
	int T, K, N; 
	fin >> T;
	int t  = 1;
	for (t; t <= T; t++)
	{
		fin >> N;
		fin >> K;
		fout << "Case #" << t << ": ";
		char ** board = new char* [N];
		for(int i = 0; i < N; i++ )
		{
			board[i] = new char[N];
			for(int j = 0; j< N; j++)
				fin>> board[i][j];
		}
		

		//===move===//
		for(int i = 0; i < N; i++)
		{
			int p = N-1;
			for(int j = N-1; j >=0; j--)
			{
				if(board[i][j] == '.'){}
				else
				{
					board[i][p] = board[i][j];
					p--;
				}
			}
			while(p >=0)
			{
				board[i][p] = '.';
				p--;
			}
		}
		
		//test//
/*		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j < N; j++)
			{
				fout << board[i][j] << " ";
			}
			fout << endl;
		}
*/
		
		bool redflag = false, blueflag = false;
		for(int i = N-1; i >=0; i--)
		{
			int redrow = 0, bluerow = 0;
			bool redbefore = true, bluebefore = true;
			for (int j = N-1; j>=0; j--)
			{
				if(board[i][j] == 'R')
				{
					if(redbefore)
					{
					redrow++;
					if(redrow == K)
						redflag = true;
					}
					else redrow = 1;
					bluebefore = false;
					redbefore = true;
				}
				else if (board[i][j] == 'B')
				{
					if(bluebefore)
					{
						bluerow++;
						if(bluerow == K)
							blueflag = true;
					}
					else bluerow = 1;
					redbefore = false;
					bluebefore = true;
				}
				else continue;
			}
		}


		//-----column-----//
		for(int j = N-1; j >=0; j--)
		{
			int redrow = 0, bluerow = 0;
			bool redbefore = true, bluebefore = true;
			for (int i = N-1; i>=0; i--)
			{
				if(board[i][j] == 'R')
				{
					if(redbefore)
					{
					redrow++;
					if(redrow == K)
						redflag = true;
					}
					else redrow = 1;
					bluebefore = false;
					redbefore = true;
				}
				else if (board[i][j] == 'B')
				{
					if(bluebefore)
					{
						bluerow++;
						if(bluerow == K)
							blueflag = true;
					}
					else bluerow = 1;
					redbefore = false;
					bluebefore = true;
				}
				else continue;
			}
		}
		

		//-----diag---//
		for(int i = 1; i <= N; i++)
		{
			int redrow = 0, bluerow = 0;
			bool redbefore = true, bluebefore = true;
			for(int j = 0; j< i; j++)
			{
				if(board[N-1-j][N-i+j] == 'R')
				{
					if(redbefore)
					{
					redrow++;
					if(redrow == K)
						redflag = true;
					}
					else redrow = 1;
					bluebefore = false;
					redbefore = true;
				}
				else if (board[N-1-j][N-i+j] == 'B')
				{
					if(bluebefore)
					{
						bluerow++;
						if(bluerow == K)
							blueflag = true;
					}
					else bluerow = 1;
					redbefore = false;
					bluebefore = true;
				}
				else continue;
			}
		}

	if(redflag&& blueflag)
		fout << "Both" <<endl;
	else if (redflag &&!blueflag)
		fout <<"Red" <<endl;
	else if (!redflag &&blueflag)
		fout<< "Blue" <<endl;
	else fout<<"Neither" <<endl;



	}
	return 0;


}