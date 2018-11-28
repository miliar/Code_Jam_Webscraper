#include <stdio.h>
int n;
int m, v;
int ret = 0xfffffff;
int node[100000];
int pause;
int sign[100000];

int write(int root)
{
	if (root > pause)
	{
		return node[root];
	}
	else
	{
		if (node[root] == 1)
			return write(root*2) & write(root*2+1);
		else
			return write(root*2) | write(root*2+1);
	}
}

int dfs(int step, int num)
{
	int i,res;
	if (step > pause)
	{
		res = write(1);
		if (res == v && num < ret)
		{
			ret = num;
		}
		return 0;
	}
	for (i = 0;  i<= sign[step] ;  i++)
	{
		if (i == 1)
		{
			if (node[step] == 0)
				node[step] = 1;
			else
				node[step] = 0;

			dfs(step+1, num+1);
			if (node[step] == 0)
				node[step] = 1;
			else
				node[step] = 0;
		}
		else
			dfs(step+1, num);
	}
}



int main(int argc, char *argv[])
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d", &n);
	for (int i=0; i<n; i++)
	{
		ret = 0xfffffff;
		scanf("%d%d", &m, &v);
		pause = (m-1)/2;
		for (int j = 1; j<=pause ; j++)
		{
			scanf("%d%d",&node[j], &sign[j]);
		}
		for (int j = pause +1 ; j<=m ; j++)
		{
			scanf("%d", &node[j]);
			sign[j] = 0;
		}
		dfs(1, 0);
		if (ret != 0xfffffff)
		{
			printf("Case #%d: %d\n", i+1, ret);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n", i+1);
		}
	}
	
	return 0;
}
