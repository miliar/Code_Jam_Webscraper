#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int N;
vector<int> G[1001];
vector<int> roots;
int rootOf[1001];

void solve(istream& input, ostream& output)
{
	roots.clear();
	for (auto& v : G)
		v.clear();

	input >> N;
	for (int i = 1; i <= N; ++i)
	{
		int m;
		input >> m;
		if (m == 0)
		{
			roots.push_back(i);
			continue;
		}
		for (int j = 0; j < m; ++j)
		{
			int a;
			input >> a;
			G[a].push_back(i);
		}
	}
	
	fill_n(rootOf, N + 1, 0);
	for (int r : roots)
	{
		rootOf[r] = r;
		queue<int> q;
		q.push(r);
		while (!q.empty())
		{
			int u = q.front();
			q.pop();

			for (int v : G[u])
			{
				if (rootOf[v] == r)
				{
					output << "Yes";
					return;
				}
				rootOf[v] = r;
				q.push(v);
			}
		}
	}
	output << "No";
}

int main()
{
	int t;
	ifstream fin("A-large.in");
	fin >> t;

	ofstream cout("output.txt");
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve(fin, cout);
		cout << "\n";
	}
}