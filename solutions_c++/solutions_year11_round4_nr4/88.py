#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;

int n, m;
int d[40][40];
int a[40][40];
int ans;

int v2[40];
bool v[40];

void bt(int x)
{
	int i, j;
	v2[d[1][x]]=x;
	if(x==1)
	{
		memset(v, false, sizeof(v));
		for(i=0;i<=d[1][2]-1;i++)
		{
			v[v2[i]]=true;
			for(j=1;j<=n;j++)
			{
				if(a[v2[i]][j]) v[j]=true;
			}
		}
		int tot=0;
		for(i=1;i<=n;i++) tot+=v[i];
		ans=max(ans, tot);
		return;
	}
	for(i=1;i<=n;i++)
	{
		if(a[x][i] && d[1][i]==d[1][x]-1) bt(i);
	}
}

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	
	int i, j, k;
	int t, tc;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%d%d", &n, &m);
		memset(a, 0, sizeof(a));
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++) d[i][j]=n+1;
			d[i][i]=0;
		}
		while(m--)
		{
			int t1, t2;
			fscanf(fp, "%d,%d", &t1, &t2);
			t1++; t2++;
			a[t1][t2]=a[t2][t1]=1;
			d[t1][t2]=d[t2][t1]=1;
		}
		for(k=1;k<=n;k++)
		{
			for(i=1;i<=n;i++)
			{
				for(j=1;j<=n;j++) d[i][j]=min(d[i][j], d[i][k]+d[k][j]);
			}
		}
		ans=0;
		for(i=1;i<=n;i++)
		{
			if(d[1][i]==d[1][2]-1 && a[i][2])
				bt(i);
		}
		fprintf(ofp, "Case #%d: %d %d\n", t, d[1][2]-1, ans-d[1][2]);
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
