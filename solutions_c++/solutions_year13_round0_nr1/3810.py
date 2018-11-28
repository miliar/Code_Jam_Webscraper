#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <string>
#include <queue>
#include <bitset>		//UWAGA - w czasie kompilacji musi byc znany rozmiar wektora - nie mozna go zmienic
#include <cassert>
#include <iomanip>		//do setprecision
#include <ctime>
#include <complex>
using namespace std;

#define FOR(i,b,e) for(int i=(b);i<(e);++i)
#define FORQ(i,b,e) for(int i=(b);i<=(e);++i)
#define FORD(i,b,e) for(int i=(b)-1;i>=(e);--i)
#define REP(x, n) for(int x = 0; x < (n); ++x)

#define ST first
#define ND second
#define PB push_back
#define MP make_pair
#define LL long long
#define ULL unsigned LL
#define LD long double

const double pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342;

char t[4][4];

string result()
{	
	//diagonals
	int countX = 0, countO = 0, countT = 0;
	REP(i,4)
	{
		countX += (t[i][i] == 'X');
		countO += (t[i][i] == 'O');
		countT += (t[i][i] == 'T');
	}
	if(countX == 4 || (countX == 3 && countT == 1)) return "X won";
	if(countO == 4 || (countO == 3 && countT == 1)) return "O won";
	countX = 0, countO = 0, countT = 0;
	REP(i,4)
	{
		countX += (t[i][3-i] == 'X');
		countO += (t[i][3-i] == 'O');
		countT += (t[i][3-i] == 'T');
	}
	if(countX == 4 || (countX == 3 && countT == 1)) return "X won";
	if(countO == 4 || (countO == 3 && countT == 1)) return "O won";
	REP(i,4)
	{		
		countX = 0, countO = 0, countT = 0;
		REP(j,4)
		{
			countX += (t[i][j] == 'X');
			countO += (t[i][j] == 'O');
			countT += (t[i][j] == 'T');
		}
		if(countX == 4 || (countX == 3 && countT == 1)) return "X won";
		if(countO == 4 || (countO == 3 && countT == 1)) return "O won";
		countX = 0, countO = 0, countT = 0;
		REP(j,4)
		{
			countX += (t[j][i] == 'X');
			countO += (t[j][i] == 'O');
			countT += (t[j][i] == 'T');
		}
		if(countX == 4 || (countX == 3 && countT == 1)) return "X won";
		if(countO == 4 || (countO == 3 && countT == 1)) return "O won";
	}
	bool empty = 0;
	REP(i,4)REP(j,4) if(t[i][j] == '.') empty = 1;
	if(empty)return "Game has not completed";		
	return "Draw";
}

int main()
{
	int T;
	scanf("%d", &T);
	REP(c,T)
	{
		scanf("%s%s%s%s", t[0], t[1], t[2], t[3]);		
		printf("Case #%d: %s\n", c+1, result().c_str());
	}
	return 0;
}