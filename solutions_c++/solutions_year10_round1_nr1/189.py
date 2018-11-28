#include <stdio.h>
#define swap(x,y) {char t=x;x=y;y=t;}

const int T = 100;
const int N = 50;

const int R = 1<<0;
const int B = 1<<1;

typedef struct point
{
	int x, y;
}point;

const point D[] = {{0,1},{1,0},{1,1},{-1,1}};
const int Dn = 4;

main()
{
	int t, n, k;
	int ans;
	char map[N][N+1];
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		ans=0;
		scanf("%d%d", &n, &k);
		for (int j=0;j<n;j++)
			scanf("%s", &map[j][0]);
		
		for (int j=0;j<n;j++)
		{
			int pos=n-1;
			for (int l=n-1;l>=0;l--)
				if (map[j][l]!='.')
				{
					swap(map[j][l],map[j][pos])
					pos--;
				}
		}
		
		for (int j=0;j<n;j++)
		{
			for (int l=0;l<n;l++)
			{
				if (map[j][l]=='.')
					continue;
				for (int m=0;m<Dn;m++)
				{
					int check=1;
					
					for (int o=1;o<k;o++)
						if ((j+o*D[m].x)>=n || (j+o*D[m].x)<0 || (l+o*D[m].y)>=n || map[j+o*D[m].x][l+o*D[m].y]!=map[j][l])
							check=0;
					
					if (!check)
						continue;
					
					if (map[j][l]=='R')
						ans|=R;
					if (map[j][l]=='B')
						ans|=B;
				}
			}
		}
		
		printf("Case #%d: ", i);
		if ((ans&R) && (ans&B))
			printf("Both");
		else if (ans&R)
			printf("Red");
		else if (ans&B)
			printf("Blue");
		else
			printf("Neither");
		printf("\n");
	}
}
