#include <stdio.h>
#include <math.h>
#include <memory.h>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <queue>

using namespace std;

int dir[4][2] = {{-1, 0},{0, 1},{1, 0},{0, -1}};
int ZERO = 3500;

#define MAX 7000

int V[MAX][2];
int H[MAX][2];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);

	int L;
	char s[50];
	for (int t = 0; t < T; t++)
	{
		for (int i = 0; i < MAX; i++)
		{
			V[i][0] = 1000000000;
			V[i][1] = -1000000000;
			H[i][0] = 1000000000;
			H[i][1] = -1000000000;
		}
		scanf("%d", &L);
		int d = 0;
		int x = 0, y = 0;		
		long long S = 0;
		for (int l = 0; l < L; l++)
		{
			int count;
			scanf("%s%d", s, &count);
			for (int i = 0; i < count; i++)
			{
				for (int j = 0; s[j] != 0; j++)
				{
					if (s[j] == 'R')
					{
						d = (d + 1) % 4;
					}
					if (s[j] == 'L')
					{
						d = (d - 1 + 4) % 4;
					}
					if (s[j] == 'F')
					{
						int x1 = x + dir[d][0];
						int y1 = y + dir[d][1];
						if (d == 0)
						{
							V[x1+ZERO][0] = min(y, V[x1+ZERO][0]);
							V[x1+ZERO][1] = max(y, V[x1+ZERO][1]);
						}
						if (d == 2)
						{
							V[x+ZERO][0] = min(y, V[x+ZERO][0]);
							V[x+ZERO][1] = max(y, V[x+ZERO][1]);
						}
						if (d == 1)
						{
							H[y+ZERO][0] = min(x, H[y+ZERO][0]);
							H[y+ZERO][1] = max(x, H[y+ZERO][1]);
						}
						if (d == 3)
						{
							H[y1+ZERO][0] = min(x, H[y1+ZERO][0]);
							H[y1+ZERO][1] = max(x, H[y1+ZERO][1]);
						}
						long long dx = x1 - x;
						long long dy = (y + y1);
						S += dx*dy;
						x = x1;
						y = y1;
					}
				}
			}			
		}
		if (S < 0)
			S = -S;
		S /= 2;
		long long S2 = 0;
		for (int a = -3100; a <= 3100; a++)
			for (int b = -3100; b <= 3100; b++)
			{
				if (
					(V[a+ZERO][0] <= b && V[a+ZERO][1] > b) ||
					(H[b+ZERO][0] <= a && H[b+ZERO][1] > a) )
					S2++;
			}
		printf("Case #%d: %lld\n", t+1, S2-S);
	}


	fclose(stdin);
	fclose(stdout);
	return 0;
}