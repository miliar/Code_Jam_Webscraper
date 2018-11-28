#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <stdio.h>

#define forp(a,b,i) for (int i = a; i < b; i++)
#define pb push_back
#define mp make_pair

using namespace std;

int r,c;
char grid[100][100];
char grid2[100][100];

int main()	{

	int t;
	cin >> t;
	forp(0,t,z)	{
		
		cin >> r >> c;
		forp(0,r,i)	{
			forp(0,c,j)	{
				cin >> grid[i][j];
				grid2[i][j] = grid[i][j];
			}
		}
		
		bool impossible = false;
		
		forp(0,r,i)	{
			forp(0,c,j)	{
				if (grid2[i][j] == '#')	{
					grid2[i][j] = '/';
					grid2[i+1][j] = '\\';
					grid2[i][j+1] = '\\';
					grid2[i+1][j+1] = '/';
					if (i + 1 >= r || j +1 >= c)	{
						impossible = true;
					}
				} else if (grid2[i][j] == '.'){
					grid2[i][j] = '.';
				}
				if (impossible)
					break;
			}
			if (impossible)
				break;
		}
		
		forp(0,r,i)	{
			forp(0,c,j)	{
				if (grid[i][j] == '.' && grid2[i][j] != '.')
					impossible = true;
				
				if (impossible)
					break;
			}
			if (impossible)
					break;
		}
		
		cout << "Case #" << (z+1) <<":" << endl;
		if (impossible)	{
			cout << "Impossible" << endl;
		} else	{
			forp(0,r,i)	{
				forp(0,c,j)	{
					cout << grid2[i][j];
				}
				cout << endl;
			}
		}
	}
}