#include<iostream>
#include<queue>
#include<stdio.h>
#include<stdlib.h>
#include<queue>

using namespace std;

int cas()
{
	int n, i;
	
	scanf("%d", &n);
	
	vector<int> v(n);
	vector<bool> bot(n);

	char c;
	int but;

	for (i = 0; i < n; i++)
	{
		scanf("%*c%c%d", &c, &but);
		v[i] = but;
		bot[i] = (c != 'O');
	}
	int cur[] = {1, 1};
	int tot_time = 0, lst_time = 0, need_time;

	
	for (i = 0; i < n;)
	{
		need_time = abs(v[i] - cur[bot[i]]);
		if (need_time <= lst_time)
		{
			tot_time += 1;
			lst_time = 1;
		}
		else
		{
			tot_time += (need_time - lst_time + 1);
			lst_time = need_time - lst_time + 1;
		}
		i++;
		while (i < n && bot[i] == bot[i-1])
		{
			tot_time += abs(v[i] - v[i-1]) + 1;
			lst_time += abs(v[i] - v[i-1]) + 1;
			i++;
		}
		cur[bot[i-1]] = v[i-1];
	}
	return tot_time;	
}
int main()
{
	int t;
	scanf("%d", &t);

	int i;
	for (i = 1; i <=t; i++)
		printf("Case #%d: %d\n", i, cas());
	return 0;
}
