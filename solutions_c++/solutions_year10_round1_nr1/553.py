#include <cstdio>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cstring>
#include <cmath>
#include <string>
#include <queue>
#include <cassert>
using namespace std;
#define PB push_back
#define LL long long
#define ULL unsigned LL
#define LD long double

#define MR 60
int n, k;
char t[MR][MR], t1[MR][MR];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		scanf("%d%d", &n, &k);
		for(int i = 0; i < n; i++)
			scanf("%s", t1[i]);
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
				t[j][i] = t1[n-i-1][j];
		//grawitacja
		for(int i = 0; i < n; i++)
		{
			int j = n-1;	//pozycja, na ktora trzeba zrzucac
			while(j >= 0)
			{
				//podwyzszaj j
				while(j >= 0 && t[j][i] != '.')j--;
				int l = j-1;
				while(l >= 0 && t[l][i] == '.')l--;
				while(l >= 0 && t[l][i] != '.')
				{
					t[j][i] = t[l][i];
					t[l][i] = '.';	//aktualnie jest wolne
					j--;
					l--;
				}	
				if(l < 0)
					break;
			}
		}
		bool blue = 0, red = 0;
		//po wierszach
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n;)
			{
				int l = j + 1;
				while(l < n && t[i][l] == t[i][j])l++;
				if(l - j >= k)
				{
					if(t[i][j] == 'B')
						blue = 1;
					else if(t[i][j] == 'R')
						red = 1;
				}
				j = l;
			}
		}
		//po kolumnach
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n;)
			{
				int l = j + 1;
				while(l < n && t[l][i] == t[j][i])l++;
				if(l - j >= k)
				{
					if(t[j][i] == 'B')
						blue = 1;
					else if(t[j][i] == 'R')
						red = 1;
				}
				j = l;
			}
		}
		//po przekatnych /
		for(int i = 0; i < n; i++)
		{
			int col = 0;
			for(int j = i; j >= 0;)
			{
				int l = j - 1, col1 = col + 1;
				while(l >= 0 && t[j][col] == t[l][col1])
				{
					l--;
					col1++;
				}
				if(j - l >= k)
				{
					if(t[j][col] == 'B')
						blue = 1;
					else if(t[j][col] == 'R')
						red = 1;
				}
				j = l;
				col = col1;
			}
		}
		for(int i = 0; i < n; i++)
		{
			int raw = n-1;
			for(int j = i; j < n;)
			{
				int l = j + 1, raw1 = raw - 1;
				while(l < n && t[raw][j] == t[raw1][l])
				{
					l++;
					raw1--;
				}
				if(l - j >= k)
				{
					if(t[raw][j] == 'B')
						blue = 1;
					else if(t[raw][j] == 'R')
						red = 1;
				}
				j = l;
				raw = raw1;
			}
		}
		//po przekatnych
		for(int i = 0; i < n; i++)
		{
			int col = i;
			for(int j = 0; col < n;)
			{
				int l = j + 1, col1 = col + 1;
				while(col1 < n && t[j][col] == t[l][col1])
				{
					l++;
					col1++;
				}
				if(l - j >= k)
				{
					if(t[j][col] == 'B')
						blue = 1;
					else if(t[j][col] == 'R')
						red = 1;
				}
				j = l;
				col = col1;
			}
		}
		for(int i = 0; i < n; i++)
		{
			int raw = i;
			for(int j = 0; raw < n;)
			{
				int l = j + 1, raw1 = raw + 1;
				while(raw1 < n && t[raw][j] == t[raw1][l])
				{
					l++;
					raw1++;
				}
				if(l - j >= k)
				{
					if(t[raw][j] == 'B')
						blue = 1;
					else if(t[raw][j] == 'R')
						red = 1;
				}
				j = l;
				raw = raw1;
			}
		}
		if(blue && red)
			printf("Case #%d: Both\n", c+1);
		else if(blue)
			printf("Case #%d: Blue\n", c+1);
		else if(red)
			printf("Case #%d: Red\n", c+1);
		else
			printf("Case #%d: Neither\n", c+1);
	}
	return 0;
}