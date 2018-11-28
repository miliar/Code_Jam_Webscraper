#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <Map>
#include <hash_set>
#include <exception>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>

using namespace std;
using namespace stdext;

int T, H, W;

bool Solve(int* Map[], char* ans[], int H, int W, int h, int w, vector<pair<int,int>>& route, char nextChar)
{
	char c;
	vector<pair<int,int>>::iterator iter;
	if ((c = ans[h][w]) != 0)
	{
		for (iter = route.begin(); iter!= route.end(); iter++)
			ans[iter->first][iter->second] = c;
		return false;
	}

	int hh = h, ww = w, min = Map[h][w];

	//north
	if (h > 0 && Map[h-1][w] < min)
	{
		hh = h-1;
		ww = w;
		min = Map[hh][ww];
	}

	//west
	if (w > 0 && Map[h][w-1] < min)
	{
		hh = h;
		ww = w-1;
		min = Map[hh][ww];
	}

	//east
	if (w < W-1 && Map[h][w+1] < min)
	{
		hh = h;
		ww = w+1;
		min = Map[hh][ww];
	}

	//south
	if (h < H-1 && Map[h+1][w] < min)
	{
		hh = h+1;
		ww = w;
		min = Map[hh][ww];
	}

	//sink
	if (hh==h && ww==w)
	{
		ans[hh][ww] = nextChar;
		for (iter = route.begin(); iter!= route.end(); iter++)
			ans[iter->first][iter->second] = nextChar;
		return true;		
	} else
	{
		route.push_back(pair<int,int>(h,w));
		return Solve(Map, ans, H, W, hh, ww, route, nextChar);
	}
}
void CreateAns(int* Map[], char* ans[], int H, int W)
{
	for (int h=0; h<H; h++)
		for (int w=0; w<W; w++)
			ans[h][w] = 0;

	int hh, ww, min;
	vector<pair<int,int>> route;
	char nextChar = 'a';

	for (int h=0; h<H; h++)
		for (int w=0; w<W; w++)
		{
			route.clear();
			if (Solve((int**)Map, (char**)ans, H, W, h, w, route, nextChar))
				nextChar++;
		}
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int** Map = (int**) malloc(100*sizeof(int*));
	char** ans = (char**) malloc(100*sizeof(char*));
	for (int i=0; i<100; i++)
	{
		Map[i] = (int*) calloc(100, sizeof(int));
		ans[i] = (char*) calloc(100, sizeof(char));
	}

	cin >> T ;
	for (int i=0; i<T; i++)
	{
		cin >> H >> W;
		for (int h=0; h<H; h++)
			for (int w=0; w<W; w++)
				cin >> Map[h][w];

		CreateAns((int**)Map, (char**)ans, H, W);
			
		cout << "Case #" << i+1 << ":\n";
		for (int h=0; h<H; h++)
		{
			for (int w=0; w<W; w++)
				cout << ans[h][w] << ' ';

			cout << '\n';
		}
	}

	for (int i=0; i<100; i++)
	{
		free(Map[i]); 
		free(ans[i]);
	}
	free(Map);
	free(ans);

	return 0;
}