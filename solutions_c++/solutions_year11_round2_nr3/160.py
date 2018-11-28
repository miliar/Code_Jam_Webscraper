#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;
int mat[10][10];
int room[100][10];
int len[100];
int rn;
int n, m, label;

vector<int>  col[10];
int had[100][100];

int a[10], ans;

int tot[100];

void GO(int x, int y)
{
	int i;
	room[rn][0] = x;
	room[rn][1] = y;
	len[rn]=2;
	while (true)
	{
		for (i=y; i!=x; i=(i+1)%n)
		  if (mat[y][i]) room[rn][len[rn]]=i;
		y = room[rn][len[rn]];
		len[rn]++;
		if (mat[y][x]) return;
	}
}

bool is_unique(int x)
{
	int i, j;
	for (i=0; i<x; i++)
	{
		for (j=0; j<n; j++)
		  if (room[i][j]!=room[x][j]) break;
		if (j==n) return false;
	}
	return true;
}


bool search(int x)
{
	int i, j;
	if (x==n)
	{
		for (i=0; i<label; i++)
		   if (tot[i]!=ans) return false;
		return true;   
	}
	for (i=0; i<ans; i++)
	{
		a[x]=i;
		for (j=0; j<col[x].size(); j++)
		{
		  had[ col[x][j] ][i]++;
		  if (had[ col[x][j] ][i]==1) tot[col[x][j]]++;
		}
		if (search(x+1)) return true;
		for (j=0; j<col[x].size(); j++)
		{
		  had[ col[x][j] ][i]--;
		  if (had[ col[x][j] ][i]==0) tot[col[x][j]]--;
		}
		a[x]=0;		
	}
	return false;
}

int main()
{
	int T, cas, i, j;
	int b[10], e[10];
	scanf("%d", &T);
	for (cas=1; cas<=T; cas++)
	{
		scanf("%d%d", &n, &m);
		for (i=0; i<m; i++)
		 scanf("%d", &b[i]);
		for (i=0; i<m; i++)
		  scanf("%d", &e[i]);
		memset(mat, 0, sizeof(mat));  
		for (i=0; i<n; i++)
		{
		  mat[i][(i+1)%n]=true;
		  col[i].clear();
		}
		for (i=0; i<m; i++)
		  mat[b[i]-1][e[i]-1] =  mat[e[i]-1][b[i]-1] = true;
		  
		rn=0;  
		for (i=0; i<n; i++)
		 for (j=i+1; j<n; j++)
		  if (mat[i][j])
		  {
		  	memset(room[rn], 0, sizeof(room[rn]));
		  	len[rn]=0;
		  	GO(i, j);
		  	rn++;
		  }
		
		label=0;
		for (i=0; i<rn; i++)
		{
			sort(room[i], room[i]+len[i]);
			if (is_unique(i)) 
			{
				for (j=0; j<len[i]; j++)
		  			col[room[i][j]].push_back(label);
				label++;  
			}
		}
		int bak[10];
		for (ans=1; ans<=n; ans++)
		{
			memset(had, 0, sizeof(had));
			memset(tot, 0, sizeof(tot));
			for (i=0; i<n; i++)
			  bak[i]=a[i];
			if (!search(0)) break;
		}
		ans--;
		
		printf("Case #%d: %d\n", cas, ans);
		for (i=0; i<n; i++)
		  if (i==n-1) printf("%d\n", bak[i]+1);
		  else printf("%d ", bak[i]+1);

	}
	return 0;
}
/*
2
4 1
2
4
8 3
1 1 4
3 7 7

*/