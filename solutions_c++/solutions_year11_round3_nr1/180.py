#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <bitset>
#include <string.h>
using namespace std;

int R, C;
vector<string> tiles;

void readCase()
{
	scanf("%d %d\n", &R, &C);
	tiles.clear();
	for(int i = 0; i < R; i++) 
	{
		char buf[200];
		gets(buf);
		tiles.push_back(buf);
	}
}

void solve()
{
	bool possible = true;
	for(int x = 0; x < C - 1; x++)
		for(int y = 0; y < R - 1; y++)
		{
			if(tiles[y][x] == '#' && tiles[y+1][x] == '#' && tiles[y][x+1] == '#' && tiles[y+1][x+1] == '#')
			{
				tiles[y][x] = '/';
				tiles[y+1][x] = '\\';
				tiles[y][x+1] = '\\';
				tiles[y+1][x+1] = '/';
			}
		}
	
	for(int x = 0; x < C; x++)
		for(int y = 0; y < R; y++)
		{
			if(tiles[y][x] == '#') possible = false;
		}

	if(!possible)
	{
		printf("\nImpossible");
		return;
	}

	for(int i = 0; i < R; i++) 
	{
		printf( "\n%s", tiles[i].c_str() );
	}
}

int main()
{
	//string fname = "./test/A-example.in";
	//string fname = "./test/A-small-attempt0.in";
	string fname = "./test/A-large.in";
	
	freopen(fname.c_str(),"r",stdin);freopen((fname+".out").c_str(),"w",stdout);

	int analizeCase = -1;
	
	int T;
	scanf("%d", &T);
	for(int tCase = 1; tCase <= T; tCase++) {
		printf("Case #%d: ", tCase);
		readCase();
		if(analizeCase < 0 || analizeCase == tCase) solve();
		printf("\n");
		fflush(stdout);
		fprintf(stderr, "Done %d %%     \r", 100 * tCase / T );
	}
	return 0;
}

