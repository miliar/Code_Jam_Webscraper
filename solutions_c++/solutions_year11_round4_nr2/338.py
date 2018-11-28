#include <assert.h> 
#include <ctype.h> 
#include <float.h> 
#include <math.h> 
#include <stdio.h> 
#include <string> 
#include <stdlib.h> 
#include <time.h> 
#include <algorithm> 
#include <numeric> 
#include <functional> 
#include <utility> 
#include <vector> 
#include <list> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <sstream> 
#include <iostream> 
#include <memory.h>

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;

char s[1000];
int w[503][503];

double sx[503][503];
double sy[503][503];
double sd[503][503];

double sumX(int left, int right, int top, int bottom)
{
	return sx[bottom][right] - sx[bottom][left] - sx[top][right] + sx[top][left];
}

double sumY(int left, int right, int top, int bottom)
{
	return sy[bottom][right] - sy[bottom][left] - sy[top][right] + sy[top][left];
}
double sumD(int left, int right, int top, int bottom)
{
	return sd[bottom][right] - sd[bottom][left] - sd[top][right] + sd[top][left];
}


int main(int argc, char* argv[])
{
#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
#endif
	int T;
	scanf("%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{		
		int R, C, D;
		cin >>R >> C >> D;

		for( int i = 0; i < R; i++)
		{
			scanf("%s", s);
			for (int j = 0; j < C; j++)
			{
				w[i][j] = D + s[j] - '0';
			}
		}

		memset(sx,0, sizeof(sx));
		memset(sy,0, sizeof(sy));
		memset(sd,0, sizeof(sd));

		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				sx[i + 1][j + 1] = sx[i + 1][j] + sx[i][j + 1] - sx[i][j] + w[i][j] * j;
				sy[i + 1][j + 1] = sy[i + 1][j] + sy[i][j + 1] - sy[i][j] + w[i][j] * i;
				sd[i + 1][j + 1] = sd[i + 1][j] + sd[i][j + 1] - sd[i][j] + w[i][j] ;
			}

		}

		int bestSize = -1;

		for (int k = min(R, C); k >= 3; k--)
		{
			for (int top = 0; top < R; top++)
			{
				for (int left = 0; left < C; left++)
				{
					if (top + k > R || left + k > C)
						break;					

					double xCenter2 = 0;
					double sd = sumD(left, left + k, top, top + k);;

					xCenter2 += sumX(left, left + k, top, top + k);
					xCenter2 += 0.5 * sd;
					xCenter2 -= left * sd;
					xCenter2 -= k / 2.0 * sd;
					
					xCenter2 -= (left + 0.5 - (left + k /2.0)) * w[top][left];
					xCenter2 -= (left + k - 1 + 0.5 - (left + k /2.0)) * w[top][left + k - 1];
					xCenter2 -= (left + 0.5 - (left + k /2.0)) * w[top + k - 1][left];
					xCenter2 -= (left + k - 1 + 0.5 - (left + k /2.0)) * w[top+ k - 1][left + k - 1];

					double yCenter2 = 0;

					yCenter2 += sumY(left, left + k, top, top + k);
					yCenter2 += 0.5 * sd;
					yCenter2 -= top * sd;
					yCenter2 -= k / 2.0 * sd;

					yCenter2 -= (top + 0.5 - (top + k /2.0)) * w[top][left];
					yCenter2 -= (top + 0.5 - (top + k /2.0)) * w[top][left + k - 1];
					yCenter2 -= (top + k - 1 + 0.5 - (top + k /2.0)) * w[top + k - 1][left];
					yCenter2 -= (top + k - 1 + 0.5 - (top + k /2.0)) * w[top+ k - 1][left + k - 1];

					if (fabs(xCenter2) < 1e-6 && fabs(yCenter2) < 1e-6)
					{
						bestSize = k;
						goto printIt;

					}
				}
			}
		}
printIt:

		printf("Case #%d: ", nTest);
		if (bestSize == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", bestSize);
		fflush(stdout);
	} 


	return 0;
}

 
