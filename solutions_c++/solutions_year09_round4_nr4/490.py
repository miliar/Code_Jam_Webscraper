#include <iostream>
#include <cmath>
using namespace std;

struct node
{
	int x;
	int y;
	int r;
}date[10];

double ans;

double dis(node p1 , node p2)
{
	return sqrt((p1.x - p2.x) * (p1.x - p2.x) * 1.0 + (p1.y - p2.y) * (p1.y - p2.y));
}

int main()
{
	int i , j , t , n , cas;
	double l;
	freopen("D-small-attempt1.in" , "r" , stdin);
	freopen("1.txt" , "w" , stdout);
	scanf("%d" , &t);
	for(cas = 1 ; cas <= t ; cas ++)
	{
		scanf("%d" , &n);
		for(i = 0 ; i < n ; i ++)
		{
			scanf("%d %d %d" , &date[i].x , &date[i].y , &date[i].r);
		}	ans = -1;
		if(n == 1)
		{
			ans = date[0].r;
		}
		for(i = 0 ; i < n ; i ++)
		{
			for(j = i + 1 ; j < n ; j ++)
			{
				l = dis(date[i] , date[j]) + date[i].r + date[j].r;
				l /= 2;
				if(i == 0 && j == 1)
				{
					if(l < date[2].r)
						l = date[2].r;
				}
				else if(i == 0 && j == 2)
				{
					if(l < date[1].r)
						l = date[1].r;
				}
				else
				{
					if(l < date[0].r)
						l = date[0].r;
				}
				if(ans < 0 || ans > l)
					ans = l;
			}
		}
		if(n == 2)
		{
			if(date[1].r > date[0].r)
				ans = date[1].r;
			else
				ans = date[0].r;
		}
		printf("Case #%d: %lf\n" , cas , ans);
	}
	return 0;
}