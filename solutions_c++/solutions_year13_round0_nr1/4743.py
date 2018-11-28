#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <string>
#include <fstream>

using namespace std;

#define maxx(a, b) ((a > b)? a: b)
#define minn(a, b) ((a < b)? a: b)
#define round(a) (int)(a + 0.5)

int get_powers(long long n, int p)
{
    int res = 0;
    for (long long power = p ; power <= n ; power *= p)
        res += n/power;
    return res;
}

int main()
{
	//cout << pr <<endl;
	freopen("input.txt","r", stdin);
	freopen("output.txt", "w" , stdout);

	int T, ind = 0;
	scanf("%d", &T);
	char b[5][5];
	while(ind++ < T)
	{
		string oup = "";
		bool dots = false;
		int xc = 0, oc = 0, tc = 0, dc = 0;
		for(int i = 0;i < 4;i++)
		{
			xc = oc = tc = dc = 0;
			scanf("%s\n", b[i]);
			
			for(int j = 0;j < 4;j++)
			{
				switch (b[i][j])
				{
				case 'X':
					xc++;
					break;
				case 'O':
					oc++;
					break;
				case 'T':
					tc++;
					break;
				case '.':
					dc++;
					dots = true;
					break;
				}
			}
			if(xc == 4 || (xc == 3 && tc == 1))
			{
				oup = "X won";
			}
			else if(oc == 4 || (oc == 3 && tc == 1))
			{
				oup = "O won";
			}
		}
		for(int j = 0;j < 4;j++)
		{
			xc = oc = tc = dc = 0;
			for(int i = 0;i < 4;i++)
			{
				//for(int j = 0;j < 4;j++)
				{
					switch (b[i][j])
					{
					case 'X':
						xc++;
						break;
					case 'O':
						oc++;
						break;
					case 'T':
						tc++;
						break;
					case '.':
						dc++;
						dots = true;
						break;
					}
				}
			}
			if(xc == 4 || (xc == 3 && tc == 1))
			{
				oup = "X won";
			}
			else if(oc == 4 || (oc == 3 && tc == 1))
			{
				oup = "O won";
			}
		}
		xc = oc = tc = dc = 0;
		for(int i = 0, j = 0;i < 4, j < 4;i++, j++)
		{
			
			//for(int j = 0;j < 4;j++)
			{
				switch (b[i][j])
				{
				case 'X':
					xc++;
					break;
				case 'O':
					oc++;
					break;
				case 'T':
					tc++;
					break;
				case '.':
					dc++;
					dots = true;
					break;
				}
			}
		}
		if(xc == 4 || (xc == 3 && tc == 1))
		{
			oup = "X won";
		}
		else if(oc == 4 || (oc == 3 && tc == 1))
		{
			oup = "O won";
		}
		xc = oc = tc = dc = 0;
			
		for(int i = 0, j = 3;i < 4, j >= 0;i++, j--)
		{
			//for(int j = 0;j < 4;j++)
			{
				switch (b[i][j])
				{
				case 'X':
					xc++;
					break;
				case 'O':
					oc++;
					break;
				case 'T':
					tc++;
					break;
				case '.':
					dc++;
					dots = true;
					break;
				}
			}
			
		}
		if(xc == 4 || (xc == 3 && tc == 1))
		{
			oup = "X won";
		}
		else if(oc == 4 || (oc == 3 && tc == 1))
		{
			oup = "O won";
		}
		if(oup != "")
		{
			printf("Case #%d: %s\n", ind, oup.c_str());
		}
		else if(dots)
		{
			printf("Case #%d: Game has not completed\n", ind);
		}
		else
		{
			printf("Case #%d: Draw\n", ind);
		}
	}
	
    return 0;
}
