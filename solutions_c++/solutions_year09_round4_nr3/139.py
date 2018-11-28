#include <iostream>
#include <vector>
using namespace std;

const int infty = 10000072;
const int MAXN = 210;
//const int MAXM = 1072;

int capacity[MAXN][MAXN], flow[MAXN][MAXN];
vector<int> edges[MAXN];

int /*n,*/ s, t, tn;
int maxflow;

int layer[MAXN];
vector <int> path;

void getlayer()
{
	vector<int> queue;
	queue.clear();
	int q1 = 0;
	for(int i=0; i<MAXN; i++) layer[i] = -1;
	layer[s] = 0;
	queue.push_back(s);
	while(queue.size() > q1)
	{
		int u = queue[q1];
		for(int i=0; i<edges[u].size(); i++)
		{
			int v = edges[u][i];
			if(layer[v] >=0) continue;
			if(capacity[u][v] - flow[u][v] <= 0) continue;
			layer[v] = layer[u] + 1;
			queue.push_back(v);
			if(v == t) return;
		}
		q1++;
	}
}

void augment(int u)
{
	//cout << u << endl;
	path.push_back(u);
	if(u == t)
	{
		int augflow = infty;
		int bottleneck = path.size()-2;
		//cout << path.size() << endl;
		for(int i=path.size()-2; i>=0; i--)
		{
			//cout << path[i] << " " << path[i+1] << " " << capacity[path[i]][path[i+1]] << endl;
			int segflow = capacity[path[i]][path[i+1]] - flow[path[i]][path[i+1]];
			if(segflow <= augflow)
			{
				augflow = segflow;
				bottleneck = i;
			}
		}
		//cout << "augment " << augflow << " " << bottleneck << endl;
		//system("pause");
		maxflow += augflow;
		for(int i=path.size()-2; i>=0; i--)
		{
			flow[path[i]][path[i+1]] += augflow;
			flow[path[i+1]][path[i]] -= augflow;
			if(i >= bottleneck) path.pop_back();
		}
		return;
	}
	//cout << edges[u].size() << endl;
	for(int i=0; i<edges[u].size(); i++)
	{
		int v = edges[u][i];
		//cout << "v=" << v << endl;
		if(layer[v] == layer[u]+1 && capacity[u][v] > flow[u][v]) augment(v);
		//cout << path.end() << endl;
		//cout << *(path.end()) << endl;
		//cout << *(path.rbegin()) << endl;
		if(*(path.rbegin()) != u) return;
	}
	path.pop_back();
}

void dinic()
{
	maxflow = 0;
	while(true)
	{
		getlayer();
		//cout << "layer done\n";
		//for(int i=0; i<n+2; i++) cout << layer[i] << " ";
		//cout << endl;
		if(layer[t] == -1) return;
		path.clear();
		augment(s);
		//cout << "sol=" << maxflow << endl;
	}
}

void output()
{
	cout << tn - maxflow << endl;
}

void makegraph()
{
	//cin >> m >> n;
	int tk, n;
	cin >> tn >> tk;
	n = tn*2;
	int a[100][100];
	for(int i=0; i<tn; i++)
	{
		for(int j=0; j<tk; j++)
		{
			cin >> a[i][j];
		}
	}
	for(int i=0; i<MAXN; i++)
	{
		edges[i].clear();
		for(int j=0; j<MAXN; j++) capacity[i][j] = flow[i][j] = 0;
	}
	s = 0;
	t = n + 1;
	for(int i=0; i<tn; i++)
	{
		edges[s].push_back(i+i+1);
		edges[i+i+1].push_back(s);
		capacity[s][i+i+1] = 1;
		//capacity[i+i+1][s] = 0;
		edges[i+i+2].push_back(t);
		edges[t].push_back(i+i+2);
		capacity[i+i+2][t] = 1;
		for(int j=0; j<tn; j++) if(j != i)
		{
			int k;
			for(k=0; k<tk; k++) if(a[i][k] >= a[j][k]) break;
			if(k == tk)
			{
				edges[i+i+1].push_back(j+j+2);
				edges[j+j+2].push_back(i+i+1);
				capacity[i+i+1][j+j+2] = 1;
			}
		}
	}
}

int main()
{
	int c, tc;
	cin >> c;
	for(tc = 1; tc <= c; tc ++)
	{
		cout << "Case #" << tc << ": ";
		makegraph();
		//cout << "graph made\n";
		dinic();
		output();
	}
	return 0;
}
