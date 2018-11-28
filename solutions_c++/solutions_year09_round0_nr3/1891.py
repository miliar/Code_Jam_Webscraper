#include <iostream>
#define MAX_SIZE 35
using namespace std;

int n, result, head, tail;
char str[MAX_SIZE], sample[] = "welcome to code jam";

struct node
{
	int nextSearch;
	int nextLetter;
} bfs[99999999];

int main()
{
 	freopen("C-small-attempt0.in", "r", stdin);
	freopen("Welcome come to Code Jam.out", "w", stdout);

	int i, j, l, s, len;

	cin >> n;
	getchar();
	for (i = 1; i <= n; ++i)
	{
		result = 0;
		
		gets(str);
		
		head = tail = 0;
		len =  strlen(str);
		for (j = 0; j < len; ++j)
		{
			if (str[j] == 'w')
			{
				bfs[tail].nextLetter = 1;
				bfs[tail++].nextSearch = j + 1;
			}
		}

		while (head != tail)
		{
			l = bfs[head].nextLetter;
			s = bfs[head++].nextSearch;

			if (sample[l] == '\0')
			{
				++result;
				continue;
			}

			for (j = s; j < len; ++j)
			{
				if (str[j] == sample[l])
				{
					bfs[tail].nextLetter = l + 1;
					bfs[tail++].nextSearch = j + 1;
				}
			}
		}
		
		printf("Case #%d: %04d\n", i, result);
	}
	return 0;
}