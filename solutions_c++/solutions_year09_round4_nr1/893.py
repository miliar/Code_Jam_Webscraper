#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <set>

using namespace std;

typedef vector<int> vint;

bool valid(const vint &perm, const vint &b)
{
	for (int c = 0; c < perm.size(); ++c)
		if (b[ perm[c] ] > c+1) return false;

	return true;
}

set<vint> flag;

int bfs(const vint &b)
{
	const int k = b.size();
	queue<vint> q;

	vint sentinel(k, -1);

	vint id;
	for (int c = 0; c < k; ++c)
		id.push_back(c);

	q.push(id);
	q.push(sentinel);

	int dist = 0;

	while(!q.empty())
	{
		vint st = q.front(); q.pop();

		if (st[0] == -1)
		{
			++dist;
			if (!q.empty()) q.push(sentinel);

			continue;
		}

		if (flag.find(st) != flag.end()) continue;
		flag.insert(st);

		if (valid(st, b)) return dist;

		for (int c = 0; c < k-1; ++c)
		{
			swap( st[c], st[c+1] );
			if (flag.find(st) == flag.end()) q.push(st);
			swap( st[c], st[c+1] );
		}
	}

	throw 1;
	return -1;
}

int main()
{
	int tc;
	cin >> tc;
	for (int casecnt = 1; casecnt <= tc; ++casecnt)
	{
		cout << "Case #" << casecnt << ": ";

		int n;
		cin >> n;

		vint bnd;
		for (int c = 0; c < n; ++c)
		{
			string in;
			cin >> in;
			reverse(in.begin(), in.end());
			in += '1';

			for (int c = 0; c < in.size(); ++c)
				if (in[c] == '1')
				{
					bnd.push_back(n-c);
					break;
				}
		}

		flag.clear();
		cout << bfs(bnd) << endl;
	}

	return 0;
}
