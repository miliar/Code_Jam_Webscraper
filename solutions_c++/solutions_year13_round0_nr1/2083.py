#pragma comment(linker, "/STACK:1000000000")
#define _CRT_SECURE_NO_WARNINGS
#include "iostream"
#include "vector"
#include "algorithm"
#include "string"
#include "cstring"
#include "cstdlib"
#include "fstream"
#include "cmath"
#include "stack"
#include "bitset"
#include "queue"
#include "map"
#include "set"
#include <stdio.h>
#include <time.h>

using namespace std;
#define REP(i,b) for(int i=0; i<b;i++)
#define FOR(i,a,b) for(int i=a; i<=b;i++)
#define mp make_pair
#define pb push_back
#define X  first
#define Y  second
#define eps 0.000000001
typedef long long LL;
typedef unsigned long long ULL;
const int size = 1000010;
const LL alphabet = 130;
const LL INF =  1000000000;
const double pi = 4 * atan(1.0);
const LL MOD = 1000000007;

LL n, m, k;
int d[size];
int mas[10][10];

int main()
{
	#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif
	cin >> n;
	char ch;
	REP(k,n)
	{
		memset(mas,0,sizeof(mas));
		REP(i,4)
			REP(j,4)
			{
				cin >> ch;
				if (ch == 'X')
					mas[i][j] = -100;
				if (ch == 'O')
					mas[i][j] = 100;
				if (ch == 'T')
					mas[i][j] = 50;
			}
		int diag1 = mas[0][0] + mas[1][1]+ mas[2][2]+ mas[3][3], diag2 = mas[0][3] + mas[1][2]+mas[2][1]+mas[3][0];
		bool draw = 1, out = 0;
		REP(i,4)
		{
			int tmp1 = 0, tmp2 = 0;
			REP(j,4)
			{
				tmp1 += mas[i][j];
				tmp2 += mas[j][i];
				if (mas[i][j] == 0 || mas[j][i] == 0)
					draw = 0;
			}
			if (tmp1 == -400 || tmp1 == -250 || tmp2 == -400 || tmp2 == -250 || diag1 == -400 || diag1 == -250 || diag2 == -400 || diag2 == -250)
			{
				printf("Case #%d: X won\n", k+1), out = 1;
				break;
			}
			if (tmp1 == 400 || tmp1 == 350 || tmp2 == 400 || tmp2 == 350 || diag1 == 400 || diag1 == 350 || diag2 == 400 || diag2 == 350)
			{
				printf("Case #%d: O won\n", k+1), out = 1;
				break;
			}
		}
		if (!out && draw)
			printf("Case #%d: Draw\n", k+1), out = 1;
		if (!out && !draw)
			printf("Case #%d: Game has not completed\n", k+1), out = 1;
	}
	return 0;
}