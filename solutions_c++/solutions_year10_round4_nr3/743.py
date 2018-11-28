#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MAX = 505;

int mm[MAX][MAX];
int pp[MAX][MAX];

int num()
{
	int res = 0;
	for(int i = 0; i < MAX; i++)
		for(int j = 0; j < MAX; j++)
			if(mm[i][j])  res++;
	return res;
}

int go()
{
	int res = 0;
	while(num())
	{
		res++;
		memset(pp, 0, sizeof(pp));
		for(int i = 0; i < MAX; i++)  for(int j = 0; j < MAX; j++)
		{
			if(i > 0 && mm[i - 1][j] && j > 0 && mm[i][j - 1])  pp[i][j] = 1;
			//if(j > 0 && mm[i][j - 1])  pp[i][j] = 1;
			if(mm[i][j])
			{
				if(j > 0 && mm[i][j - 1])  pp[i][j] = 1;
				if(i > 0 && mm[i - 1][j])  pp[i][j] = 1;
			}
		}
		
		for(int i = 0; i < MAX; i++)
		{
			for(int j = 0; j < MAX; j++)
			{
				mm[i][j] = pp[i][j];
				//printf("%d", mm[i][j]);
			}
			//printf("\n");
		}
	//	printf("\n");
		

	}
	return res;
}

int main()
{
	freopen("d:\\C-small-attempt0.in", "r", stdin);
	freopen("d:\\C-small-attempt0.out", "w", stdout);

	int T, c = 0;
	scanf("%d", &T);
	while(T--)
	{
		int R;
		memset(mm, 0, sizeof(mm));
		scanf("%d", &R);
		while(R--)
		{
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for(int i = x1; i <= x2; i++)  for(int j = y1; j <= y2; j++)
				mm[i][j] = 1;
		}
		printf("Case #%d: %d\n", ++c, go());
	}
}