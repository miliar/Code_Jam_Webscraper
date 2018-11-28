#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <ctime>
#include <numeric>
#include <string.h>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "B-small-attempt1";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}

int dp[10010];
long long mas[1101];

int main()
{
	init();

	int tst;
	scanf("%d",&tst);
	for (int cas = 1;cas<=tst;cas++)
	{
		memset(dp,1,sizeof(dp));
		dp[0]=0;
		long long len;
		int n;
		scanf("%lld%d\n",&len,&n);
		for (int i=0;i<n;i++)  {
			scanf("%lld",&mas[i]);
			for (int j=mas[i];j<=10000;j++)
				dp[j]=min(dp[j],dp[j-mas[i]]+1);
		}
		long long res=-1;
		for (int i=0;i<=10000;i++) if (dp[i]<10010)
		{
			long long left = len - i;
			for (int j=0;j<n;j++) if (left%mas[j]==0)
			{
				if (res==-1 ||	(left/mas[j]+dp[i]<res))
				{
					res = left/mas[j]+dp[i];
				}
			}
		}
		if (res==-1) printf("Case #%d: IMPOSSIBLE\n",cas); else
		printf("Case #%d: %lld\n",cas,res);
	}




  return 0;
}
