#include <stdio.h>
#include <map>

using namespace std;

const int MAX = 1048800;

map<int, int> cando[2][MAX + 1];

void addbetter(int now, int z, int one, int two)
{
	if (cando[now][z].find(one) == cando[now][z].end() || cando[now][z][one] < two)
	{
		cando[now][z][one] = two;
	}
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++)
	{		
		for (int z = 0; z <= MAX; z++)
		{
			cando[1][z].clear();
		}

		cando[1][0][0] = 0;
		int N;
		scanf("%d", &N);

		for (int j = 0; j < N; j++)
		{
			int c;

			scanf("%d", &c);

			int now = j % 2;
			for (int z = 0; z <= MAX; z++)
			{
				cando[now][z].clear();
			}

			for (int z = 0; z <= MAX; z++)
			{
				for (map<int, int>::iterator it = cando[!now][z].begin(); it != cando[!now][z].end(); it++)
				{
					addbetter(now, z ^ c, it->first, it->second);
					addbetter(now, z, it->first ^ c, it->second + c);
				}
			}
		}

		int bestval = 0;
		int now = (N - 1) % 2;

		for (int z = 1; z <= MAX; z++)
		{
			if (cando[now][z][z] > bestval) bestval = cando[now][z][z];
		}

		if (bestval)
			printf("Case #%d: %d\n", i + 1, bestval);
		else
			printf("Case #%d: NO\n", i + 1, bestval);
	}
}