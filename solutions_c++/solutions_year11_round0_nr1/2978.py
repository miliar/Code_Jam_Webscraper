#include<iostream>
#include<queue>
#include<stdio.h>
#include<stdlib.h>
#include<queue>

using namespace std;

int function()
{
	int n, i;
	
	cin >> n;
	
	vector<int> x(n);
	vector<bool> bot(n);

	char c;
	int but;

	for (i = 0; i < n; i++)
	{
		scanf("%*c%c%d", &c, &but);
		x[i] = but;
		bot[i] = (c != 'O');
	}

	int cur[] = {1, 1};
	int tottime = 0, lsttime = 0, needtime;

	
	for (i = 0; i < n;)
	{
		needtime = abs(x[i] - cur[bot[i]]);
		if (needtime <= lsttime)
		{
			tottime += 1;
			lsttime = 1;
		}
		else
		{
			tottime += (needtime - lsttime + 1);
			lsttime = needtime - lsttime + 1;
		}
		i++;
		while (i < n && bot[i] == bot[i-1])
		{
			tottime += abs(x[i] - x[i-1]) + 1;
			lsttime += abs(x[i] - x[i-1]) + 1;
			i++;
		}
		cur[bot[i-1]] = x[i-1];
	}
	return tottime;	
}

int main()
{
	int t;
	cin >> t;

	int i;
	for (i=1;i<=t;i++)
		printf("Case #%d: %d\n", i, function());

	return 0;
}
