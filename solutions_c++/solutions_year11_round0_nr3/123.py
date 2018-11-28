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

	int t, tc;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		int n;
		int i;
		int tot=0, txor=0;
		int mval=9999999;
		int x;
		fscanf(fp, "%d", &n);
		for(i=1;i<=n;i++)
		{
			fscanf(fp, "%d", &x);
			tot+=x; txor^=x;
			if(mval>x) mval=x;
		}
		fprintf(ofp, "Case #%d: ", t);
		if(txor) fprintf(ofp, "NO\n");
		else fprintf(ofp, "%d\n", tot-mval);
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
