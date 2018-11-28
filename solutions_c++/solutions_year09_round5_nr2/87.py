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
#define BASE 10009
using namespace std;

int n, K;
char pbuf[128];
char a[32][64];
int d[8];
int wcnt[32];
void f1(int cnt, int s, int tot)
{
	d[cnt]+=tot;
	if(cnt==K) return;
	int i, j;
	int ntot, tmp;
	for(i=s;i<=n;i++)
	{
		for(j=0;a[i][j];j++) wcnt[a[i][j]-'a'+1]++;
		ntot=0; tmp=1;
		for(j=0;pbuf[j];j++)
		{
			if(pbuf[j]=='+'){ntot=(ntot+tmp)%BASE; tmp=1;}
			else tmp=(tmp*wcnt[pbuf[j]-'a'+1])%BASE;
		}
		f1(cnt+1, ntot);
		for(j=0;a[i][j];j++) wcnt[a[i][j]-'a'+1]--;
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
		fscanf(fp, "%s%d%d", pbuf, &K, &n);
		strcat(pbuf, "+");
		for(i=1;i<=n;i++) fscanf(fp, "%s", a[i]);
		for(i=1;i<=K;i++) d[i]=0;
		for(i=1;i<=26;i++) wcnt[i]=0;
		f1(0, 0);
		printf("%d done\n", t);
		fprintf(ofp, "Case #%d:", t);
		for(i=1;i<=K;i++) fprintf(ofp, " %d", d[i]%BASE);
		fprintf(ofp, "\n");
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
