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

double S, R, T;
int n;
double tot[110];

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
		memset(tot, 0, sizeof(tot));
		fscanf(fp, "%lf%lf%lf%lf%d", &tot[0], &S, &R, &T, &n);
		for(i=1;i<=n;i++)
		{
			int t1, t2, t3;
			fscanf(fp, "%d%d%d", &t1, &t2, &t3);
			tot[t3]+=(double)(t2-t1);
			tot[0]-=(double)(t2-t1);
		}
		double ans=0.0;
		for(i=0;i<=100;i++)
		{
			if(tot[i]/(R+(double)(i))<T)
			{
				ans+=(tot[i]/(R+(double)(i)));
				T-=(tot[i]/(R+(double)(i)));
			}
			else
			{
				ans+=T; tot[i]-=((R+(double)(i))*T); T=0.0;
				ans+=(tot[i]/(S+(double)(i)));
			}
		}
		fprintf(ofp, "Case #%d: %.10lf\n", t, ans);
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
