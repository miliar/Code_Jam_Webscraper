#include <string>
#include <iostream>
#include <fstream>
using namespace std;
void main () 
{
	ifstream infile ("infile.txt");
	ofstream outfile ("result.txt");
	int cases;
	char tic[4][4];
	int i,j,n,flag,xflag,oflag;
	infile >> cases;
	for (n=1;n<cases+1;n++)
	{
		for (i=0;i<4;i++)
		{
			for (j=0;j<4;j++)
			{
				infile >> tic[i][j];
			}
		}
	
		for (i=0;i<4;i++)
		{
			xflag = 1;
			oflag = 1;
			for (j=0;j<4;j++)
			{
				if (tic[i][j]=='X' || tic[i][j]=='.')
					oflag = 0;
				if (tic[i][j] == 'O' || tic[i][j]=='.')
					xflag = 0;
			}
			if (xflag || oflag)
				break;
		}
		if (!xflag && !oflag)
		{
			for (j=0;j<4;j++)
			{
				xflag = 1;
				oflag = 1;
				for (i=0;i<4;i++)
				{
					if (tic[i][j]=='X' || tic[i][j]=='.')
						oflag = 0;
					if (tic[i][j] == 'O' || tic[i][j]=='.')
						xflag = 0;
				}
				if (xflag || oflag)
					break;
			}
		}
		if (!xflag && !oflag)
		{
			xflag = 1;
			oflag = 1;
			for (i=0;i<4;i++)
			{
				if (tic[i][i]=='X' || tic[i][i]=='.')
					oflag = 0;
				if (tic[i][i] == 'O' || tic[i][i]=='.')
					xflag = 0;
			}
		}

		if (!xflag && !oflag)
		{
			xflag = 1;
			oflag = 1;
			for (i=0;i<4;i++)
			{
				if (tic[4-(i+1)][i]=='X' || tic[4-(i+1)][i]=='.')
					oflag = 0;
				if (tic[4-(i+1)][i] == 'O' || tic[4-(i+1)][i]=='.')
					xflag = 0;
			}
		}

		if (xflag)
			outfile << "Case #" << n << ": X won" << endl;
		else if (oflag)
			outfile << "Case #" << n << ": O won" << endl;
		else
		{
			flag=1;
			for (i=0;i<4;i++)
				for (j=0;j<4;j++)
					if (tic[i][j] == '.')
						flag=0;
			if (flag)
				outfile << "Case #" << n << ": Draw" << endl;
			else
				outfile << "Case #" << n << ": Game has not completed" << endl;
		}
	}
    

}