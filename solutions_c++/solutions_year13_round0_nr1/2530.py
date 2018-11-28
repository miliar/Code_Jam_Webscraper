#pragma comment(linker, "/STACK:500000000")
#include <algorithm>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <math.h>
#include <set>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define y0 y123
#define y1 y1234
#define ll long long
#define PI 3.1415926535897932384626433832795
#define EPS 1e-9
#define INF 2147483647
#define MOD 1000000007
#define N 15
#define M 1305

int gcd(int a, int b) { return (!b) ? a : gcd(b, a % b); }
int lcm(int a, int b) { return a / gcd(a,b) * b; }

int t;
char a[N][N];
bool eq(char a, char b)
{
	if(a == '.' || b == '.') return false;
	if(a == 'T' || b == 'T') return true;
	return a == b;
}
int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	scanf("%d%*c", &t);
	for(int tt = 1; tt <= t; tt++)
	{
		for(int i = 0; i < 4; i++)
			gets(a[i]);
		scanf("%*c");
		int x = 0, o = 0;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
			{
				if(a[i][j] == 'X') x++;
				else if(a[i][j] == 'O') o++;
			}
		bool x_win = 0, o_win = 0;
		for(int i = 0; i < 4; i++)
			if(eq(a[i][0], a[i][1]) && eq(a[i][1], a[i][2]) && eq(a[i][2], a[i][3]) && eq(a[i][3], a[i][0]))
			{
				for(int j = 0; j < 4; j++)
					if(a[i][j] != 'T')
					{
						if(a[i][j] == 'X') x_win = 1;
						else o_win = 1;
						break;
					}
			}
		for(int j = 0; j < 4; j++)
			if(eq(a[0][j], a[1][j]) && eq(a[1][j], a[2][j]) && eq(a[2][j], a[3][j]) && eq(a[3][j], a[0][j]))
			{
				for(int i = 0; i < 4; i++)
					if(a[i][j] != 'T')
					{
						if(a[i][j] == 'X') x_win = 1;
						else o_win = 1;
						break;
					}
			}
		if(eq(a[0][0], a[1][1]) && eq(a[1][1], a[2][2]) && eq(a[2][2], a[3][3]) && eq(a[3][3], a[0][0]))
		{
			if(a[0][0] == 'X') x_win = 1;
			if(a[0][0] == 'O') o_win = 1;
			if(a[1][1] == 'X') x_win = 1;
			if(a[1][1] == 'O') o_win = 1;
			if(a[2][2] == 'X') x_win = 1;
			if(a[2][2] == 'O') o_win = 1;
			if(a[3][3] == 'X') x_win = 1;
			if(a[3][3] == 'O') o_win = 1;
		}
		if(eq(a[0][3], a[1][2]) && eq(a[1][2], a[2][1]) && eq(a[2][1], a[3][0]) && eq(a[3][0], a[0][3]))
		{
			if(a[0][3] == 'X') x_win = 1;
			if(a[0][3] == 'O') o_win = 1;
			if(a[1][2] == 'X') x_win = 1;
			if(a[1][2] == 'O') o_win = 1;
			if(a[2][1] == 'X') x_win = 1;
			if(a[2][1] == 'O') o_win = 1;
			if(a[3][0] == 'X') x_win = 1;
			if(a[3][0] == 'O') o_win = 1;
		}
		printf("Case #%d: ", tt);
		if(x + o < 15)
		{
			if(!x_win && !o_win)
				puts("Game has not completed");
			else 
			{
				if(x_win && o_win) puts("Draw");
				else if(x_win) puts("X won");
				else puts("O won");
			}
		}
		else
		{
			if(x_win == o_win)
				puts("Draw");
			else if(x_win) puts("X won");
			else puts("O won");
		}
	}
	return 0;
}