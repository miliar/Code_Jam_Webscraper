#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#define clr(a) memset(a, 0, sizeof(a))

#define DEBUG 1

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
#endif
}


int edge[500][500];
int n,k;
int in[100][100];
int cmp[200][200];



void readdata()
{
	scanf("%d%d", &n, &k);
	for(int i = 0; i < n; i++)
		for(int j = 0; j < k; j++)
			scanf("%d", &in[i][j]);
	for(int i = 0; i < n; i++)
		for(int j = i+1; j < n; j++)
		{
			int ar[3];
			clr(ar);
			for(int t = 0; t < k; t++)
			{
				if (in[i][t] < in[j][t])
					ar[0] = 1;
				else if (in[i][t] == in[j][t])
					ar[1] = 1;
				else
					ar[2] = 1;					
			}
			if (ar[1] == 1|| ar[0]+ar[2] == 2)
				cmp[i][j] = cmp[j][i] = 0;
			else if (ar[0])
			{
				cmp[i][j] = 1;
				cmp[j][i] = -1;
			}
			else
			{
				cmp[i][j] = -1;
				cmp[j][i] = 1;
			}
		}
}
int s,t;

void buildgraph()
{
	s = 2*n;
	t = s+1;
	clr(edge);
	for(int i = 0; i < n; i++)	
	{
		edge[s][i] = edge[i+n][t] = 1;
	}
	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++)
			if(cmp[i][j] == 1)
				edge[i][j+n] = 1;

}

bool use[300];

bool dfs(int v)
{
	use[v] = true;
	if (v == t)
		return true;
	for(int i = 0; i < 2*n+2; i++)
		if (!use[i] && edge[v][i])
		{
			if (dfs(i))
			{
				edge[v][i] --;
				edge[i][v] ++;
				return true;
			}
		}
	return false;	
}


void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	readdata();
	buildgraph();
	int ans = 0;
	do
	{
		clr(use);
	}
	while(dfs(s));
	//dbg("-- %d\n", n);

	clr(use);
	for(int i = 0; i < n; i++)
	{
		if (edge[t][i+n])
			continue;
		ans++;
	}
	printf("%d\n", ans);

}





int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);
		return 0;
}
