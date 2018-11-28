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

int n, b;
int ans;
bool conflict(int x, int y)
{
	while(x && y)
	{
		if(x%b==y%b) return true;
		x/=b; y/=b;
	}
	return false;
}
void f1(vector<int>& nums, int cur, int tot)
{
	if(tot==n) ans++;
	int i, j;
	for(i=cur;tot+i<=n;i++)
	{
		for(j=0;j<nums.size();j++)
		{
			if(conflict(nums[j], i)) break;
		}
		if(j<nums.size()) continue;
		nums.push_back(i);
		f1(nums, i+1, tot+i);
		nums.pop_back();
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

	int t, tc;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%d%d", &n, &b);
		vector<int> cur;
		ans=0;
		f1(cur, 1, 0);
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
