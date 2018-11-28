#include<iostream>
#include<vector>
#include <algorithm>
#include <stack>
#include <string>
#include <utility>
#include <map>

using namespace std;

int main()
{
	int tests;
	cin >> tests;
	for(int j = 0; j < tests; j++)
	{
		int R, C;
		cin >> R >> C;
		char matrix[R][C+1];
		bool possible = true;
		for(int i = 0; i < R; i++)
		{
			string line;
			cin >> line;
			for(int k = 0; k < C; k++)
			{
				matrix[i][k] = line[k];
			}
			matrix[i][C] = '\0';
		}
		for(int i = 0; i < R; i++)
		{
			char line[C];
			for(int k = 0; k < C; k++)
			{
				if(matrix[i][k] =='#')
				{
					if(matrix[i][k+1]== '#' && matrix[i+1][k+1]== '#' && matrix[i+1][k]== '#')
					{
						matrix[i][k] = '/';
						matrix[i+1][k] = '\\';
						matrix[i][k+1] = '\\';
						matrix[i+1][k+1] = '/';
					}
					else
					{
						possible = false;
					}
				}
			}
		}
		here:
		if(possible)
		{
			printf("Case #%d:\n",j+1);
			for(int i = 0; i < R; i++)
			{
				printf("%s\n",matrix[i]);
			}
		}
		else
			printf("Case #%d:\nImpossible\n",j+1);
	}
}