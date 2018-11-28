#include <cstdio>
#include <cstring>

const int LMAX = 1000, NMAX = 200, INF = 2000000000;

char word[2 * NMAX][LMAX], buff[5], path[LMAX];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int test = 0; test < t; ++test)
	{
		int n, m, res = 0;
		scanf("%d%d", &n, &m);
		gets(buff);

		for (int i = 0; i < n; ++i)
			gets(word[i]);
		for (int i = 0; i < m; ++i)
		{
			gets(path);
			int min = 0;
			for (int j = 0; path[j]; ++j)
				if (path[j] == '/')
					++min;

			for (int j = 0; j < n; ++j)
			{
				int index = 0, lenPath = strlen(path), lenWord = strlen(word[j]);
				while (index < lenPath && index < lenWord && path[index] == word[j][index])
					++index;

				if (!path[index] && (!word[j][index] || word[j][index] == '/'))
				{
					min = 0;
					break;
				}

				int curr = 1;
				if (path[index] == '/' && word[j][index])
					++curr;
				for (int k = index + 1; path[k]; ++k)
					if (path[k] == '/')
						++curr;

				if (curr < min)
					min = curr;
			}

			strcpy(word[n++], path);
			res += min;
		}

		printf("Case #%d: %d\n", test + 1, res);
	}

	return 0;
}