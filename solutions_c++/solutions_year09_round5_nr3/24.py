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

struct point
{
	int x, y;
	friend bool operator < (point p1, point p2){return p1.x>p2.x;}
};

int miny, maxy;
int n;
point a[128];
set<int> chk[128];

bool f1(int k, int mask, int cols)
{
	if(chk[k].find(mask)!=chk[k].end()) return false;
	chk[k].insert(mask);
	if(k>n) return true;
	int i, j;
	int tmp[16]={0, };
	for(i=1;i<=maxy;i++){tmp[i]=mask&3; mask>>=2;}
	bool v[5]={false, };
	for(i=max(1, a[k].y-1);i<=min(a[k].y+1, maxy);i++) v[tmp[i]]=true;
	int nxt;
	for(i=0;i<cols;i++)
	{
		if(v[i]) continue;
		nxt=0;
		for(j=maxy;j>=1;j--) nxt=(nxt<<2)+((j==a[k].y)?i:tmp[j]);
		if(f1(k+1, nxt, cols)) return true;
	}
	return false;
}

bool f_possible(int k)
{
	int i;
	int st=0;
	for(i=1;i<=maxy;i++) st=(st<<2)+k;
	for(i=1;i<=n;i++) chk[i].clear();
	return f1(1, st, k);
}

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, k;
	int t, tc;
	int ans;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%d", &n);
		miny=999; maxy=0;
		for(i=1;i<=n;i++){fscanf(fp, "%d%d", &a[i].x, &a[i].y); miny=min(miny, a[i].y); maxy=max(maxy, a[i].y);}
		for(i=1;i<=n;i++) a[i].y-=(miny-1);
		maxy-=(miny-1);
		sort(&a[1], &a[n+1]);
		for(k=1;k<=3;k++)
		{
			if(f_possible(k)) break;
		}
		fprintf(ofp, "Case #%d: %d\n", t, k);
		printf("Case #%d: %d\n", t, k);
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
