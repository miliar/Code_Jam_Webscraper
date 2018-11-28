#include <iostream>

using namespace std;

int db[256];
int base;

int c2i[256];

char line[1024], *ptr;

int main()
{
	int caseNo, I = 1;

	scanf("%d", &caseNo);

	while (caseNo--)
	{
		base = 2;
		memset(db, 0, sizeof(db));
		scanf("%s", line);
		ptr = line;
		
		db[(int)*ptr] = 1;
		c2i[(int)*ptr] = 1;
		
		ptr++;

		while (*ptr && *ptr == *line)
		{
			ptr++;
		}

		if (*ptr)
		{
			//cout << *ptr << endl;
			db[(int)*ptr] = 1;
			c2i[(int)*ptr] = 0;

			ptr++;
		}
		
		while (*ptr)
		{
			int b = *ptr;
			if (db[b] == 0)
			{
				c2i[b] = base;
				base++;
				db[b] = 1;
			}
			ptr++;
		}

		__int64 res = 0;
		int len = strlen(line);
		if (len == 1)
		{
			res = 1;
		}
		else
		{
			__int64 base2 = 1;
			for (int i = len - 1; i >= 0; i--)
			{
				res += c2i[(int)(line[i])] * base2;
				base2 *= base;
			}
		}

		printf("Case #%d: %I64d\n", I++, res);
	}


	return 0;
}