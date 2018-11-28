#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <assert.h>
#define DIM 4

using namespace std;

void read_mat(char mat[][4], ifstream& inf)
{
	string line;
	for(int i=0; i<DIM; i++)
	{
		getline(inf, line);
		for(int j=0; j<DIM; j++)
		{
			mat[i][j] = (char) line.c_str()[j];
		}
	}

	if(inf.good())
		getline(inf, line);
}

int main(int argc, char* argv[])
{
	ifstream inf(argv[1]);
	assert(inf.is_open());

	char mat[DIM][DIM];
	string line;

	getline(inf, line);
	int T = atoi(line.c_str());
	for(int i=0; i<T; i++)
	{
		int O_rows[DIM] = {0};
		int O_cols[DIM] = {0};
		int X_rows[DIM] = {0};
		int X_cols[DIM] = {0};
		int T_rows[DIM] = {0};
		int T_cols[DIM] = {0};
		int O_diag[DIM/2] = {0};
		int X_diag[DIM/2] = {0};
		int T_diag[DIM/2] = {0};
		int dot = 0;
		char winner = '_';
		
		read_mat(mat, inf);
		winner = '_';

		for(int j=0; j<DIM; j++)	
		{
			for(int k=0; k<DIM; k++)
			{
				if(mat[j][k] == 'O')
				{
					O_rows[j]++;
				}
				else if(mat[j][k] == 'X')
				{
					X_rows[j]++;
				}
				else if(mat[j][k] == 'T')
				{
					T_rows[j]++;
				}
				else if(mat[j][k] == '.')
				{
					dot++;
				}
			}
		
			for(int k=0; k<DIM; k++)
			{
				if(mat[k][j] == 'O')
				{
					O_cols[j]++;
				}
				else if(mat[k][j] == 'X')
				{
					X_cols[j]++;
				}
				else if(mat[k][j] == 'T')
				{
					T_cols[j]++;
				}
			}
			
			if(mat[j][j] == 'O')
			{
				O_diag[0]++;
			}
			else if(mat[j][j] == 'X')
			{
				X_diag[0]++;
			}
			else if(mat[j][j] == 'T')
			{
				T_diag[0]++;
			}
			
			if(mat[j][DIM-j-1] == 'O')
			{
				O_diag[1]++;
			}
			else if(mat[j][DIM-j-1] == 'X')
			{
				X_diag[1]++;
			}
			else if(mat[j][DIM-j-1] == 'T')
			{
				T_diag[1]++;
			}
		}

		for(int j=0; j<DIM; j++)
		{
			if(O_rows[j] >= 3)
			{
				if(O_rows[j] + T_rows[j] == 4) {
					winner = 'O';
					break;
				}
			}
			if(O_cols[j] >= 3)
			{
				if(O_cols[j] + T_cols[j] == 4) {
					winner = 'O';
					break;
				}
			}
			if(X_rows[j] >= 3)
			{
				if(X_rows[j] + T_rows[j] == 4) {
					winner = 'X';
					break;
				}
			}
			if(X_cols[j] >= 3)
			{
				if(X_cols[j] + T_cols[j] == 4) {
					winner = 'X';
					break;
				}
			}
			if(j < DIM/2)
			{
				if(O_diag[j] >= 3)
				{
					if(O_diag[j] + T_diag[j] == 4) {
						winner = 'O';
						break;
					}
				}
				if(X_diag[j] >= 3)
				{
					if(X_diag[j] + T_diag[j] == 4) {
						winner = 'X';
						break;
					}
				}
			}
		}
		if(winner != '_')
		{
			cout<<"Case #"<<i+1<<": "<<winner<<" won"<<endl;
		}
		else
		{
			if(dot > 0)
			{
				cout<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;
			}
			else
			{
					cout<<"Case #"<<i+1<<": "<<"Draw"<<endl;
			}
		}
	}
	inf.close();
	return 0;
}
