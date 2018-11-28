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
#define max(a, b) (((a)>(b))?(a):(b))
#define min(a, b) (((a)<(b))?(a):(b))
using namespace std;

int gcd(int x, int y)
{
	if(x<0) x=-x;
	if(y<0) y=-y;
	int t;
	while(y){x%=y; t=x; x=y; y=t;}
	return x;
}

int a[5];

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i;
	int n;
	int g;
	int t, tc;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%d", &n);
		for(i=1;i<=n;i++) fscanf(fp, "%d", &a[i]);
		g=0;
		for(i=2;i<=n;i++)
		{
			if(g==0) g=a[i]-a[1];
			else g=gcd(g, a[i]-a[1]);
		}
		if(g<0) g=-g;
		fprintf(ofp, "Case #%d: %d\n", t, (g-(a[1]%g))%g);
	}
	
	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
