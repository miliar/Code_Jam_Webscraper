#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

int h, w;
vector <bool> was;
vector <vector <int> > alt;
vector <vector <int> > gr;
vector <vector <int> > ans;

int dx[4] = {0, -1, 1, 0};
int dy[4] = {-1, 0, 0, 1};

void BFS(int v)
{
	vector <int> comp;
	was[v] = true;
	queue <int> q;
	q.push(v);
	while(!q.empty())
	{
		int u = q.front();
		q.pop();
		comp.push_back(u);
		for(int i = 0; i < gr[u].size(); i++)
			if(!was[gr[u][i]])
			{
				was[gr[u][i]] = true;
				q.push(gr[u][i]);
			}
	}
	int m = 1e9;
	for(int i = 0; i < comp.size(); i++)
		m = min(m, ans[comp[i] / w][comp[i] % w]);
	for(int i = 0; i < comp.size(); i++)
		ans[comp[i] / w][comp[i] % w] = m;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cin >> h >> w;
		alt.clear();
		alt.assign(h, vector <int> (w));
		ans.clear();
		ans.assign(h, vector <int> (w));
		gr.clear();
		gr.resize(h * w);
		for(int j = 0; j < h; j++)
			for(int k = 0; k < w; k++)
			{
				cin >> alt[j][k];
				ans[j][k] = j * w + k;
			}
		for(int j = 0; j < h; j++)
			for(int k = 0; k < w; k++)
			{
				int dir = -1;
				int m = alt[j][k];
				for(int i = 0; i < 4; i++)
					if(j + dy[i] >= 0 && j + dy[i] < h && k + dx[i] >= 0 && k + dx[i] < w)
						if(alt[j + dy[i]][k + dx[i]] < m)
						{
							dir = i;
							m = alt[j + dy[i]][k + dx[i]];
						}
				if(dir >= 0)
				{
					gr[j * w + k].push_back((j + dy[dir]) * w + k + dx[dir]);
					gr[(j + dy[dir]) * w + k + dx[dir]].push_back(j * w + k);
				}
			}
		
		was.assign(h * w, false);
		for(int j = 0; j < h; j++)
			for(int k = 0; k < w; k++)
				if(!was[j * w + k])
					BFS(j * w + k);
		char curr = 'a';
		map <int, char> b;
		printf("Case #%d:\n", i + 1);
		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)
			{
				char pr;
				if(b.find(ans[i][j]) == b.end())
				{
					pr = curr++;
					b[ans[i][j]] = pr;
				}
				else
					pr = b[ans[i][j]];
				cout << pr << " ";
			}
			cout << endl;
		}
	}
	return 0;
}