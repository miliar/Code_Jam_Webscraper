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

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int n;
	int i, j;
	long long ans;
	int t, tc;
	int t1, t2;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%d", &n);
		map<int, int> a;
		map<int, int>::iterator it;
		for(i=1;i<=n;i++)
		{
			fscanf(fp, "%d%d", &t1, &t2);
			a[t1]=t2;
		}
		ans=0;
		while(true)
		{
			bool flag=false;
			for(it=a.begin();it!=a.end();it++)
			{
				if(it->second<2) continue;
				int tmp=(it->second)/2;
				flag=true;
				ans+=tmp;
				a[it->first-1]+=tmp;
				a[it->first+1]+=tmp;
				it->second&=1;
				break;
			}
			if(!flag) break;
		}
		fprintf(ofp, "Case #%d: %lld\n", t, ans);
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
