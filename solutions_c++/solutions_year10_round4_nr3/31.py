#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
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

int n;
bool a[128][128];

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
		memset(a, 0, sizeof(a));
		for(fscanf(fp, "%d", &n);n--;)
		{
			int sx, sy, ex, ey;
			fscanf(fp, "%d%d%d%d", &sx, &sy, &ex, &ey);
			for(i=sx;i<=ex;i++)
			{
				for(j=sy;j<=ey;j++) a[i][j]=1;
			}
		}
		for(k=0;;k++)
		{
			bool flag=false;
			for(i=100;i>=1;i--)
			{
				for(j=100;j>=1;j--)
				{
					if(a[i][j]) flag=true;
					if(a[i-1][j] && a[i][j-1]) a[i][j]=1;
					else if(!a[i-1][j] && !a[i][j-1]) a[i][j]=0;
				}
			}
			if(!flag) break;
		}
		fprintf(ofp, "Case #%d: %d\n", t, k);
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
