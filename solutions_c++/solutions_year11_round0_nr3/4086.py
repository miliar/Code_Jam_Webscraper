#include<stdio.h>
#include<string>
#include<cmath>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

map<pair<int,int>,int> memo[1002][2][2];
int n;
vector<int> can;

int solve(int index,int sealsum,int patsum,int flag1,int flag2)
{
	if (index == n)
	{
		if (sealsum - patsum == 0 && flag1 == 1 && flag2 == 1) return 0;
		else return -999999999;
	}
	if (memo[index][flag1][flag2].count(make_pair(sealsum,patsum)) != 0) return memo[index][flag1][flag2][make_pair(sealsum,patsum)];
	int ret = max(can[index] + solve(index + 1,sealsum ^ can[index],patsum,1,flag2),solve(index + 1,sealsum, patsum ^ can[index],flag1,1));
	memo[index][flag1][flag2][make_pair(sealsum,patsum)] = ret;
	return ret;
}

int main()
{
	freopen("In.in","r",stdin);
	freopen("Out.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int x = 1; x <= t;x++)
	{
		can.clear();
		scanf("%d",&n);
		for(int i = 0; i <= n + 1;i++){ memo[i][0][0].clear();memo[i][0][1].clear();memo[i][1][0].clear();memo[i][1][1].clear();}
		for(int i = 0; i < n;i++)
		{
			int c;
			scanf("%d",&c);
			can.push_back(c);
		}
		int ret = solve(0,0,0,0,0);
		if (ret < 0)printf("Case #%d: NO\n",x); 
		else printf("Case #%d: %d\n",x,ret); 
		
	}
	//while(true);
}