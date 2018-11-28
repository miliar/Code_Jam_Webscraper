#include <stdio.h>

int main()
{
	//freopen("A-small.txt", "r", stdin);
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out.txt", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);

	int i, t;
	int j, n;
	scanf("%d", &t);
	for(i = 1; i <= t; i++)
	{
		scanf("%d", &n);
		int po = 1, pb = 1;
		char last = '\0';
		char robot;
		int index;
		int duration = 0;
		int sum = 0;
		int cost = 0;
		for(j = 0; j < n; j++)
		{			
			scanf(" %c %d", &robot, &index);
			if(robot == 'O') {				
				cost = index > po ? index - po : po - index;
				if(robot != last) {
					cost = cost < duration ? 0 : cost - duration;
					duration = 0;
				}
				cost += 1;				
				po = index;
			} else if(robot == 'B') {
				cost = index > pb ? index - pb : pb - index;
				if(robot != last) {
					cost = cost < duration ? 0 : cost - duration;
					duration = 0;
				}
				cost += 1;				
				pb = index;
			}
			sum += cost;
			duration += cost;
			last = robot;
		}
		printf("Case #%d: %d\n", i, sum);
	}
	return 0;
}