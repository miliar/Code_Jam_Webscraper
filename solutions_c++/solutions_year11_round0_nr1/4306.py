#include <stdio.h>

int T;
int N;

int main()
{
	int idx, i;
	int max, o, b, opos, bpos;
	char s[8];
	int pos;
	int tmp;
	scanf("%d", &T);
	for(idx = 0; idx < T; idx++)
	{
		max = o = b = 0;
		opos = bpos = 1;
		scanf("%d", &N);
		for(i = 0; i < N; i++)
		{
			scanf("%s", s);
			scanf("%d", &pos);
			if(s[0] == 'O')
			{
				tmp = pos - opos;
				opos = pos;
				o += (tmp > 0 ? tmp : -tmp);
				if(o > max)	max = o;
				else o = max;
				max++;
				o++;
			}
			else if(s[0] == 'B')
			{
				tmp = pos - bpos;
				bpos = pos;
				b += (tmp > 0 ? tmp : -tmp);
				if(b > max) max = b;
				else b = max;
				max++;
				b++;
			}
		}
		printf("Case #%d: %d\n", idx + 1, max);
	}

	return 0;
}