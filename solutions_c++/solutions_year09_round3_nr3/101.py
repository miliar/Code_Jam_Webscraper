#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<iostream>
#include<sstream>
#include<fstream>
#include<cmath>

using namespace std;

const int MAXN = 102;



int dp[MAXN][MAXN];
int N, P;

vector<int> pos;

const int inf = 2000000000;

int solve(int a, int b)
{
	int & ret = dp[a][b];
	if(ret >=0)
		return ret;
	
	if(b-a == 1)
		return ret = 0;
	
	ret = inf;

	for(int i=a+1; i<b; i++)
	{
		ret = min(ret, (pos[b]-pos[a]-2) + solve(a, i)+ solve(i, b));
	}

	return ret;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int numCase;
	scanf("%d", &numCase);
	for(int c=1; c<=numCase; c++)
	{
		pos.clear();
		memset(dp, -1, sizeof(dp));
		
		scanf("%d %d", &P, &N);
		pos.push_back(0);
		int tmp;
		for(int i=0; i<N; ++i)
		{
			scanf("%d", &tmp);
			pos.push_back(tmp);
		}
		pos.push_back(P+1);

		int ret = solve(0, pos.size()-1);

		printf("Case #%d: %d\n", c, ret);
	}

	return 0;
}
