#include <iostream>
#include <vector>
using namespace std;

const __int64 MAX = 105;

struct G
{
	__int64 cnt, type;
	G() {}
	G(__int64 _cnt, __int64 _type) : cnt(_cnt), type(_type) {}
};

__int64 n, m, ans;

vector<G> ga, gb;

void dfs(__int64 x, __int64 y, __int64 all)
{
	if(x >= ga.size() || y >= gb.size())
	{
		ans = max(ans, all);
		return;
	}

	__int64 c = 0;
	if(ga[x].type == gb[y].type)
	{
		c = min(ga[x].cnt, gb[y].cnt);
	}

	ga[x].cnt -= c;
	gb[y].cnt -= c;
	all += c;

	dfs(x, y + 1, all);
	dfs(x + 1, y, all);

	ga[x].cnt += c;
	gb[y].cnt += c;
	all -= c;
}

__int64 go()
{
	ans = 0;
	dfs(0, 0, 0);
	return ans;
}

void main()
{
	freopen("C:\\Users\\Administrator\\Desktop\\GCJ\\C-small-attempt0.in", "r", stdin);
	freopen("C:\\Users\\Administrator\\Desktop\\GCJ\\C-small-attempt0.out", "w", stdout);

	__int64 T, c = 0;
	scanf("%I64d", &T);
	//T = 100;

	while(T--)
	{
		ga.clear();
		gb.clear();

		scanf("%I64d%I64d", &n, &m);
		//n = 3;
		///m = 100;

		for(__int64 i = 0; i < n; i++)
		{
			__int64 cnt, type;
			//cnt = type = 0;
			scanf("%I64d%I64d", &cnt, &type);
			ga.push_back(G(cnt, type));
		}
		for(__int64 i = 0; i < m; i++)
		{
			__int64 cnt, type;
			//cnt = type = 0;
			scanf("%I64d%I64d", &cnt, &type);
			gb.push_back(G(cnt, type));
		}

		printf("Case #%I64d: %I64d\n", ++c, go());
	}

	//system("pause");
}