//replace all commas to spaces
#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

void bfs(vector<vector<int> > &graph, int from, vector<int> &dist)
{
	dist = vector<int>(graph.size(), 1000000000);
	vector<int> q;
	q.push_back(from);
	dist[from] = 0;
	int ndx = 0;
	while (ndx < (int)q.size())
	{
		int f = q[ndx];
		++ndx;
		for (int i = 0;i<(int)graph[f].size();i++)
		{
			int t = graph[f][i];
			if (dist[t] > dist[f] + 1)
			{
				dist[t] = dist[f] + 1;
				q.push_back(t);
			}
		}
	}
}

vector<pair<int, int> > edges;
vector<vector<int> > graph;
vector<vector<int> > isNeib;
vector<vector<int> > isNeibC;

int ans[5000][1000];
int ansM[5000][1000];

int getEdge(int f, int t)
{
	return lower_bound(edges.begin(),edges.end(), make_pair(f,t)) - edges.begin();
}

int runFind(int e, int v)
{
	if (isNeib[v][1])
		return ansM[e][v];
	if (ans[e][v] != -1)
		return ans[e][v];
	int opt = 0;
	for (int i = 0; i < (int)graph.size();i++)
		if (isNeibC[v][i])
		{
			int en = getEdge(edges[e].second, v);
			if (edges[en].first != edges[e].second || edges[en].second != v)
				throw 0;

			int test = runFind(en, i);
			opt = max(opt, test);
		}
	return ans[e][v] = opt + ansM[e][v];
}

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int taa;
	cin>>taa;
	cout.setf(ios_base::fixed);
	cout.precision(20);
	for (int aaa = 0; aaa < taa; aaa++)
	{
		int n,m;
		cin>>n>>m;
		graph = vector<vector<int> > (n+2);
		int vstart = n + 1;
		int vend = 1;
		graph[vstart].push_back(vstart - 1);
		graph[vstart - 1].push_back(vstart);
		graph[vstart - 1].push_back(0);
		graph[0].push_back(vstart - 1);

		for (int i=0;i<m;i++)
		{
			int f = -2,t = -2;
			cin>>f>>t;
			graph[f].push_back(t);
			graph[t].push_back(f);
		}

		isNeib = vector<vector<int> > (graph.size(), vector<int> (graph.size()));
		for (int i=0;i<(int)graph.size();i++)
			for (int j=0;j<(int)graph[i].size();j++)
				isNeib[i][graph[i][j]] = 1;

		vector<int> distF, distT;
		bfs(graph, vstart, distF);
		bfs(graph, vend, distT);
		int d = distF[vend];

		for (int i=0;i<(int)graph.size();i++)
			for (int j=0;j<(int)graph[i].size();j++)
			{
				int f = i;
				int t = graph[i][j];
				if (distF[f] + 1 + distT[t] != d)
				{
					graph[i].erase(graph[i].begin() + j);
					--j;
				}
			}

		edges.clear();
		for (int i=0;i<(int)graph.size();i++)
			for (int j=0;j<(int)graph[i].size();j++)
				edges.push_back(make_pair(i, graph[i][j]));

		sort(edges.begin(), edges.end());


		isNeibC = vector<vector<int> > (graph.size(), vector<int> (graph.size()));
		for (int i=0;i<(int)graph.size();i++)
			for (int j=0;j<(int)graph[i].size();j++)
				isNeibC[i][graph[i][j]] = 1;

		memset(ans, -1, sizeof(ans));
		memset(ansM, 0, sizeof(ansM));

		for (int i=0;i<(int)edges.size();i++)
			for (int j=0;j<(int)graph.size();j++)
			{
				int a = edges[i].first;
				int b = edges[i].second;
				int c = j;
				int res = 0;
				for (int k = 0; k < (int)graph.size();k ++)
					if (isNeib[c][k] && !isNeib[b][k] && !isNeib[a][k] && a != k && b != k)
						++res;
				ansM[i][j] = res;
			}

		cout<<"Case #"<<aaa + 1<<": ";
		cout<<d - 3;
		cout<<' '<<runFind((int)edges.size() - 1, 0) - (d - 3);
		cout<<endl;
	}
	
}