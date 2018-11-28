#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <string.h>
#include <math.h>
using namespace std;
char s[64];
int a[64],na,ns;
__int64 k2[64];
__int64 cur;
bool dfs(int i)
{
	if (i==na)
	{
		__int64 k = int(sqrt(cur));
		return k*k==cur;
	}
	s[a[i]]='0';
	if (dfs(i+1)) return true;
	s[a[i]]='1';
	cur+=k2[ns-1-a[i]];
	if (dfs(i+1)) return true;
	cur-=k2[ns-1-a[i]];
	return false;
}
int main()
{
	int tc,cas,i,j;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	k2[0]=1;
	for(i=1;i<64;++i) k2[i]=k2[i-1]*2;
	scanf("%d",&tc);
	for (cas=1;cas<=tc;++cas)
	{
		scanf("%s", s);
		na=0;
		cur=0;
		ns=strlen(s);
		for (i=0;s[i];++i) 
			if (i>0&&s[i]=='?') a[na++]=i;
			else cur += int(s[i]=='1')*k2[ns-i-1];
		dfs(0);
		printf("Case #%d: %s\n", cas,s);
	}
	return 0;
}