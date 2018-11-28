#include<cstdio>
#include<cmath>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int N;
	int i;
	char c;
	int a;
	int j;
	for(j = 1; j<=T; j++)
	{
		scanf("%d", &N);
		int time = 0;
		int time1 = 0;
		int time2 = 0;
		int pos1 = 1;
		int pos2 = 1;
		bool pos = true;
		for(i = 1; i<=N; i++)
		{
			while((c = getchar()) == ' ');
			scanf("%d", &a);
			if(c == 'O')
			{
				if(pos == false)
				{
					time1 += abs(a-pos1)+1;
					time+=abs(a-pos1)+1;
				}
				else
				{
					time1 = abs(a-pos1)+1;
					if(time1>time2)
					{
						time+= time1-time2;
						time1 = time1-time2;
					}
					else
					{
						time++;
						time1 = 1;
					}
				}
				pos1 = a;
				pos = false;
			}
			if(c == 'B')
			{
				if(pos == true)
				{
					time2 += abs(a-pos2)+1;
					time+=abs(a-pos2)+1;
				}
				else
				{
					time2 = abs(a-pos2)+1;
					if(time2>time1)
					{
						time+= time2-time1;
						time2 = time2 - time1;
					}
					else
					{
						time++;
						time2 = 1;
					}
				}
				pos2 = a;
				pos = true;
			}
		}
		printf("Case #%d: %d\n", j, time);
	}
	return 0;
}