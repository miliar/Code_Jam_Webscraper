#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>
#include <queue>
#include <functional>
#include <sstream>
#include <complex>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <ctime>
#include <iomanip>
#include <time.h>
#include <string.h>

using namespace std;

#ifdef ONLINE_JUDGE
void init()
{
}
#else
FILE* inputstream;
FILE* outputstream;
void init()
{
	inputstream = freopen("B-large.in", "r", stdin);
	outputstream = freopen("B-large.out", "w", stdout);
}
#endif

int tonum_int(const string& str)
{
	int num;
	stringstream ss(str);
	ss>>num;
	return num;
}

int matrix[500][500];
pair<int, int> xdir[500][501];
pair<int, int> ydir[500][501];
int xdir2[500][501];
int ydir2[500][501];

int main()
{
	init();
	int T;
	cin >> T;
	for (int ii = 1; ii <= T; ++ii)
	{
		int R, C, D;
		cin >> R >> C >> D;
		ws(cin);
		for (int j = 0; j < R; ++j)
		{
			string str;
			getline(cin, str);
			for (int k = 0; k < C; ++k)
			{
				matrix[j][k] = str[k] - '0';
			}
		}
		for (int j = 0; j < R; ++j)
		{
			xdir[j][0] = make_pair(0, 0);
			xdir2[j][0] = 0;
			for (int k = 0; k < C; ++k)
			{
				xdir[j][k + 1] = xdir[j][k];
				xdir[j][k + 1].first += matrix[j][k] * k;
				xdir[j][k + 1].second += matrix[j][k] * j;
				xdir2[j][k+1] = xdir2[j][k] + matrix[j][k];
				//cout << xdir2[j][k+1] << " ";
			}
			//cout << endl;
		}
		for (int j = 0; j < C; ++j)
		{
			ydir[j][0] = make_pair(0, 0);
			ydir2[j][0] = 0;
			for (int k = 0; k < R; ++k)
			{
				ydir[j][k + 1] = ydir[j][k];
				ydir[j][k + 1].first += matrix[k][j] * j;
				ydir[j][k + 1].second += matrix[k][j] * k;
				ydir2[j][k+1] = ydir2[j][k] + matrix[k][j];
			}
		}
		int res = -1;
		for (int i = 1; i + 1 < R; ++i)
		{
			for (int j = 1; j + 1 < C; ++j)
			{
				int kmax = min(min(i, R - 1 - i), min(j, C - 1 - j));
				//cout << kmax << " ";
				//cout << kmax << " ";
				long long curx = 0;
				long long cury = 0;
				//int curbk = 0;
				long long kx = 0;
				for (int k = 1; k <= kmax; ++k)
				{
					curx += (xdir[i - k][j + k].first - xdir[i - k][j - k + 1].first);
					cury += (xdir[i - k][j + k].second - xdir[i - k][j - k + 1].second);
					curx += (xdir[i + k][j + k].first - xdir[i + k][j - k + 1].first);
					cury += (xdir[i + k][j + k].second - xdir[i + k][j - k + 1].second);
					
					curx += (ydir[j - k][i + k].first - ydir[j - k][i - k + 1].first);
					cury += (ydir[j - k][i + k].second - ydir[j - k][i - k + 1].second);
					curx += (ydir[j + k][i + k].first - ydir[j + k][i - k + 1].first);
					cury += (ydir[j + k][i + k].second - ydir[j + k][i - k + 1].second);
					
					kx += (xdir2[i - k][j + k] - xdir2[i - k][j - k + 1]);
					kx += (xdir2[i + k][j + k] - xdir2[i + k][j - k + 1]);
					kx += (ydir2[j - k][i + k] - ydir2[j - k][i - k + 1]);
					kx += (ydir2[j + k][i + k] - ydir2[j + k][i - k + 1]);
					
					//curbk += (k * 2 - 1) * 4;
					//cout << curbk << " ";
					
					if (kx * i == cury && kx * j == curx)
					{
						res = max(res, k * 2 + 1);
					}
					/*
					if (matrix[i][j] == 9)
					{
						cout << curx << " " << cury << " " << kx << " " << i << " " << j << endl;
					}
					*/
					//curbk += 4;
					curx += matrix[i - k][j - k] * (j - k);
					curx += matrix[i - k][j + k] * (j + k);
					curx += matrix[i + k][j - k] * (j - k);
					curx += matrix[i + k][j + k] * (j + k);
					
					cury += matrix[i - k][j - k] * (i - k);
					cury += matrix[i - k][j + k] * (i - k);
					cury += matrix[i + k][j - k] * (i + k);
					cury += matrix[i + k][j + k] * (i + k);
					
					kx += matrix[i - k][j - k];
					kx += matrix[i - k][j + k];
					kx += matrix[i + k][j - k];
					kx += matrix[i + k][j + k];
					
				}
			}
		}
		
		for (int i = 1; i + 2 < R; ++i)
		{
			for (int j = 1; j + 2 < C; ++j)
			{
				int kmax = min(min(i, R - 1 - i), min(j, C - 1 - j));
				//cout << kmax << " ";
				long long curx = matrix[i][j] * j + matrix[i+1][j] * j + matrix[i][j+1] * (j+1) + matrix[i+1][j+1] *(j+1);
				long long cury = matrix[i][j] * i + matrix[i+1][j] * (i+1) + matrix[i][j+1] * i + matrix[i+1][j+1] *(i+1);
				//int curbk = 0;
				long long kx = matrix[i][j] + matrix[i+1][j] + matrix[i][j+1] + matrix[i+1][j+1];
				//cout << curx << " " << cury << endl;
				for (int k = 1; k <= kmax; ++k)
				{
					curx += (xdir[i - k][j + k + 1].first - xdir[i - k][j - k + 1].first);
					cury += (xdir[i - k][j + k + 1].second - xdir[i - k][j - k + 1].second);
					curx += (xdir[i + k + 1][j + k + 1].first - xdir[i + k + 1][j - k + 1].first);
					cury += (xdir[i + k + 1][j + k + 1].second - xdir[i + k + 1][j - k + 1].second);
					
					curx += (ydir[j - k][i + k + 1].first - ydir[j - k][i - k + 1].first);
					cury += (ydir[j - k][i + k + 1].second - ydir[j - k][i - k + 1].second);
					curx += (ydir[j + k + 1][i + k + 1].first - ydir[j + k + 1][i - k + 1].first);
					cury += (ydir[j + k + 1][i + k + 1].second - ydir[j + k + 1][i - k + 1].second);
					
					kx += (xdir2[i - k][j + k + 1] - xdir2[i - k][j - k + 1]);
					kx += (xdir2[i + k + 1][j + k + 1] - xdir2[i + k + 1][j - k + 1]);
					kx += (ydir2[j - k][i + k + 1] - ydir2[j - k][i - k + 1]);
					kx += (ydir2[j + k + 1][i + k + 1] - ydir2[j + k + 1][i - k + 1]);
					
					//curbk += (k * 2 - 1) * 4;
					//cout << curbk << " ";
					
					if (kx * (2 * i + 1) == 2 * cury && kx * (2 * j + 1)== 2 * curx)
					{
						res = max(res, k * 2 + 2);
					}
					/*
					if (matrix[i][j] == 9)
					{
						cout << curx << " " << cury << " " << kx << " " << i << " " << j << endl;
					}
					*/
					//curbk += 4;
					curx += matrix[i - k][j - k] * (j - k);
					curx += matrix[i - k][j + k + 1] * (j + k + 1);
					curx += matrix[i + k + 1][j - k] * (j - k);
					curx += matrix[i + k + 1][j + k + 1] * (j + k + 1);
					
					cury += matrix[i - k][j - k] * (i - k);
					cury += matrix[i - k][j + k + 1] * (i - k);
					cury += matrix[i + k + 1][j - k] * (i + k + 1);
					cury += matrix[i + k + 1][j + k + 1] * (i + k + 1);
					
					kx += matrix[i - k][j - k];
					kx += matrix[i - k][j + k + 1];
					kx += matrix[i + k + 1][j - k];
					kx += matrix[i + k + 1][j + k + 1];
					
				}
			}
		}
		
		if (res == -1)
		{
			printf("Case #%d: IMPOSSIBLE\n", ii);
		}
		else
		{
			printf("Case #%d: %d\n", ii, res);
		}
	}
	return 0;
}
