#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

typedef long long LL;

int x, y;
char s[1000];
int a[10000][2];
int N, ans;
bool nn[10000];

int get_num(int y1, int x1)
{
	y1 = (y1 + y) % y;
	x1 = (x1 + x) % x;
	return y1*x + x1;
}

void rec(int x)
{
	if (x==N)
	{
		ans++;
	}
	else
	{
		if (!nn[ a[x][0] ])
		{
			nn[ a[x][0] ] = true;
			rec(x + 1);
			nn[ a[x][0] ] = false;
		}
		if (!nn[ a[x][1] ])
		{
			nn[ a[x][1] ] = true;
			rec(x + 1);
			nn[ a[x][1] ] = false;
		}
	}
}

int main()
{
    int tc;
	//freopen("c.in", "r", stdin);
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt)
    {
		scanf("%i %i", &y, &x);
		for(int j=0; j<y; ++j)
		{
			scanf("%s", s);
			for(int i=0; i<x; ++i)
			{
				int num = get_num(j, i);
				switch(s[i])
				{
				case '-':{
							a[num][0] = get_num(j, i - 1);
							a[num][1] = get_num(j, i + 1);
							break;
						 }
				case '|':{
							a[num][0] = get_num(j - 1, i);
							a[num][1] = get_num(j + 1, i);
							break;
						 }
				case '/':{
							a[num][0] = get_num(j - 1, i + 1);
							a[num][1] = get_num(j + 1, i - 1);
							break;
						 }
				case 92:{
							a[num][0] = get_num(j - 1, i - 1);
							a[num][1] = get_num(j + 1, i + 1);
							break;
						 }
				}
			}
		}
		ans = 0;
		N = x*y;
		memset(nn, 0, sizeof(nn));
		rec(0);	
        printf("Case #%i: %i\n", tt, ans);
    }
}