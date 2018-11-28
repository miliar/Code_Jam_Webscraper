#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

char buf[520];
int a[520][520];
int row[520][520], col[520][520], f[520][520];
int num[520];
int n, m;

void solve(int ti)
{
	int i, j, ai, aj, ans, tot;
	memset(num, 0, sizeof(num));
	while (true)
	{
		bool flag=false;
	for (i=0; i<n; i++)
	 for (j=0; j<m; j++) if (a[i][j]!=-1)
	 {
	 	flag=true;
	 	col[i][j]=row[i][j]=1;
	 	if (j>0 && a[i][j]!=a[i][j-1] && a[i][j-1]!=-1) row[i][j]=row[i][j-1]+1;
	 	if (i>0 && a[i][j]!=a[i-1][j] && a[i-1][j]!=-1) col[i][j]=col[i-1][j]+1;
	 }
	 if (!flag) break;
	 ans=0;
	for (i=0; i<n; i++)
	 for (j=0; j<m; j++) if (a[i][j]!=-1)
	 {
	 	f[i][j]=1;
	 	if (i>0 && j>0 && a[i][j]==a[i-1][j-1])
  		 f[i][j]=min(min(row[i][j], col[i][j]), f[i-1][j-1]+1);
  		if (f[i][j]>ans || f[i][j]==ans && i<ai ||  
  			f[i][j]==ans && i==ai && j<aj)
		{
			ans=f[i][j];
			ai=i;
			aj=j;
		}		
	 }
	 num[ans]++;
	 for (i=ai-ans+1; i<=ai; i++)
	  for (j=aj-ans+1; j<=aj; j++)
	    a[i][j]=-1;
   /*
	if (ans>=3)
	{
		for (i=0; i<n; i++)
		{
			for (j=0; j<m; j++)
			  if (a[i][j]==-1) printf(" ");
			  else printf("%d", a[i][j]);
			  printf("\n");
		}
		printf("\n");
	}
	*/    
	}
	tot=0;
	for (i=n; i>=0; i--)
	  if (num[i]>0) tot++;
	printf("Case #%d: %d\n", ti, tot);
	for (i=n; i>=0; i--)
	  if (num[i]>0) printf("%d %d\n", i, num[i]);

}

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);	
	int T, ti, i, j, k, x;
	scanf("%d", &T);
	for (ti=1; ti<=T; ti++)
	{
		scanf("%d%d", &n, &m);
		memset(a, 0, sizeof(a));
		for (i=0; i<n; i++)
		{
			scanf("%s", buf);
			for (j=0; j<m/4; j++)
			{
				char temp[5];
				temp[0]=buf[j];
				temp[1]='\0';
				sscanf(temp, "%x", &x);
				for (k=0; k<4; k++)
				  if ((1<<k)&x) a[i][j*4+3-k]=1;
			}
		}
		for (i=0; i<n; i++)
		{
			/*
			for (j=0; j<m; j++)
			  printf("%d", a[i][j]);
			  printf("\n");
			  */
		}
		solve(ti);
	}
	return 0;
}
