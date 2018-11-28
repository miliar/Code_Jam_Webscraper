
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>

using namespace std;

ifstream fin("Rotate.txt");
#define cin fin

ofstream fout("output.txt");
#define cout fout

int n, k;
char grid[220][220];
char rotated[220][220];

void rotate()
{
	int i, j;
	for(i=0; i<n; i++)
	{
		for(j=0; j<n; j++)
		{
			//ii = new row
			//jj = new column
			int ii, jj;
			ii = j;
			jj = n - 1 - i;
			rotated[ii][jj] = grid[i][j];
		}
	}
}

void applyGravity()
{
	int i, j, kk;
	for(kk=0; kk<n; kk++)
	{
		for(j=0; j<n; j++)
		{
			for(i=n-2; i>=0; i--)
			{
				if(rotated[i][j] != '.' && rotated[i+1][j] == '.')
				{
					rotated[i+1][j] = rotated[i][j];
					rotated[i][j] = '.';
				}
			}
		}
	}
}

int check(char c, int i, int j, int di, int dj)
{
	int ii, jj;
	ii = i + di;
	jj = j + dj;

	if(ii < 0 || ii >= n || jj < 0 || jj >= n)
	{
		return 0;
	}

	if(rotated[ii][jj] == c)
	{
		return check(c, ii, jj, di, dj) + 1;
	}

	return 0;
}

int main()
{
	int t, i, j, kk, kkk;
	cin>>t;
	for(kk=0; kk<t; kk++)
	{
		cin>>n>>k;
		for(i=0; i<n; i++)
		{
			for(j=0; j<n; j++)
			{
				grid[i][j] = rotated[i][j] = '.';
				cin>>grid[i][j];
			}
		}
		rotate();
		//for(i=0; i<n; i++)
		//{
		//	for(j=0; j<n; j++)
		//	{
		//		cout<<rotated[i][j];
		//	}
		//	cout<<endl;
		//}
		//cout<<endl;
		applyGravity();
		//for(i=0; i<n; i++)
		//{
		//	for(j=0; j<n; j++)
		//	{
		//		cout<<rotated[i][j];
		//	}
		//	cout<<endl;
		//}
		//cout<<endl;

		int di[] = {0, 1, 1, 1};
		int dj[] = {1, 0, -1, 1};

		bool r = 0, b = 0;
		for(i=0; i<n; i++)
		{
			for(j=0; j<n; j++)
			{
				for(kkk=0; kkk<4; kkk++)
				{

					if(rotated[i][j] == 'R')
						r = r | (check('R', i, j, di[kkk], dj[kkk]) + 1 >= k);
					if(rotated[i][j] == 'B')
						b = b | (check('B', i, j, di[kkk], dj[kkk]) + 1 >= k);
				}
			}
		}

		string out[] = {"Neither", "Red", "Blue", "Both"};
		int res = r + (b << 1);
		cout<<"Case #"<<kk+1<<": "<<out[res]<<endl;

	}

	return 0;
}