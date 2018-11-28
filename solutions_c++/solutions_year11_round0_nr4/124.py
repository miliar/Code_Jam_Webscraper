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
int a[1024];
bool v[1024];

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int t, tc;
	int i, j;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		int n;
		double ans=0.0;
		fscanf(fp, "%d", &n);
		for(i=1;i<=n;i++) fscanf(fp, "%d", &a[i]);
		memset(v, false, sizeof(v));
		for(i=1;i<=n;i++)
		{
			if(a[i]==i || v[i]) continue;
			int len=0;
			for(j=i;!v[j];j=a[j]){len++; v[j]=true;}
			ans+=(double)(len);
		}
		fprintf(ofp, "Case #%d: %.6lf\n", t, ans);
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
