#include<iostream>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;

int INFINITY = 100000*10000;

int p;
vector<int> miss;
vector<int> price;
map<pair<int, int>, int> memo;
int dp(int match, int watched_already)
{
	pair<int, int> idx = make_pair<int,int>(match, watched_already);
	if(memo.find(idx) == memo.end())
	{
		int level = 0;
		int mm = match;
		while(mm > 1)
		{
			++level;
			mm/=2;
		}

		int levels_left = p-level;
		if(levels_left < 0)
		{
			memo[idx] = INFINITY;
			return INFINITY;
		}
		int first_match = (match << levels_left) - (1<<p);
		int final_match = (first_match + (1<<levels_left)) - 1;

		int max_required = 0;
		for(int i=first_match; i<=final_match;++i)
		{
			int needs_to_watch = (p - miss[i]);
			max_required = max(max_required, needs_to_watch - watched_already);
		}
		if(max_required > levels_left)
		{
			memo[idx] = INFINITY;
			return INFINITY;
		}
		if(max_required == 0)
		{
			memo[idx] = 0;
			return 0;
		}
		
		int r1 = price[match] + dp(match*2+1, watched_already+1) + dp(match*2, watched_already+1);
		int r2 = dp(match*2+1, watched_already) + dp(match*2, watched_already);
		memo[idx] = min(r1, r2);
		if(memo[idx] > INFINITY)
			memo[idx] = INFINITY;
	}

	return memo[idx];
}


int main()
{
	freopen("B-large.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);
	FILE * f = fopen("B-large.out","wt");
	int tests;
	scanf("%d", &tests);
	for(int num=1;num<=tests;++num)
	{
		p = 0;
		price.clear();
		price.resize(2048);
		miss.clear();
		memo.clear();
		scanf("%d", &p);
		int a;
		for(int i=0;i<(1<<p);++i)
		{
			scanf("%d", &a);
			miss.push_back(a);
		}
		int lim = 1<<(p-1);
		int tmp;

		while(lim >= 1)
		{
			for(int x=0;x<lim;x++)
				scanf("%d", &price[lim + x]);
			lim = lim/2;
		}
		int buy = 0;
		int res = dp(1,0);

		printf("Case #%d: %d\n", num,  res);
		fprintf(f, "Case #%d: %d\n", num,  res);
	}

	return 0;
}