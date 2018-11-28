#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

char data[4][4];
int main()
{
	
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int n;
	cin>>n;
	map<char, int> m;
	m.insert(make_pair('X', 100));
	m.insert(make_pair('O', 10));
	m.insert(make_pair('T', -1));
	m.insert(make_pair('.', 0));
	for(int k=0; k<n; k++)
	{
		int result = 4;
		int o_num = 0, x_num = 0;
		int nodot = 1;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
				cin>>data[i][j];
		}
		int sum = 0;
		for(int x=0; x<4; x++)
		{
			sum = 0;
			for(int y=0; y<4; y++)
				sum += m[data[x][y]];
			if(sum == 299 || sum == 198 || sum == 97 || sum == 400)
			{
				result = 1;
			}
			else if(sum == 40 || sum == 29 || sum == 18 || sum == 7)
			{
				result = 2;
			}
		}
		for(int x=0; x<4; x++)
		{
			sum = 0;
			for(int y=0; y<4; y++)
			{
				sum += m[data[y][x]];
				if(data[y][x] == '.')
					nodot = 0;
			}
			if(sum == 299 || sum == 198 || sum == 97 || sum == 400)
			{
				result = 1;
			}
			else if(sum == 40 || sum == 29 || sum == 18 || sum == 7)
			{
				result = 2;
			}
		}
		sum = 0;
		for(int x=0; x<4; x++)
		{
			sum += m[data[x][x]];
		}
		if(sum == 299 || sum == 198 || sum == 97 || sum == 400)
		{
			result = 1;
		}
		else if(sum == 40 || sum == 29 || sum == 18 || sum == 7)
		{
			result = 2;
		}
		sum = 0;
		sum = m[data[0][3]] + m[data[3][0]] + m[data[1][2]] + m[data[2][1]];
		if(sum == 299 || sum == 198 || sum == 97 || sum == 400)
		{
			result = 1;
		}
		else if(sum == 40 || sum == 29 || sum == 18 || sum == 7)
		{
			result = 2;
		}
		if(nodot == 1 && result == 4)
			result = 3;
		switch(result)
		{
		case 1:
			printf("Case #%d: X won\n", k+1);
			break;
		case 2:
			printf("Case #%d: O won\n", k+1);
			break;
		case 3:
			printf("Case #%d: Draw\n", k+1);
			break;
		case 4:
			printf("Case #%d: Game has not completed\n", k+1);
			break;

		}
		
	}

	//fclose(stdout);
	//fclose(stdin);
	return 0;
}

