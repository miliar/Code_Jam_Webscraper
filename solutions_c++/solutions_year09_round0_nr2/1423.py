#include <iostream>
#include <cstring>
#include <vector>
#define MAX_H 101
#define MAX_W 101
#define MAX_ALT 10000
using namespace std;

int altitudes[MAX_H][MAX_W];

void drains(pair<int, int> actual, pair<int, int> &cell, int h, int w)
{
	int lowestAlt = MAX_ALT, actualH = actual.first, actualW = actual.second, actualAlt = altitudes[actualH][actualW];
	cell = actual;
	
	if(actualH > 1 && altitudes[actualH - 1][actualW] < actualAlt && altitudes[actualH - 1][actualW] < lowestAlt)
	{
		lowestAlt = altitudes[actualH - 1][actualW];
		cell = make_pair(actualH - 1, actualW);
	}
	if(actualW > 1 && altitudes[actualH][actualW - 1] < actualAlt && altitudes[actualH][actualW - 1] < lowestAlt)
	{
		lowestAlt = altitudes[actualH][actualW - 1];
		cell = make_pair(actualH, actualW - 1);
	}
	if(actualW < w && altitudes[actualH][actualW + 1] < actualAlt && altitudes[actualH][actualW + 1] < lowestAlt)
	{
		lowestAlt = altitudes[actualH][actualW + 1];
		cell = make_pair(actualH, actualW + 1);
	}
	if(actualH < h && altitudes[actualH + 1][actualW] < actualAlt && altitudes[actualH + 1][actualW] < lowestAlt)
	{
		lowestAlt = altitudes[actualH + 1][actualW];
		cell = make_pair(actualH + 1, actualW);
	}
}	

int main(void)
{
	int T, H, W;
	
	cin >> T;
	for(int numCase = 1; numCase <= T; numCase++)
	{
		pair<int, int> drainings[MAX_H][MAX_W];
		char labeled[MAX_H][MAX_W];
		
		for(int i = 0; i < MAX_H; i++)
			for(int j = 0; j < MAX_W; j++) altitudes[i][j] = MAX_ALT;
		
		cin >> H >> W;
		for(int i = 1; i <= H; i++)
			for(int j = 1; j <= W; j++)
			{
				cin >> altitudes[i][j];
				labeled[i][j] = 0;
			}
			
		for(int i = 1; i <= H; i++)
			for(int j = 1; j <= W; j++)
				drains(make_pair(i, j), drainings[i][j], H, W);
		
		char nextLabel = 'a';
		vector<pair<int, int> > sameBasin;
		
		for(int i = 1; i <= H; i++)
			for(int j = 1; j <= W; j++)
			{
				if(labeled[i][j]) continue;
				
				sameBasin.push_back(make_pair(i, j));
				while(!sameBasin.empty())
				{
					pair<int, int> actual = sameBasin.back();
					sameBasin.pop_back();
					labeled[actual.first][actual.second] = nextLabel;
					
					pair<int, int> next = drainings[actual.first][actual.second];
					if(!labeled[next.first][next.second]) sameBasin.push_back(next);
					
					pair<int, int> north = make_pair(actual.first, actual.second - 1);
					if(!labeled[north.first][north.second] && drainings[north.first][north.second] == actual) sameBasin.push_back(north);
					
					pair<int, int> west = make_pair(actual.first - 1, actual.second);
					if(!labeled[west.first][west.second] && drainings[west.first][west.second] == actual) sameBasin.push_back(west);
					
					pair<int, int> east = make_pair(actual.first + 1, actual.second);
					if(!labeled[east.first][east.second] && drainings[east.first][east.second] == actual) sameBasin.push_back(east);
					
					pair<int, int> south = make_pair(actual.first, actual.second + 1);
					if(!labeled[south.first][south.second] && drainings[south.first][south.second] == actual) sameBasin.push_back(south);
				}
				
				nextLabel++;
			}
			
		cout << "Case #" << numCase << ":" << endl;
			
		for(int i = 1; i <= H; i++)
		{
			for(int j = 1; j <= W; j++) cout << labeled[i][j] << " ";
			cout << endl;
		}
	}
}
