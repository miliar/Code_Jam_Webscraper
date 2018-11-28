#include<iostream>
#include <fstream> 
#include<math.h>
using namespace std;

int main()
{
	ofstream fout("result.rtf");
	int T;
	scanf("%d\n", &T);
	for(int k=0; k<T; k++)
		{
		int square[4][4];

		int sum_i[4] = {0};
		int sum_j[4] = {0};

		bool endOfGame = false;

		char c;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				c = getchar();
				if( c == 'T')
					square[i][j] = 5;
				else if( c == 'X')
					square[i][j] = 10;
				else if( c == 'O')
					square[i][j] = -10;
				else if(c == '.')
					square[i][j] = 0;
			}
			c = getchar();
		}

		c = getchar();
		

		for(int i=0; i<4 && endOfGame == false ; i++)
		{
			for(int j=0; j<4; j++)
			{
				sum_i[i] += square[i][j];
			}
			if(sum_i[i] >= 35)
			{
				fout << "Case #" << k+1 << ": " << "X won" << endl;
				endOfGame = true;
			}
			if(sum_i[i] <=-25)
			{
				fout << "Case #" << k+1 << ": " << "O won" << endl;
				endOfGame = true;
			}
		}

		for(int j=0; j<4 && endOfGame == false ; j++)
		{
			for(int i=0; i<4; i++)
			{
				sum_j[j] += square[i][j];
			}
			if(sum_j[j] >= 35)
			{
				fout << "Case #" << k+1 << ": " << "X won" << endl;
				endOfGame = true;
			}
			if(sum_j[j] <=-25)
			{
				fout << "Case #" << k+1 << ": " << "O won" << endl;
				endOfGame = true;
			}
		}




		if(endOfGame == false)
		{

			int sum_L_Diagonal = 0;
			for(int i=0; i<4; i++)
			{
				sum_L_Diagonal += square[i][i];
			}

			if(sum_L_Diagonal >= 35)
			{
				fout << "Case #" << k+1 << ": " << "X won" << endl;
				endOfGame = true;
			}
			if(sum_L_Diagonal <= -25)
			{
				fout << "Case #" << k+1 << ": " << "O won" << endl;
				endOfGame = true;
			}
		}

		if(endOfGame == false)
		{

			int sum_R_Diagonal = 0;
			for(int i=0; i<4; i++)
			{
				sum_R_Diagonal += square[3-i][i];
			}

			if(sum_R_Diagonal >= 35)
			{
				fout << "Case #" << k+1 << ": " << "X won" << endl;
				endOfGame = true;
			}
			if(sum_R_Diagonal <= -25)
			{
				fout << "Case #" << k+1 << ": " << "O won" << endl;
				endOfGame = true;
			}
		}
		/////////////////////////////////////////////////////////
		if(endOfGame == false)
		{
			bool completed = true;
			for(int i=0; i<4; i++)
			{
				for(int j=0; j<4; j++)
				{
					if(square[i][j] == 0)
					{
						completed = false;
						break;
					}
				}
			}

			if(completed)
				fout << "Case #" << k+1 << ": " << "Draw" << endl;
			else
				fout << "Case #" << k+1 << ": " << "Game has not completed" << endl;
		}
	}
	system("pause");
}
