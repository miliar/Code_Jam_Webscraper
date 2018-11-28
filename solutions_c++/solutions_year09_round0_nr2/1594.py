#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int H,W;
pair<int,int> memo[102][102];
int m[102][102];
int dy[] = { 0, -1, 1, 0 };
int dx[] = { -1, 0, 0, 1 };
map<pair<int,int>, char> ch;

pair<int,int> dp(int x, int y)
{
	//cout << x << " " << y << " " << m[x][y] << endl;
	if (memo[x][y].first != -1 && memo[x][y].second != -1)
		return memo[x][y];
	int lx,ly;
	int min = 20000;
	for (int i = 0; i < 4; ++i)
	{
		int x1 = x + dx[i];
		int y1 = y + dy[i];
		if (x1 < 0 || y1 < 0 || x1 >= H || y1 >= W)
			continue;
		if (m[x1][y1] >= m[x][y])
			continue;
		if (m[x1][y1] < min)
		{
			min = m[x1][y1];
			lx = x1;
			ly = y1;
		}
	}
	if (min == 20000)	
		return memo[x][y] = make_pair(x,y);
	
	return memo[x][y] = dp(lx,ly);
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		cin >> H >> W;
		
		for (int j = 0; j < H; ++j)
			for (int k = 0; k < W; ++k)
				cin >> m[j][k];	
	
		for (int j = 0; j < H; ++j)
			for (int k = 0; k < W; ++k)
				memo[j][k] = make_pair(-1,-1);
		
		for (int j = 0; j < H; ++j)
			for (int k = 0; k < W; ++k)
				dp(j,k);
			
		ch.clear();
		int count = 0;
		cout << "Case #" << (i+1) << ":" << endl;
		for (int j = 0; j < H; ++j)
		{
			for (int k = 0; k < W; ++k)
			{
				if (ch.count(memo[j][k]) == 0)
					ch[memo[j][k]] = (char) ('a' + count++);
				
				cout << ch[memo[j][k]];
				if (k < W-1)
					cout << " ";
			}
			cout << endl;
		}
	}
	return 0;
}
