#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define two(X) (1<<(X))
#define contain(S,X) (((S)&two(X))!=0)

int n,m;
int f[10][10][two(12)];
int A[10][10];

int solve(int x,int y,int set)
{
	if (x==n) return 0;
	if (y==m) return solve(x+1,0,set);
	int &ret=f[x][y][set];
	if (ret!=-1) return ret;
	ret=solve(x,y+1,(set<<1)&(two(12)-1));
	bool good=true;
	if (A[x][y]==0) good=false;
	if (x-1>=0 && y-1>=0 && contain(set,m)) good=false;
	if (x-1>=0 && y+1<m && contain(set,m-2)) good=false;
	if (y-1>=0 && contain(set,0)) good=false; 
	if (good) 
	{
		int tmp=solve(x,y+1,((set<<1)+1)&(two(12)-1))+1;
		if (tmp>ret) ret=tmp;
	}
	return ret;
}
int main()
{
//	freopen("input.txt","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d:",caseId);
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++) 
		{
			char buf[200];
			scanf("%s",buf);
			for (int j=0;j<m;j++) A[i][j]=(int)(buf[j]=='.');
		}
		memset(f,255,sizeof(f));
		int ret=solve(0,0,0);
		printf(" %d\n",ret);
		fflush(stdout);
	}
	return 0;
}

