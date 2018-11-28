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

long long n;
bool sieve[1048576];
long long p[100000];

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	
	int i, j;
	long long k;
	sieve[1]=true;
	for(i=2;i<=1000000;i++)
	{
		if(sieve[i]) continue;
		p[++p[0]]=i;
		for(j=i+i;j<=1000000;j+=i) sieve[j]=true;
	}
	int t, tc;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%lld", &n);
		if(n==1){fprintf(ofp, "Case #%d: 0\n", t); continue;}
		int ans=1;
		for(i=1;i<=p[0] && p[i]*p[i]<=n;i++)
		{
			for(k=p[i]*p[i];k<=n;k*=p[i]) ans++;
		}
		printf("%d/%d\n", t, tc);
		fprintf(ofp, "Case #%d: %d\n", t, ans);
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
