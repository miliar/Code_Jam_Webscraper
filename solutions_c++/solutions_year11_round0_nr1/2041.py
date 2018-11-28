#include <cstdio>
int abs(int x)
{
	return (x < 0 ? -x : x);
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("Large.out", "w", stdout);
	int n, t, button;
	char bot;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &t);
		int pos[2] = {1, 1};
		int tm[2] = {0, 0};
		int tshift, time = 0;
		for (int j = 0; j < t; j++)
		{
			scanf("%c%c%d", &bot, &bot, &button);
			int k = 0;
			if (bot == 'B')
				k++;
			tshift = abs(button - pos[k]) + 1;
			tshift -= tm[k];
			if (tshift <= 0)
				tshift = 1;
			time += tshift;
			pos[k] = button;
			tm[k] = 0;
			tm[1 - k] += tshift;
		}
		printf("Case #%d: %d\n", i + 1, time);
	}
	return 0;
}