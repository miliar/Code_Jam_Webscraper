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
using namespace std;

int n, m;
int a[512][512];
int b[512][512];
int x[512][512];
int y[512][512];
int gx[512][512];
int gy[512][512];

inline int rect(int sx, int ex, int sy, int ey)
{
	return a[ex][ey]-a[sx-1][ey]-a[ex][sy-1]+a[sx-1][sy-1];
}
inline int rectx(int sx, int ex, int sy, int ey)
{
	return gx[ex][ey]-gx[sx-1][ey]-gx[ex][sy-1]+gx[sx-1][sy-1];
}
inline int recty(int sx, int ex, int sy, int ey)
{
	return gy[ex][ey]-gy[sx-1][ey]-gy[ex][sy-1]+gy[sx-1][sy-1];
}

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	
	int t, tc;
	int i, j, k;
	char buf[512];
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%d%d%*d", &n, &m);
		for(i=1;i<=n;i++)
		{
			fscanf(fp, "%s", &buf[1]);
			for(j=1;j<=m;j++)
			{
				a[i][j]=a[i][j-1]+a[i-1][j]-a[i-1][j-1]+buf[j]-'0'; b[i][j]=buf[j]-'0';
				gx[i][j]=i*b[i][j]; gy[i][j]=j*b[i][j];
			}
		}
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				gx[i][j]+=gx[i-1][j]+gx[i][j-1]-gx[i-1][j-1];
				gy[i][j]+=gy[i-1][j]+gy[i][j-1]-gy[i-1][j-1];
			}
		}
		k=min(n, m);
		int ans=-1;
		for(;k>2 && ans==-1;k--)
		{
			for(i=k;i<=n && ans==-1;i++)
			{
				for(j=k;j<=m && ans==-1;j++)
				{
					int x=rectx(i-k+1, i, j-k+1, j);
					int y=recty(i-k+1, i, j-k+1, j);
					if(k&1)
					{
						int h=(k-1)/2;
						x-=(i-h)*rect(i-k+1, i, j-k+1, j);
						y-=(j-h)*rect(i-k+1, i, j-k+1, j);
						if(y-h*(b[i][j]+b[i-k+1][j]-b[i][j-k+1]-b[i-k+1][j-k+1])==0 &&
						   x-h*(b[i][j]+b[i][j-k+1]-b[i-k+1][j]-b[i-k+1][j-k+1])==0) ans=k;
					}
					else
					{
						int h=k/2;
						x-=(i-h)*rect(i-k+1, i, j-k+1, j)+rect(i-k+1, i-h, j-k+1, j);
						y-=(j-h)*rect(i-k+1, i, j-k+1, j)+rect(i-k+1, i, j-k+1, j-h);
						if(y-h*(b[i][j]+b[i-k+1][j]-b[i][j-k+1]-b[i-k+1][j-k+1])==0 &&
						   x-h*(b[i][j]+b[i][j-k+1]-b[i-k+1][j]-b[i-k+1][j-k+1])==0) ans=k;
					}
				}
			}
		}
		fprintf(ofp, "Case #%d: ", t);
		if(ans==-1) fprintf(ofp, "IMPOSSIBLE\n");
		else fprintf(ofp, "%d\n", ans);
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
