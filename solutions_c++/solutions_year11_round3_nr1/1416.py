#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  

using namespace std;

int main()
{
	int T;
	std::cin >> T;
	int case_num = 1;

	while(case_num <= T)
	{
		int R,C;
		std::cin >> R >> C;
		vector<vector<char> > table;
		for(int i = 0 ; i < R; i++)
		{
			vector<char> row;
			char c;
			for(int j = 0 ; j < C; j++)
			{
				std::cin >> c ;
				row.push_back(c);
			}
			table.push_back(row);
		}
		int possible = 1;
		for(int i = 0 ; i < R; i++)
		{
			if(possible == 0)
				break;
			for(int j = 0 ; j < C; j++)
			{
				if(possible == 0)
				break;
				if(table[i][j] == '#')
				{
					if(i+1 < R && j+1 < C)
					{
						if(table[i+1][j] == '#' && table[i][j+1] == '#' && table[i+1][j+1] == '#')
						{
							table[i][j] = '/' ; table[i][j+1] = '\\';
							table[i+1][j] = '\\'; table[i+1][j+1] = '/';
						}
						else
						{
							possible = 0;
							break;
						}
					}
					else
					{
						possible = 0;
						break;
					}
				}
			}
		}
		std::cout << "Case #" << case_num << ": " << std::endl;
		if(possible ==0)
		{
		std::cout << "Impossible" << std::endl;
		}
		else
		{
			for(int i = 0 ; i < R; i++)
				{
					for(int j = 0 ; j < C; j++)
					{
						std::cout << table[i][j];
					}
					std::cout << std::endl;
				}
		}
		case_num++;
	}
	std::cin >> T;
	return 1;
}