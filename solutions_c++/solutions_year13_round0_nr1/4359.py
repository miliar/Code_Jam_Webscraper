#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>
#include <iomanip>
#include <string>
#include <sstream>
#include <set>
#include <cmath>
#include <map>
#include <cstdio>
using namespace std;
#define ll long long

struct str
{
	int x, o, t;
	str(int _x = 0, int _o = 0, int _t = 0)
	{
		x = _x;
		o = _o;
		t = _t;
	}
};

string s[8];
str all[16];

int main()
{
	int test, dot;
	cin >> test;
	for(int cas = 1; cas <= test; cas ++)
	{
		dot = 0;
		for(int i = 0; i < 4; i ++)
		{
			cin >> s[i];
			for(int j = 0; j < 4; j ++)
				dot += s[i][j] == '.';
		}
		
		str b;
		int idx = 0;
		for(int i = 0; i < 4; i ++)
		{
			b.x = b.o = b.t = 0;
			for(int j = 0; j < 4; j ++)
			{
				b.x += s[i][j] == 'X';
				b.o += s[i][j] == 'O';
				b.t += s[i][j] == 'T';
			}
			all[idx ++] = b;
		}
		for(int j = 0; j < 4; j ++)
		{
			b.x = b.o = b.t = 0;
			for(int i = 0; i < 4; i ++)
			{
				b.x += s[i][j] == 'X';
				b.o += s[i][j] == 'O';
				b.t += s[i][j] == 'T';
			}
			all[idx ++] = b;
		}
		int i, j;
		i = j = 0;
		b.x = b.o = b.t = 0;
		while(i < 4)
		{
			b.x += s[i][j] == 'X';
			b.o += s[i][j] == 'O';
			b.t += s[i][j] == 'T';		
			i ++;
			j ++;
		}
		all[idx ++] = b;
		
		i = 0;
		j = 3;
		b.x = b.o = b.t = 0;
		while(i < 4)
		{
			b.x += s[i][j] == 'X';
			b.o += s[i][j] == 'O';
			b.t += s[i][j] == 'T';		
			i ++;
			j --;
		}
		all[idx ++] = b;
		
		printf("Case #%d: ", cas);
		bool print = false;
		for(int i = 0; i < idx; i ++)
		{
			if( all[i].x + all[i].t == 4 )
			{
				printf("X won\n");
				print = true;
				break;
			}
			else if(all[i].o + all[i].t == 4)
			{
				printf("O won\n");
				print = true;
				break;
			}
		}
		if(print == true)
			continue;
		if(dot == 0)
		{
			printf("Draw\n");
		}
		else
		{
			printf("Game has not completed\n");
		}
	}
	return 0;
}



