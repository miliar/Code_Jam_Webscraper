#include <stdio.h>

int abs(int x)
{
	if (x<0)
		return 0-x;
	return x;
}

int main()
{
	int t;
	int last[2], remainTime[2], totalT;
	scanf("%d", &t);
	for (int i = 0; i<t; i++)
	{
		for (int j = 0; j<2; j++)
		{
			last[j] = 1;
			remainTime[j] = 0;
		}
		totalT = 0;

		int p;
		scanf("%d", &p);
		for (int j = 0; j<p; j++){
			char c;
			int next;
			scanf(" %c", &c);
			scanf("%d", &next);
			int flag = (int) (c=='O');
			int len = abs(next-last[flag]);

			if ( len <= remainTime[flag]) {	// don't need to use more time
				totalT ++;
				remainTime[1-flag]++;

				remainTime[flag] = 0;
				last[flag] = next;
			}
			else {
				totalT += len - remainTime[flag] + 1;
				remainTime[1-flag] += len-remainTime[flag] + 1;

				remainTime[flag] = 0;
				last[flag] = next;
			}
		}
		printf("Case #%d: %d\n", i+1, totalT);
	}
	return 0;
}
