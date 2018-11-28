
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

bool isPossible(int R, int C, vector<vector<char>> vec)
{
	int i, j, k;
	//bool t = true;
	
	int row, column; 
	for(i = 0; i < R; i++)
	{
		for(j = 0; j < C; j++)
		{
			if(vec[i][j] == '#')
			{
				row = 1;
				column = 1; 
				
				k = i - 1;
				while(k > -1)
				{
					if(vec[k][j] == '#')
						row++;
					else break;
					k--;
				}

				k = i+1;
				while(k < R)
				{
					if(vec[k][j] == '#')
						row++;
					else break; 
					k++;
				}

				if(row %2 == 1)
					return false;

				//col
				row = 1;
				column = 1; 
				
				k = j - 1;
				while(k > -1)
				{
					if(vec[i][k] == '#')
						column++;
					else break;
					k--;
				}

				k = j+1;
				while(k < C)
				{
					if(vec[i][k] == '#')
						column++;
					else break; 
					k++;
				}

				if(column %2 == 1)
					return false;
			}
		}
	}

	return true; 
}

int main()
{
	ifstream in ("A-large.in");
	ofstream out ("A-large.out");

	string s;

	int T;
	in >> T;

	getline(in, s); 
	
	int i, j, k;

	for(i = 0; i < T; i++)
	{
		int R, C;
		in >> R >> C;

		getline(in, s);
		
		vector<vector<char>> vec; 
		char ch;
 		for(j = 0; j < R; j++)
		{
			vector<char> v;
			for(k = 0; k < C; k++)
			{
				in >> ch;
				v.push_back(ch);
			}
			vec.push_back(v);
			getline(in, s); 
		}
		
		bool t = isPossible(R, C, vec);
		
		if(t)
		{
			out << "Case #" << i+1 <<":" << endl; 
			for(j = 0; j < R; j++)
			{
				for(k = 0; k < C; k++)
				{
					if(vec[j][k] == '#')
					{
						vec[j][k] = '/';
						vec[j+1][k] = '\\';
						vec[j][k+1] = '\\';
						vec[j+1][k+1] = '/';
					}
					out << vec[j][k];
				}
				out << endl;
			}
		}
		else 
		{
			out << "Case #" << i+1 <<":" << endl << "Impossible" << endl;

		}
	}

	return 0;
}