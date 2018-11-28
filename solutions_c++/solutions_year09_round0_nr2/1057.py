//
//  untitled
//
//  Created by  on 2009-09-03.
//  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
//

#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <list>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector <int> VI;
typedef vector <double> VD;
typedef vector <vector<int> > VVI;
typedef pair <int,int> PII;
typedef pair <int,PII> PIII;
typedef vector <LL> VL;
typedef vector <string> VS;

int curr_letter = 'a';

VVI memo;
VVI ret;

int dx[] = {0,-1,1,0};
int dy[] = {-1,0,0,1};
int w,h;

int go(int x, int y) 
{
	int min = 1000000000;
	int bestx, besty;
	if (ret[y][x] != -1) return ret[y][x];
	for(int i = 0; i < 4; ++i)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx < 0 || nx >= w || ny < 0 || ny >= h) continue;
		if (memo[ny][nx] < min) {
			min = memo[ny][nx];
			bestx = nx;
			besty = ny;
		}
	}
	if (min < memo[y][x]) {
		int c = go(bestx,besty);
		ret[y][x] = c;
		return c;
	}
	ret[y][x] = curr_letter;
	curr_letter++;
	return ret[y][x];
}

int main()
{
	int t;
	cin >> t;
	for(int tt = 0; tt < t; ++tt)
	{
		cin >> h >> w;
		memo = VVI(h,VI(w));
		ret = VVI(h,VI(w,-1));
		for(int i = 0; i < h; ++i)
		{
			for(int j = 0; j < w; ++j)
			{
				cin >> memo[i][j];
			}
		}
		curr_letter = 'a';
		for(int i = 0; i < h; ++i)
		{
			for(int j = 0; j < w; ++j)
			{
				if (ret[i][j] == -1) {
					go(j,i);
				}
			}
		}
		
		printf("Case #%d:\n", tt+1);
		for(int i = 0; i < h; ++i)
		{
			for(int j = 0; j < w; ++j)
			{
				cout << (j == 0 ? "" : " ");
				cout << (char)ret[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}