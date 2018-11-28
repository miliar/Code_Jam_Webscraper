/*
ID: piotrso1
PROG: temp
LANG: C++
*/

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

using namespace std;

int K = 1 << 0;
int X = 1 << 1;
int T = 1 << 2;

bool is_inc(char arr[][5])
{
	REP(i, 4)
	{

		REP(k, 4)
		{

			if(arr[i][k] == '.')
			{
				return true;
			}
		}
	}
	return false;
}


bool is_solveable(char s, char arr[][5])
{
	bool result = false;

	//
	REP(i, 4)
	{
		bool ok = true;
		REP(k, 4)
		{
			if(arr[i][k] != s && arr[i][k] != 'T')
			{
				ok = false;
			}
		}
		if(ok)
			result = true;
	}
	//
	REP(k, 4)
	{
		bool ok = true;
		REP(i, 4)
		{
			if(arr[i][k] != s && arr[i][k] != 'T')
			{
				ok = false;
			}
		}
		if(ok)
			result = true;
	}
	//
	bool ok = true;
	REP(k, 4)
	{
		if(arr[k][k] != s && arr[k][k] != 'T')
		{
			ok = false;
		}

	}
	if(ok)
		result = true;
	//
	ok = true;
	REP(k, 4)
	{
		if(arr[k][3 - k] != s && arr[k][3 - k] != 'T')
		{
			ok = false;
		}

	}
	if(ok)
		result = true;

	return result;
}

void solve(int c, FILE * fin, FILE * fout)
{
	char arr[4][5];
	REP(i, 4)
	{
		fscanf(fin, "%s", arr[i]);
	}
	bool inc = is_inc(arr);
	bool x_won = is_solveable('X', arr);
	bool o_won = is_solveable('O', arr);

	string res = "";
	if(x_won)
	{
		res = "X won";
	}
	else if(o_won)
	{
		res = "O won";
	}
	else if(inc)
	{
		res = "Game has not completed";
	}
	else
	{
		res = "Draw";
	}



	fprintf(fout, "Case #%d: %s\n", c + 1, res.c_str());

}

int main() {
    	
	FILE *fin, *fout;
    
	fin = fopen("temp.in", "r");
	fout = fopen("temp.out", "w");
	
	int cases;
	fscanf(fin, "%d", &cases);
	REP(i, cases)
	{
		solve(i, fin, fout);
	}


	fclose(fin);
	fclose(fout);
	
	return 0;
}
