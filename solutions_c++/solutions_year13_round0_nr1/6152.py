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
	freopen("A-large.in", "rt", stdin); 
	freopen("A-large.out", "wt", stdout);
	int t;
	cin >> t;
	int c=1;
	while(t--)
	{
		int x,y;
		bool x1,y1,dot;
		x1=y1=dot=false;
		vector<string> v(4);
		for(int i=0;i<4;i++)
			cin >> v[i];
		for(int i=0;i<4;i++)
		{
			x=y=0;
			for(int j=0;j<4;j++)
			{
				if(v[i][j] == 'X')
					x++;
				else if(v[i][j] == 'O')
					y++;
				else if(v[i][j] == 'T')
				{
					x++;
					y++;
				}
				else
					dot=true;
			}
			if(x == 4)
			{
				x1=true;
			}
			else if(y==4)
			{
				y1=true;
			}

		}
		if(!(x1 || y1))
		{
			for(int i=0;i<4;i++)
			{
				x=y=0;
				for(int j=0;j<4;j++)
				{
					if(v[j][i] == 'X')
						x++;
					else if(v[j][i] == 'O')
						y++;
					else if(v[j][i] == 'T')
					{
						x++;
						y++;
					}
				}
				if(x == 4)
				{
					x1=true;
				}
				else if(y==4)
				{
					y1=true;
				}

			}
			if(!(x1 || y1))
			{
			x=y=0;
			for(int i=0;i<4;i++)
			{
				if(v[i][i] == 'X')
					x++;
				else if(v[i][i] == 'O')
					y++;
				else if(v[i][i] == 'T')
				{
					x++;
					y++;
				}
			}
			if(x==4)
				x1=true;
			else if(y==4)
				y1=true;
			else
			{
				x=y=0;
				for(int i=0,j=3;i<4;i++,j--)
				{
					if(v[i][j] == 'X')
						x++;
					else if(v[i][j] == 'O')
						y++;
					else if(v[i][j] == 'T')
					{
						x++;
						y++;
					}
				}

				if(x==4)
					x1=true;
				else if(y==4)
					y1=true;
			}
		}
		}
		cout << "Case #" << c << ": " ;
		if(x1)
			cout << "X won\n";
		else if(y1)
			cout << "O won\n";
		else if(dot)
			cout << "Game has not completed\n";
		else
			cout << "Draw\n";
		c++;
	}
	return 0;
}