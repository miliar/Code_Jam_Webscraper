//replace all commas to spaces
#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

vector < vector<int> > graph;
vector < vector<int> > graph1, graph1T;
vector<int> match;
vector<char> used;

bool try_kuhn (int v) 
{
	if (used[v]) 
		return false;
	used[v] = true;
	for (int i=0; i< (int)graph[v].size(); ++i) 
	{
		int to = graph[v][i];
		if (match[to] == -1 || try_kuhn (match[to])) 
		{
			match[to] = v;
			return true;
		}
	}
	return false;
}
int n,m;
int vIndex(int i, int j, bool second)
{
	if (i < 0)
		i += n;
	if (j < 0)
		j += m;
	if (i >= n)
		i -= n;
	if (j >= m)
		j -= m;
	return i * m + j + (second ? n*m : 0);
}
bool run_kuhn()
{
	int mv = vIndex(n-1,m-1,false);
	match = vector<int>(graph.size(), -1);
	for (int v = 0; v <= mv; ++v) 
	{
		used = vector<char>(graph.size(), 0);
		if (!try_kuhn(v))
			return false;
	}
	return true;
}

char buf[1000][1000];

vector<int> order, component;
 
void DFS1 (int v)
{
	if (used[v])
		return;
	used[v] = true;
	for (int i=0; i<(int)graph1[v].size(); ++i)
		DFS1(graph1[v][i]);
	order.push_back (v);
}
 
void DFS2 (int v, int base) 
{
	if (used[v])
		return;
	used[v] = true;
	component.push_back(v);
	for (int i=0; i<(int)graph1T[v].size(); ++i)
		DFS2 (graph1T[v][i], base);
}
__int64 getResult(int n)
{
	__int64 res = 1;
	for (int i=1;i<=n;i++)
	{
		res = res * 2;
		res %= 1000003;
	}
	return res;
}

__int64 build()
{
	graph = vector<vector<int> > (vIndex(n-1,m-1,true) + 1);
	for (int i=0;i<n;i++)
		for (int j=0;j<m;j++)
		{
			char c = buf[i][j];
			int v = vIndex(i, j, false);
			switch(c)
			{
				case '|':
					graph[v].push_back(vIndex(i-1,j,true));
					graph[v].push_back(vIndex(i+1,j,true));
					break;
				case '-':
					graph[v].push_back(vIndex(i,j-1,true));
					graph[v].push_back(vIndex(i,j+1,true));
					break;
				case '/':
					graph[v].push_back(vIndex(i+1,j-1,true));
					graph[v].push_back(vIndex(i-1,j+1,true));
					break;
				case '\\':
					graph[v].push_back(vIndex(i-1,j-1,true));
					graph[v].push_back(vIndex(i+1,j+1,true));
					break;
			}
		}

	if (!run_kuhn())
		return 0;

	graph1 = vector<vector<int> > (vIndex(n-1,m-1,true) + 1);
	graph1T = vector<vector<int> > (vIndex(n-1,m-1,true) + 1);
	
	for (int i=0;i<=vIndex(n-1,m-1,false);i++)
	{
		for (int j=0;j<(int)graph[i].size();j++)
		{
			int to = graph[i][j];
			if (match[to] == i)
			{
				graph1[to].push_back(i);
				graph1T[i].push_back(to);
			}
			else
			{
				graph1[i].push_back(to);
				graph1T[to].push_back(i);
			}
		}
//		graph1[i].push_back(vIndex(n-1,m-1,true) + 1);
//		graph1T[vIndex(n-1,m-1,true) + 1].push_back(i);
	}
	for (int i=vIndex(0,0,true);i<=vIndex(n-1,m-1,true);i++)
	{
//		graph1T[i].push_back(vIndex(n-1,m-1,true) + 2);
//		graph1[vIndex(n-1,m-1,true) + 2].push_back(i);
	}


	used = vector<char>(graph1.size(), 0);
	order.clear();
	for (int i=0; i<(int)graph1.size(); ++i)
		DFS1(i);

	used = vector<char>(graph1.size(), 0);
	int ccnt = 0;
	for (int i=0; i<(int)graph1.size(); ++i) 
	{
		int v = order[(int)graph1.size()-i-1];
		if (!used[v]) 
		{
			DFS2 (v, v);
			if (component.size() > 1)
				++ccnt;
			component.clear();
		}
	}
	return getResult(ccnt);
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
		cout<<"Case #"<<aaa + 1<<": ";
		cin>>n>>m;
		for (int i=0;i<n;i++)
			cin>>buf[i];
		cout<<build();
		cout<<endl;
	}
	
}