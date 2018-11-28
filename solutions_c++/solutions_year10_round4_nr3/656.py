#include<cstdio>
#include<cstring>
const int maxn = 102;
int a[maxn][maxn];
int b[maxn][maxn];

int solve()
{
	int s = 0;
	bool flag;
	while(1)
	{
		memcpy(b , a , sizeof(a));
		flag = false;
		int i , j;
		for(i = 1;i <= 100;i++)
			for(j = 1;j <= 100;j++)
			{
				if(b[i][j] == 1)
				{
					flag = true;
					if(b[i - 1][j] == 0 && b[i][j - 1] == 0) a[i][j] = 0;
					else a[i][j] = 1;
				}
				else
				{
					if(b[i - 1][j] == 1 && b[i][j - 1] == 1) a[i][j] = 1;
					else a[i][j] = 0;
				}
			}
		if(!flag) return s;
		s++;
	}
}

int main()
{
//	freopen("C-small-attempt0.in" , "r" , stdin);
//	freopen("1.txt" , "w" , stdout);
	int t , p;
	scanf("%d" , &t);
	for(p = 1;p <= t;p++)
	{
		int i;
		int n;
		scanf("%d" , &n);
		memset(a , 0 , sizeof(a));
		for(i = 0;i < n;i++)
		{
			int x1 , x2 , y1 , y2;
			int j , k;
			scanf("%d%d%d%d" , &x1 , &y1 , &x2 , &y2);
			for(j = x1;j <= x2;j++)
				for(k = y1;k <= y2;k++)
					a[j][k] = 1;
		}
		printf("Case #%d: %d\n" , p , solve());
	}
	return 0;
}