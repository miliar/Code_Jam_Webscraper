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

const int lim=10000;
int a[128];
int d[lim+1];

int gcd(int x, int y)
{
	while(y){int t=x%y; x=y; y=t;}
	return x;
}

long long L;
int n;
long long ans;

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, j;
	int g;
	int t, tc;
	int maxv;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fprintf(ofp, "Case #%d: ", t);
		fscanf(fp, "%lld%d", &L, &n);
		g=0; maxv=0;
		for(i=1;i<=n;i++)
		{
			fscanf(fp, "%d", &a[i]);
			if(g==0) g=a[i];
			else g=gcd(g, a[i]);
			maxv=max(maxv, a[i]);
		}
		sort(&a[1], &a[n+1]);
		if(L%g){fprintf(ofp, "IMPOSSIBLE\n"); continue;}
		for(i=1;i<=lim;i++) d[i]=-1;
		d[0]=0;
		for(i=0;i<=lim;i++)
		{
			if(d[i]==-1) continue;
			for(j=1;j<=n && i+a[j]<=lim;j++)
			{
				if(d[i+a[j]]==-1 || d[i+a[j]]>d[i]+1)
					d[i+a[j]]=d[i]+1;
			}
		}
		ans=-1;
		for(i=0;i<=lim;i++)
		{
			if((L-i)%maxv || d[i]==-1) continue;
			long long tmp=((L-i)/(long long)(maxv))+d[i];
			if(ans=-1) ans=tmp;
			else if(ans>tmp) ans=tmp;
		}
		fprintf(ofp, "%lld\n", ans);
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
