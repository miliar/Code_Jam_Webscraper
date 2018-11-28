#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

int last = 1;
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

int wave(vector<vector<int> >& altitudes, vector<vector<int> >& result, int x, int y) 
{
	int nx,ny;
	int minx = x, miny = y;
	for (int i = 0; i < 4; ++i) {
		nx = x + dx[i];
		ny = y + dy[i];
		if (nx >= 0 && nx < result.size() && ny >= 0 && ny < result[0].size() && altitudes[nx][ny] < altitudes[minx][miny]) {
			minx = nx;
			miny = ny;
		}
	}

	if (minx == x && miny == y)
		return result[x][y] = last++;
	else if (result[minx][miny])
		return result[x][y] = result[minx][miny];
	else
		return result[x][y] = wave(altitudes, result, minx, miny);
}

int main()
{
	ifstream cin("B-large.in");
	ofstream cout("file.out");
	
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		int H,W;
		last = 1;
		cin >> H >> W;
		vector <vector <int> > altitudes(H, vector <int> (W));
		vector <vector <int> > result(H, vector <int> (W));
		for (int j = 0; j < H; ++j)
			for (int k = 0; k < W; ++k)
				cin >> altitudes[j][k];
		
		for (int j = 0; j < H; ++j)
			for (int k = 0; k < W; ++k) {
				if (!result[j][k]) {
					result[j][k] = wave(altitudes, result, j, k);
				}
			}

		cout << "Case #" << i + 1 << ":" << endl;
		for (int j = 0; j < H; ++j) {
			for (int k = 0; k < W; ++k) {
				cout << char('a' + result[j][k] - 1) << ' ';
			}
			cout << endl;
		}
	}

	return 0;
}
