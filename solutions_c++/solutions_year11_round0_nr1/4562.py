#include <iostream>
#include <math.h>
using namespace std;
#define DEBUG
struct node
{
	int flag;
	int location;
}N[1001];
int main()
{
#ifdef DEBUG
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int i, j, k, t, n, b, pre_O, pre_B, mintime = 0, time_left_O, time_left_B;
	char a[10];
	int walktime = 0, cas = 0;
	scanf("%d", &t);
	while(t--)
	{
		mintime = 0;
		time_left_B = time_left_O = 0;
		scanf("%d", &n);
		for(int i = 0; i < n; i ++)
		{
			scanf("%s %d", &a, &b);
			if(a[0] == 'O')
				N[i].flag = 0;
			else N[i].flag = 1;
			N[i].location = b;
		}
		pre_O = 1;
		pre_B = 1;
		for(i = 0 ; i < n; i ++)
		{
			if(N[i].flag == 0)
			{
			
				walktime = abs(N[i].location - pre_O) - time_left_O;
				if(walktime < 0 ) walktime = 0;
				pre_O = N[i].location;
				mintime += walktime + 1;
				time_left_O = 0;
				time_left_B += walktime + 1;
			}
			else
			{
				walktime = abs(N[i].location - pre_B) - time_left_B;
				if(walktime < 0 ) walktime = 0;
				pre_B = N[i].location;
				mintime += walktime + 1;
				time_left_B = 0;
				time_left_O += walktime + 1;
			}
		}
		printf("Case #%d: %d\n", ++cas, mintime);
	}
}