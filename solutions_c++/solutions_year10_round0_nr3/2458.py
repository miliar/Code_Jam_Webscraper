// Jam2010_1_2.cpp : Defines the entry point for the console application.
//
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef signed int int32;
typedef unsigned int uint32;
typedef signed __int64 int64;
typedef unsigned __int64 uint64;

uint64 g[2000];
uint64 resultSet[2000];
uint64 nextIndex[2000];

int main()
{
	freopen("../C-large.in","r",stdin);
	freopen("../C-large.out","w",stdout);

	int ch = 0;

	int testCase = 0;
	scanf("%d",&testCase);
	for (int testId=1; testId <= testCase; ++testId)
	{
		uint64 result = 0;

		memset(g, 0, sizeof(g));
		memset(resultSet, 0, sizeof(resultSet));
		memset(nextIndex, 0, sizeof(nextIndex));

		uint32 R = 0;
		uint32 k = 0;
		uint32 N = 0;
		scanf("%d %d %d",&R, &k, &N);
		//printf("%d %d %d\n",R, k, N);

		getchar();
		for(int i=0; i<N; ++i)
		{
			uint32 gi = 0;
			for (int j = 0; j < 20 && 
				((ch = getchar()) != EOF) && (ch != ' ') && (ch != '\n') && (ch != '\r'); ++j)
			{
				gi *= 10;
				gi += ch - '0';
			}
			g[i] = gi;
		}

		int index = 0;
		for(int i=0; i<R; ++i)
		{
			uint64 oneround = 0;
			int startindex = index;

			if (0 == resultSet[startindex])
			{
				while(true)
				{
					if(oneround + g[index] > k)
					{
						break;
					}
					oneround += g[index];

					++index;
					if(index == N)
						index = 0;
					if(startindex == index)
						break;
				}
				resultSet[startindex] = oneround;
				nextIndex[startindex] = index;
				//printf("%d ", startindex);
			}
			else
			{
				oneround = resultSet[startindex];
				index = nextIndex[startindex];
			}

			result += oneround;
		}
		printf("Case #%d: %I64u\n", testId, result);
	}

	return 0;
}

