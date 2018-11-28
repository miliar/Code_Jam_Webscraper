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

int n, m;

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	
	int t, tc;
	int i;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%d", &n);
		char buf[3];
		int x;
		vector<int> oo, bb;
		vector<pair<char, int> > seq;
		int i, j, k;
		int co, cb;
		for(i=1;i<=n;i++)
		{
			fscanf(fp, "%s%d", buf, &x);
			if(buf[0]=='O'){oo.push_back(x); seq.push_back(make_pair('O', x));}
			else{bb.push_back(x); seq.push_back(make_pair('B', x));}
		}
		co=1; cb=1;
		int ans=0;
		for(i=j=k=0;i<oo.size() && j<bb.size();k++)
		{
			if(seq[k].first=='O')
			{
				ans+=abs(co-oo[i])+1;
				x=min(abs(co-oo[i])+1, abs(cb-bb[j]));
				if(cb<bb[j]) cb+=x;
				else cb-=x;
				co=oo[i++];
			}
			else
			{
				ans+=abs(cb-bb[j])+1;
				x=min(abs(cb-bb[j])+1, abs(co-oo[i]));
				if(co<oo[i]) co+=x;
				else co-=x;
				cb=bb[j++];
			}
		}
		while(i<oo.size()){ans+=abs(co-oo[i])+1; co=oo[i++];}
		while(j<bb.size()){ans+=abs(cb-bb[j])+1; cb=bb[j++];}
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
