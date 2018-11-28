#include <iostream>

int main()
{
	freopen("C-small-attempt0.in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	int total;
	int r,k,n;
	int g[20];
	scanf("%d",&t);
	for(int i = 1; i<=t; i++)
	{
		scanf("%d%d%d",&r,&k,&n);
		for(int j = 0; j<n;j++)
		{
			scanf("%d",&g[j]);
		}
		total = 0;
		int point = 0;
		int begin,end;
		int temp = 0;
		for(int z = 0; z < r; z++)
		{
			temp = 0;
			begin = point;
			end = point;
			while(temp + g[point] <= k)
			{
				temp += g[point];
				point++;
				if(point > n-1) point = 0;
				end = point;
				if(begin == point) break;
			}
			total += temp;
		}
		printf("Case #%d: %d\n", i, total);
	}
	return 0;
}