#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		int R, C;
		cin >> R >> C;
		vector<string> picture(R);
		for(int i = 0; i < R; i++)
		{
			string s = "";
			for(int j = 0; j < C; j++)
			{
				char c;
				cin >> c;
				s += c;
			}
			picture[i] = s;
		}
		cout << "Case #" << t << ":" << endl; 
		bool notPossible = false;
		for(int i = 0; i < R; i++)
		{
			for(int j = 0; j < C; j++)
			{
				if(picture[i][j] == '#')
				{
					if(i + 1 >= R || j + 1 >=C)
					{
						notPossible = true;
						break;
					}
					else if(picture[i + 1][j] != '#' || picture[i][j + 1] != '#' ||  picture[i + 1][j + 1] != '#')
					{
						notPossible = true;
						break;
					}
					else
					{
						picture[i][j] = '/';
						picture[i][j + 1] = '\\';
						picture[i + 1][j] = '\\';
						picture[i + 1][j + 1] = '/';
					}
					
				}
			}
			
			if(notPossible)
				break;
				
		}
		
		if(notPossible)
		{
			cout << "Impossible" << endl;
		}
		else
		{
			for(int i = 0; i < R; i++)
			{
				for(int j = 0; j < C; j++)
					cout << picture[i][j];
					
				cout << endl;
			}
		}
	}
	
	return 0;
}
