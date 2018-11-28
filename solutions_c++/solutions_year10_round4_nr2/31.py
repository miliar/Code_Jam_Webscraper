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

int p;
long long a[4096];
int s[4096], e[4096];
int sp;

long long f_get(int x)
{
	if(x>=sp)
	{
		if(a[x]>0) return -1;
		return 0;
	}
	long long ret=0;
	int k;
	for(k=s[x];k<=e[x];k++) a[k]--;
	long long ltt=f_get(x*2), rtt=f_get(x*2+1);
	for(k=s[x];k<=e[x];k++) a[k]++;
	if(ltt==-1 || rtt==-1) return -1;
	ret=a[x]+ltt+rtt;
	long long lt=f_get(x*2), rt=f_get(x*2+1);
	if(lt!=-1 && rt!=-1 && ret>lt+rt)
		ret=lt+rt;
	return ret;
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
		fscanf(fp, "%d", &p);
		sp=1<<p;
		for(i=sp*2-1;i>=1;i--) fscanf(fp, "%d", &a[i]);
		for(i=sp;i<sp*2;i++){a[i]=p-a[i]; s[i]=e[i]=i;}
		for(i=sp-1;i>=1;i--){s[i]=s[i*2]; e[i]=e[i*2+1];}
		fprintf(ofp, "Case #%d: %lld\n", t, f_get(1));
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
