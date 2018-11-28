#include<cstdio>
#include<algorithm>

using namespace std;

int readCol()
{
	int c;
	do
		c = getchar();
	while (c != 'O' && c != 'B');
	return c != 'O';
}
int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		int N;
		scanf("%d", &N);
		int pos[2] = {1, 1};
		int tim[2] = {0, 0};
		int res = 0;
		for (int i = 0; i < N; i++)
		{
			int col = readCol();
			int p;
			scanf("%d", &p);
			int dt = abs(pos[col] - p);
			res = tim[col] = max(tim[col] + dt + 1, tim[!col] + 1);
			pos[col] = p;
		}
		printf("Case #%d: %d\n", t, res);
	}
	
	return 0;
}
