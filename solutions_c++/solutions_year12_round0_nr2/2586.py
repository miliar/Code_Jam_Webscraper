#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<list>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define GI(x) scanf("%d", &x);
#define FORN(i, n) for(int i = 0; i < n; i++)
#define FOR(i, start, end) for(int i = start; i < end; i++)
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 1000000000
using namespace std;
int N, S, p;
VI v;
int dp[110][110];
int get_best(int total, int is_surprise)
{
	int i, j, k;
	for(i = 0; i <= 10; i++)
	{
		for(j = i; j <= 10; j++)
		{
			for(k = j; k <= 10; k++)
			{
				if(i+j+k != total)
					continue;
				if(is_surprise && k - i == 2)
					return k;
				if(!is_surprise && k - i < 2)
					return k;
			}
		}
	}
	return -1;
}

int solve(int pos, int sur)
{
	//cout<<pos<<" "<<sur<<endl;
	if(pos >= N && sur == 0)
		return 0;
	if(pos >= N && sur > 0)
		return -10000;
	int &ret = dp[pos][sur];
	if(ret != -1)
		return ret;
	ret = max(ret, solve(pos+1, sur) + (get_best(v[pos], 0) >= p ? 1 : 0));
	if(sur > 0 && get_best(v[pos], 1) != -1)
	ret = max(ret, solve(pos+1, sur-1) + (get_best(v[pos], 1) >= p ? 1: 0));

	return ret;
}
int main()
{
	int tes;
	GI(tes);
	for(int c = 1; c <= tes; c++)
	{
		CLRM(dp);
		GI(N);
		GI(S);
		GI(p);
		v.clear();
		for(int i = 0; i < N; i++)
		{
			int x;
			GI(x);
			v.push_back(x);
		}
		int ans = solve(0, S);
		printf("Case #%d: %d\n", c, ans);
	}
	return 0;
}

