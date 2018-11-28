#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
using namespace std;
int main()
{
	freopen("../../google.in", "r", stdin);
	freopen("../../google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int mod  =  10007;
		int w, h, r;
		cin >> w >> h >> r;
		vector<vector<int> > v(h);
		for(int i = 0; i < h; i++)
			v[i].resize(w, 0);
		v[0][0] = 1;
		int x, y;
		for(int i = 0; i < r; i++)
		{
			cin >> x >> y;
			v[y - 1][x - 1] = -1;
		}
		for(int i = 1; i < h; i++)
		{
			for(int j = 0; j < w; j++)
			{
				if(v[i][j] == -1)
					continue;
				else
				{
					if(i > 1 && j > 0 && v[i - 2][j - 1] != -1)
						v[i][j] = (v[i][j] + v[i - 2][j - 1]) % mod;
					if(i > 0 && j > 1 && v[i - 1][j - 2] != -1)
						v[i][j] = (v[i][j] + v[i - 1][j - 2]) % mod;
					/*if(i < h - 1 && j > 1 && v[i + 1][j - 2] != -1)
						v[i][j] = (v[i][j] + v[i + 1][j - 2]) % mod;
					if(i < h - 2 && j > 0 && v[i + 2][j - 1] != -1)
						v[i][j] = (v[i][j] + v[i + 2][j - 1]) % mod;
					if(i < h - 1 && j < w - 2 && v[i + 1][j + 2] != -1)
						v[i][j] = (v[i][j] + v[i + 1][j + 2]) % mod;
					if(i < h - 2 && j < w - 1 && v[i + 2][j + 1] != -1)
						v[i][j] = (v[i][j] + v[i + 2][j + 1]) % mod;
					if(i > 0 && j < w - 2 && v[i - 1][j + 2] != -1)
						v[i][j] = (v[i][j] + v[i - 1][j + 2]) % mod;
					if(i > 1 && j < w - 1 && v[i - 2][j + 1] != -1)
						v[i][j] = (v[i][j] + v[i - 2][j + 1]) % mod;*/
				}
			}
		}
		cout << v[h - 1][w - 1] << endl;

	}
	return 0;
}
