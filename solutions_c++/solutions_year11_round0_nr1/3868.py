#include<stdio.h>
int main()
{
	int T, cases = 1;
	scanf("%d",&T);
	while(T--)
	{
		int N;
		scanf("%d",&N);
		int posO = 1, posB = 1, timeO = 0, timeB = 0;
		for(int i  = 0; i < N; i++)
		{
			char s[1];
			int p;
			scanf("%s%d", s, &p);
			if(s[0] == 'O')
			{
				int diff = p - posO;
				if(diff < 0) diff = -diff;
				timeO += (diff + 1);
				if(timeO <= timeB) timeO = timeB + 1;
				posO = p;
			}
			if(s[0] == 'B')
			{
				int diff = p - posB;
				if(diff < 0) diff = -diff;
				timeB += (diff + 1);
				if(timeB <= timeO) timeB = timeO + 1;
				posB = p;
			}
		}
		printf("Case #%d: %d\n", cases++,  timeB > timeO ? timeB : timeO);
	}
	return 0;
}
