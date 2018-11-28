#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <cctype>
#include <set>
#include <iostream>
#include <sstream>
#include <ctime>
#include <numeric>

using namespace std;

char buf[100 + 1][100 + 1];
double wp[100 + 1][2];
double owp[100 + 1];
double ret[100 + 1];

int main()
{
	int T;
	scanf("%d", &T);
	for(int testc = 1; testc <= T; testc++)
	{
		int N;
		scanf("%d", &N);
		for(int i = 0; i < N; i++)
			scanf("%s", buf[i]);
		memset(wp, 0, sizeof(wp));
		memset(owp, 0, sizeof(owp));
		memset(ret, 0, sizeof(ret));
		for(int i = 0; i < N; i++)
		{
			int up = 0, down = 0;
			for(int j = 0; j < N; j++)
				if(buf[i][j] == '0')
					down++;
				else if(buf[i][j] == '1')
					up++, down++;
			wp[i][0] = up;
			wp[i][1] = down;
		}
		for(int i = 0; i < N; i++)
		{
			int cnt = 0;
			for(int j = 0; j < N; j++)
			{
				if(buf[i][j] != '.')
				{
					owp[i] += (double)(wp[j][0] - (buf[j][i] == '1')) / (wp[j][1] - 1);
					cnt++;
				}
			}
			owp[i] /= cnt;
		}
		for(int i = 0; i < N; i++)
		{
			int cnt = 0;
			for(int j = 0; j < N; j++)
				if(buf[i][j] != '.')
				{
					ret[i] += owp[j];
					cnt++;
				}
				ret[i] /= cnt;
				ret[i] *= 0.25;
				ret[i] += 0.5 * owp[i];
				ret[i] += 0.25 * double(wp[i][0]) / wp[i][1];
		}
		printf("Case #%d:\n", testc);
		for(int i = 0; i < N; i++)
			printf("%g\n", ret[i]);
	}
	return 0;
}