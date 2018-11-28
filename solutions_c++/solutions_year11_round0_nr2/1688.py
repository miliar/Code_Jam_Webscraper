#include<stdio.h>

bool oppose[26][26];
int combine[26][26];

int sequence[200], ret[200], len;

void get_ans(int N)
{
	len = 0;
	bool clear;
	int i, j, tmp;
	for(i = 0; i < N; i ++)
	{
		clear = false;
		tmp = sequence[i];
		if(len > 0 && combine[ret[len - 1]][tmp] >= 0)
			ret[len - 1] = combine[ret[len - 1]][tmp];
		else
		{
			for(j = 0; j < len; j ++)
				if(oppose[ret[j]][tmp] == true)
				{
					clear = true;
					break;
				}
			if(clear)
				len = 0;
			else
				ret[len ++] = tmp;
		}
	}
}

void print()
{
	putchar('[');
	int i;
	for(i = 0; i < len - 1; i ++)
	{
		putchar('A' + ret[i]);
		putchar(',');
		putchar(' ');
	}
	if(len > 0)
		putchar('A' + ret[i]);
	putchar(']');
	printf("\n");
}
int main()
{
	int test, T, i, j;
	int C, O, N;
	char ts[200];
	scanf("%d", &T);
	for(test = 1; test <= T; test ++)
	{
		for(i = 0; i < 26; i ++)
			for(j = 0; j < 26; j ++)
			{
				oppose[i][j] = false;
				combine[i][j] = -1;
			}
		scanf("%d", &C);
		while(C --)
		{
			scanf("%s", ts);
			combine[ts[0] - 'A'][ts[1] - 'A'] = ts[2] - 'A';
			combine[ts[1] - 'A'][ts[0] - 'A'] = ts[2] - 'A';		
		}
		scanf("%d", &O);
		while(O --)
		{
			scanf("%s", ts);
			oppose[ts[0] - 'A'][ts[1] - 'A'] = true;
			oppose[ts[1] - 'A'][ts[0] - 'A'] = true;
		}
		scanf("%d", &N);
		scanf("%s", ts);
		for(i = 0; i < N; i ++)
			sequence[i] = ts[i] - 'A';
		get_ans(N);
		printf("Case #%d: ", test);
		print();
		
	}
	
	return 0;
}
