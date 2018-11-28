#include<cstdio>
#include<cstring>

bool flag[2000];
int a[2000];

int ret = 0;
int ddd = 0;
void dfs(int x)
{
	while(!flag[x])
	{
		flag[x] = true;
		x = a[x];
		ddd++;
	}
}

int main()
{
//	freopen("1.txt" , "r" , stdin);
//	freopen("2.txt" , "w" , stdout);
	int t;
	scanf("%d" , &t);
	int ii = 0;
	while(t--)
	{
		int n;
		scanf("%d" , &n);
		int i;
		for(i = 1;i <= n;i++)
			scanf("%d" , &a[i]);
		ret = 0;
		memset(flag , false , sizeof(flag));
		for(i = 1;i <= n;i++)
		{
			if(!flag[i])
			{
				ddd = 0;
				dfs(i);
				if(ddd != 1)
					ret += ddd;
			}
		}
		printf("Case #%d: %d\n" , ++ii , ret);
	}
	return 0;
}