#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;

int bfs(vector<string> &v)
{
	map< vector<string>, int > m;
	queue<vector<string> > q;
	q.push(v);
	m[v] = 0;
	while(!q.empty())
	{
		vector<string> t = q.front(); q.pop();
		int dist = m[t];
		bool b = 1;
		for(int i = 0; i < t.size(); i ++)
			for(int j = i + 1; j < t.size(); j ++)
				if( t[i][j] == '1' )
				{
					b = 0;
					goto out;
				}
		return dist;
		out:;
		for(int i = 0; i + 1 < t.size(); i ++)
		{
			swap(t[i], t[i + 1]);
			if(!m.count(t))
			{
				q.push(t);
				m[t] = dist + 1;
			}
			swap(t[i], t[i + 1]);
		}
	}
}

int T;
int main()
{
	cin >> T;
	for(int t = 0; t < T; t ++)
	{
		int N;
		cin >> N;
		vector<string> v(N);
		for(int i = 0; i < N; i ++)
			cin >> v[i];
		printf("Case #%d: %d\n", t + 1, bfs(v));
	}
    return 0;
}
