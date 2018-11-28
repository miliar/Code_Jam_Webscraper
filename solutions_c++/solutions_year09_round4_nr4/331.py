#include <stdio.h>
#include <math.h>

int n;
int plant[50][3];

double dist(int a[3], int b[3])
{
	return (sqrt((double)((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))) + a[2] + b[2]) / 2;
}

int main()
{
	int i;
	int t, casecnt;
	double can, ans, max;

	scanf("%d", &t);
	for(casecnt = 0; casecnt < t; casecnt++)
	{
		scanf("%d", &n);
		for(i = 0; i < n; i++)
			scanf("%d %d %d", &plant[i][0], &plant[i][1], &plant[i][2]);
		printf("Case #%d: ", casecnt+1);
		if(n <= 2)
		{
			max = -1;
			for(i = 0; i < n; i++)
			{
				if(plant[i][2] > max)
					max = plant[i][2];
			}
			printf("%.6lf\n", max);
		}
		else
		{
			ans = 99999999999;
			can = dist(plant[0], plant[1]);
			
			if(can < plant[2][2]) can = plant[2][2];
			
			if(can < ans) ans = can;
			can = dist(plant[0], plant[2]);
			if(can < plant[1][2]) can = plant[1][2];
			if(can < ans) ans = can;
			can = dist(plant[2], plant[1]);
			if(can < plant[0][2]) can = plant[0][2];
			if(can < ans) ans = can;
			printf("%.6lf\n", ans);
		}
	}

	return 0;
}