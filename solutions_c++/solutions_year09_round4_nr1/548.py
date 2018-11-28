#include <cstdio>
#include <vector>
#include <map>
#include <utility>
#include <queue>

using namespace std;

vector<int> c;
map<vector<int>, int> state;

bool iscompleted(const vector<int>& inp)
{
	for(int i = 0; i < inp.size(); ++i)
	{
		if (inp[i] > i)
			return false;
	}
	return true;
}

int solve()
{
	int ret = -1;
	queue<vector<int> > q;
	q.push(c);

	state[c] = 0;

	while(!q.empty())
	{
		vector<int> cur = q.front();
		q.pop();

		int len = state[cur];
		if ((ret == -1 || len < ret) && iscompleted(cur))
		{
			ret = len;
		}

		for(int i = 1; i < c.size(); ++i)
		{
			swap(cur[i-1], cur[i]);
			map<vector<int>, int>::iterator it = state.find(cur);
			if (it == state.end() || it->second > len + 1)
			{
				state[cur] = len + 1;
				q.push(cur);
			}
			swap(cur[i-1], cur[i]);
		}
	}
	return ret;
}

int main()
{
	int z;
	scanf("%d", &z);
	for(int i = 1; i <= z; ++i)
	{
		int n;
		scanf("%d", &n);
		char inp[1024] = {0};
		c.clear();
		state.clear();
		for(int j = 0; j < n; ++j)
		{
			scanf("%s", &inp);
			c.push_back(0);
			for(int k = 0; inp[k] != 0; ++k)
			{
				if (inp[k] == '1')
					c[j] = k;
			}
		}
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}