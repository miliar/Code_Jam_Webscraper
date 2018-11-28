#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<memory.h>
#define INF 99999
int n, m, r;
char a[16][16];
int ans;
bool chk[11][7][61][64][64];
void f1(int x, int y, int dig, int curmask, int nxtmask)
{
	if(ans<=dig) return;
	if(x==n){ans=dig; return;}
	if(chk[x][y][dig][curmask][nxtmask]) return;
	chk[x][y][dig][curmask][nxtmask]=true;
	int i;
	for(i=x+1;i<=n && a[i][y]=='.' || (i==x+1 && (nxtmask&(1<<(y-1))));i++);
	if(i-1-x>r) return;
	if(i-1==x+1){f1(i-1, y, dig, nxtmask, 0); return;}
	else if(i-1>x+1){f1(i-1, y, dig, 0, 0); return;}
	if(y>1 && (a[x][y-1]=='.' || curmask&(1<<(y-1-1)))) f1(x, y-1, dig, curmask, nxtmask);
	if(y<m && (a[x][y+1]=='.' || curmask&(1<<(y+1-1)))) f1(x, y+1, dig, curmask, nxtmask);
	if(y>1 && a[x+1][y-1]=='#' && !(nxtmask&(1<<(y-1-1))))
	{
		if(a[x][y-1]=='.' || curmask&(1<<(y-1-1)))
			f1(x, y, dig+1, curmask, nxtmask|(1<<(y-1-1)));
	}
	if(y<m && a[x+1][y+1]=='#' && !(nxtmask&(1<<(y+1-1))))
	{
		if(a[x][y+1]=='.' || curmask&(1<<(y+1-1)))
			f1(x, y, dig+1, curmask, nxtmask|(1<<(y+1-1)));
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

	int i;
	int t, tc;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%d%d%d", &n, &m, &r);
		for(i=1;i<=n;i++) fscanf(fp, "%s", &a[i][1]);
		for(i=1;i<=m;i++) a[n+1][i]='#';
		ans=INF;
		memset(chk, false, sizeof(chk));
		f1(1, 1, 0, 0, 0);
		fprintf(ofp, "Case #%d: ", t);
		if(ans==INF) fprintf(ofp, "No\n");
		else fprintf(ofp, "Yes %d\n", ans);
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
