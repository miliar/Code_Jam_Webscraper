#include <iostream>
#include <vector>
#include <fstream>

using namespace std;
vector<vector<int> > edges;
vector<int> passed;

vector<int> order;

int now = -1;
bool dfs(int i)
{
	bool flag = false;
	for(int j=0;j<edges[i].size();j++)
	{
		if(passed[edges[i][j]] == now)
			return true;
		else
		{
			passed[edges[i][j]] = now;
			flag = flag || dfs(edges[i][j]);
		}
	}
	return flag;
}

int main()
{
	ifstream cin("x.in");
	ofstream cout("x.out");
	int t,m;
	cin >>t;
	char* res;
	for(int i=1;i<=t;i++)
	{
		order.clear();
		passed.clear();
		edges.clear();
		int n;
		cin >> n;
		passed.resize(n,-1);
		edges.resize(n);
		for(int i=0;i<edges.size();i++)
		{
			cin >> n;
			edges[i].resize(n);
			for(int j=0;j<edges[i].size();j++)
			{
				cin >> edges[i][j];
				edges[i][j] --;
			}
		}
		bool flag = false;
		for(int i=0;i<edges.size();i++)
		{
			now = i;
			flag = flag || dfs(i);
		}
		cout << "Case #" << i << ": " << (flag?"Yes":"No") << "\n";
		//printf("Case %d: %s\n",i,flag?"Yes":"No");
	}
	return 0;
}