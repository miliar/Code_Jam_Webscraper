#include <iostream>
#include <string>

using namespace std;

void main()
{
	unsigned __int64 num;
	int N,a,b,c;
	int digits[128];
	string tmp;

	cin >> N;
	for (a = 1; a <= N; a++)
	{
		cin >> tmp;
		memset(digits, -1, sizeof(digits));
		c = 0;
		for (b = 0; b < tmp.size(); b++)
		{
			if (digits[tmp[b]] == -1)
			{
				if (c == 0)
				{
					digits[tmp[b]] = 1;
				}
				else if (c == 1)
				{
					digits[tmp[b]] = 0;
				}
				else
				{
					digits[tmp[b]] = c;
				}
				c++;
			}
		}
		if (c == 1)
		{
			c = 2;
		}
		num = 0;
		for (b = 0; b < tmp.size(); b++)
		{
			num *= c;
			num += digits[tmp[b]];
		}
		printf("Case #%d: %I64u\n", a, num);
	}
}
