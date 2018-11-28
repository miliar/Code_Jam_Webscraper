#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <cmath>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cstdio>
#include <cctype>
#include <string>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

const int maxn = 1100;

struct Node
{
	int idx;
	int miss;
};

bool operator<(Node a, Node b)
{
	if(a.miss != b.miss)
		return a.miss < b.miss;
	return a.idx < b.idx;
}

Node team[maxn];
int s[15][maxn];
int p, n;

int solve(int id)
{
	int dep = p-1;
	int tid = team[id].idx/2;
	int cnt = 0, hv = p-team[id].miss;
	int ret;

	while(dep>=0)
	{
		if( s[dep][tid] == 1 )
			cnt++;
		dep--;	tid/=2;
	}

	if( cnt>=hv ) return 0;
	else
	{
		ret = hv-cnt;
		cnt = hv;
	}

	dep = p-1;
	tid = team[id].idx/2;
	while(dep>=0)
	{
		if( s[dep][tid] == 0 && dep<=cnt-1)
			s[dep][tid] = 1;
		dep--;	tid/=2;
	}
	return ret;
}

int main()
{
 	freopen("B-small-attempt0.in", "r", stdin);
 	freopen("B-small-attempt0.out", "w", stdout);

	int nCase;
	int i, j, k, tmp;
	scanf("%d", &nCase);
	for(int cc=1; cc<=nCase; cc++)
	{
		scanf("%d", &p);
		n = (1<<p);
		for(i=0; i<n; i++)
		{
			team[i].idx = i;
			scanf("%d", &team[i].miss);
		}

		for(i=p-1; i>=0; i--)
		{
			int maxi = (1<<i);
			for(j=0; j<maxi; j++)
				scanf("%d", &tmp);
		}

		sort(team, team+n);

		for(i=0; i<p; i++)
		{
			for(j=(1<<i)-1; j>=0; j--)
				s[i][j] = 0;
		}

		int ret = 0;
		for(i=0; i<n; i++)
		{
			ret += solve(i);
		}

		printf("Case #%d: %d\n", cc, ret);
	}

	return 0;
}