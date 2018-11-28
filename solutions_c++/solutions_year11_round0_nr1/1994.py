#include <stdio.h>
#include <string.h>
#include <math.h>

struct S
{
	char color;
	int number;
}seq[100];

int t, n;
int Play();

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <=t; ++i)
	{
		scanf("%d", &n);
		memset(seq, 0, sizeof (seq));
		for (int j = 0; j < n; ++j)
			scanf(" %c %d", &seq[j].color, &seq[j].number);
		printf("Case #%d: %d\n", i, Play());
	}
	return 0;
}

int Play()
{
	int time = 0, ora_tim = 0, blu_tim = 0;
	int ora_num = 1, blu_num = 1;
	for (int i = 0; i < n; ++i)
	{
		int temp_time;
		if (seq[i].color == 'O')
		{
			temp_time = abs (seq[i].number - ora_num);
			if (temp_time <= blu_tim )
				temp_time = 1;
			else
				temp_time = temp_time - blu_tim + 1;
			ora_tim += temp_time;
			time += temp_time;
			blu_tim = 0;
			ora_num = seq[i].number;
		}
		else if (seq[i].color == 'B')
		{
			temp_time = abs (seq[i].number - blu_num);
			if (temp_time <= ora_tim )
				temp_time = 1;
			else
				temp_time = temp_time - ora_tim + 1;
			blu_tim += temp_time;
			time += temp_time;
			ora_tim = 0;
			blu_num = seq[i].number;
		}
	}
	return time;
}