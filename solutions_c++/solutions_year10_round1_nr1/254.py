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
	inputstream = freopen("in.txt", "r", stdin);
	outputstream = freopen("output.txt", "w", stdout);
}
#endif

char data[100][100];
char line[100];

int main()
{
	init();
	int cases;
	scanf("%d", &cases);
	int N, K;
	for (int i = 1; i <= cases; ++i)
	{
		scanf("%d %d", &N, &K);
		gets(line);
		char c;
		for (int j = 0; j < N; ++j)
		{
			for (int k = 0; k < N; ++k)
			{
				scanf("%c", &c);
				data[k][N-1-j] = c;
			}
			gets(line);
		}
		
		for (int j = N - 2; j >= 0; --j)
		{
			for (int k = 0; k < N; ++k)
			{
				if (data[j][k] != '.')
				{
					int nowj = j;
					while(nowj + 1 < N && data[nowj][k] != '.' && data[nowj+1][k] == '.')
					{
						swap(data[nowj][k], data[nowj+1][k]);
						nowj++;
					}
				}
			}
		}
		/*
		for (int j = 0; j < N; ++j)
		{
			for (int k = 0; k < N; ++k)
			{
				printf("%c", data[j][k]);
			}
			printf("\n");
		}
		*/
		bool blue = false;
		bool red = false;
		for (int j = 0; j + K <= N; ++j)
		{
			for (int k = 0; k < N; ++k)
			{
				bool bo = true;
				for (int m = 0; m < K; ++m)
				{
					if (data[j+m][k] != 'B')
					{
						bo = false;
						break;
					}
				}
				if (bo)
				{
					blue = true;
				}
			}
		}
		for (int j = 0; j < N; ++j)
		{
			for (int k = 0; k + K <= N; ++k)
			{
				bool bo = true;
				for (int m = 0; m < K; ++m)
				{
					if (data[j][k+m] != 'B')
					{
						bo = false;
						break;
					}
				}
				if (bo)
				{
					blue = true;
				}
			}
		}
		for (int j = 0; j + K <= N; ++j)
		{
			for (int k = 0; k + K <= N; ++k)
			{
				bool bo = true;
				for (int m = 0; m < K; ++m)
				{
					if (data[j+m][k+m] != 'B')
					{
						bo = false;
						break;
					}
				}
				if (bo)
				{
					blue = true;
				}
			}
		}
		for (int j = 0; j + K <= N; ++j)
		{
			for (int k = 0; k < N; ++k)
			{
				bool bo = true;
				for (int m = 0; m < K; ++m)
				{
					if (data[j+m][k] != 'R')
					{
						bo = false;
						break;
					}
				}
				if (bo)
				{
					red = true;
				}
			}
		}
		for (int j = 0; j < N; ++j)
		{
			for (int k = 0; k + K <= N; ++k)
			{
				bool bo = true;
				for (int m = 0; m < K; ++m)
				{
					if (data[j][k+m] != 'R')
					{
						bo = false;
						break;
					}
				}
				if (bo)
				{
					red = true;
				}
			}
		}
		for (int j = 0; j + K <= N; ++j)
		{
			for (int k = 0; k + K <= N; ++k)
			{
				bool bo = true;
				for (int m = 0; m < K; ++m)
				{
					if (data[j+m][k+m] != 'R')
					{
						bo = false;
						break;
					}
				}
				if (bo)
				{
					red = true;
				}
			}
		}
		printf("Case #%d: ", i);
		if (!red && !blue) printf("Neither");
		if (red && !blue) printf("Red");
		if (!red && blue) printf("Blue");
		if (red && blue) printf("Both");
		printf("\n");
	}
	return 0;
}
