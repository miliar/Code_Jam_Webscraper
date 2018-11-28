#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
using namespace std;

// #define input cin
// #define output cout
ifstream input("A-large.in");
ofstream output("A-large-out.txt");

int T, R, C;
char map[55][55];


int main()
{
	input >> T;
	int count;
	for(count = 0; count < T; count ++)
	{
		input >> R>>C;
		int i,j;
		for(i = 0; i < R; i++)
		{
			for(j = 0; j < C; j++)
			{
				input >> map[i][j];
			}
		}
		bool flag = true;
		for(i = 0; i < R; i++)
		{
			for(j = 0; j < C; j++)
			{
				if(map[i][j] == '#')
				{
					if(map[i][j+1] == '#' && map[i+1][j] == '#' && map[i+1][j+1] == '#')
					{
						map[i][j] = map[i+1][j+1] = '/';
						map[i][j+1] = map[i+1][j] = '\\';
					}
					else
					{
						flag = false;
						break;
					}
				}
			}
			if(!flag)
				break;
		}
		output << "Case #" << count+1 << ":"<<endl;
		if(!flag)
			output<<"Impossible"<<endl;
		else
		{
			for(i = 0; i < R; i++)
			{
				for(j = 0; j < C; j++)
				{
					output << map[i][j];
				}
				output << endl;
			}
		}
	}
	return 0;
}