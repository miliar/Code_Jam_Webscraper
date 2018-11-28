#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdio>

using namespace std;

long long T[500][500];

int main()
{
	int test_count, test;
	cin >> test_count;
	for (test=1;test<=test_count;test++)
	{
		int R, C, D;
		cin >> R >> C >> D;

		

		for (int i=0;i<R;i++)
			for (int j=0;j<C;j++)
			{
				char c;
				cin >> c;
				
				long long M = c-'0' + D;
				T[i][j] = M;
			}

		int res = 0;

		for (int k=3;k<=min(R, C);k++)
		{
			int x1, y1, x, y;
			for (y1=0;y1<=R-k;y1++)
				for (x1=0;x1<=C-k;x1++)
				{
					long long sumX = 0, sumY = 0, sumM = 0;
					int y2 = y1 + k - 1;
					int x2 = x1 + k - 1;
					int n = k*k - 4;
					for (y=y1;y<y1+k;y++)
						for (x=x1;x<x1+k;x++)
						{
							if ((x==x1 && y==y1) ||
								(x==x2 && y==y1) ||
								(x==x1 && y==y2) ||
								(x==x2 && y==y2) )
								continue;


							sumX+=(long long)((x-x1)*T[y][x]);
							sumY+=(long long)((y-y1)*T[y][x]);
							sumM+=T[y][x];
						}

					long long sumXdiv = sumX/sumM;
					long long sumYdiv = sumY/sumM;
					
					long long sumXmod = sumX%sumM;
					long long sumYmod = sumY%sumM;

					if (sumXmod==0 && sumYmod==0 && sumXdiv == k/2 && sumYdiv == k/2 && k%2 == 1)
					{
						res = k;
					}

					if (sumXmod==sumM/2 && sumYmod==sumM/2 && sumXdiv == k/2 - 1 && sumYdiv == k/2 - 1 && k%2 == 0)
					{
						res = k;
					}
				}
		}
		if (res>=3)
			printf("Case #%d: %d\n", test, res);
		else printf("Case #%d: IMPOSSIBLE\n", test);

	}

	return 0;
}