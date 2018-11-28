#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

int n;
char which[100];
int where[100];

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
	{
		scanf("%d", &n);
		for(int j = 0; j < n; j++)
			scanf(" %c %d", &which[j], &where[j]);

		int o = 1, b = 1;
		int t = 0;
		char turn = 'O';
		int k = 0;

		for(int j = 0; j < n; j++)
		{
			if(which[j] == 'O')
			{
				int diff = abs(where[j] - o);
				o = where[j];
				if(turn == 'B')
				{
					diff -= k;
					diff = max(0, diff);
					turn = 'O';
					k = 0;
				}
				t += diff + 1;
				k += diff + 1;
			}
			else
			{
				int diff = abs(where[j] - b);
				b = where[j];
				if(turn == 'O')
				{
					diff -= k;
					diff = max(0, diff);
					turn = 'B';
					k = 0;
				}
				t += diff + 1;
				k += diff + 1;
			}
		}
		printf("Case #%d: %d\n", i,t);
	}
	return 0;
}
