#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);

		int n, m;
		cin >> n >> m;
		vector<vector<int> > components(1);
		vector<bool> real(1, true);
		components[0].resize(n);
		for(int i = 0; i < n; i++)
			components[0][i] = i;

		vector<set<int> > vertices(n);
		set<int>::iterator itr;
		for(int i = 0; i < n; i++)
		{
			vertices[i].insert(0);
		}
		int x, y;
		int common;
		int cnte;
		int cmpIdx = 1;
		vector<int> xs(m);
		vector<int> ys(m);
		for(int i = 0; i < m; i++)
		{
			cin >> xs[i];
		}
		for(int i = 0; i < m; i++)
		{
			cin >> ys[i];
		}
		for(int i = 0; i < m; i++)
		{
			x = xs[i] - 1;
			y = ys[i] - 1;
			for(itr = vertices[x].begin(); itr != vertices[x].end(); ++itr)
			{
				if(vertices[y].find(*itr) != vertices[y].end())
				{
					common = *itr;
					break;
				}
			}
			vector<int> left, right;
			cnte = 0;
			for(int j = 0; j < components[common].size(); j++)
			{
				vertices[components[common][j]].erase(common);
				if(components[common][j] == x || components[common][j] == y)
				{
					cnte++;
					vertices[components[common][j]].insert(cmpIdx);
					left.push_back(components[common][j]);
					vertices[components[common][j]].insert(cmpIdx + 1);
					right.push_back(components[common][j]);
				} 
				else if(cnte % 2 == 0)
				{
					vertices[components[common][j]].insert(cmpIdx);
					left.push_back(components[common][j]);
				}
				else
				{
					vertices[components[common][j]].insert(cmpIdx + 1);
					right.push_back(components[common][j]);
				}
			}
			cmpIdx += 2;
			real[common] = false;
			real.push_back(true);
			real.push_back(true);
			components.push_back(left);

			components.push_back(right);
		}

		int minm = 1000000;
		vector<vector<int> > comps;
		vector<vector<int> > vert(n);
		vector<int> maps(components.size(), -1);
		for(int i = 0; i < components.size(); i++)
		{
			if(real[i])
			{
				maps[i] = comps.size();
				comps.push_back(components[i]);
				minm = min(minm, (int)components[i].size());
			}
		}
		for(int i = 0; i < n; i++)
		{
			for(itr = vertices[i].begin(); itr != vertices[i].end(); ++itr)
			{
				vert[i].push_back(maps[*itr]);
			}
		}
		vertices.clear();
		components.clear();
		vector<int> cnt(comps.size(), 0);
		vector<int> first(comps.size(), -1);
		vector<int> second(comps.size(), -1);
		vector<bool> vis(comps.size(), false);
		vector<int> color(n, -1);
		queue<int> toProcess;
		toProcess.push(0);
		first[0] = comps[0][0];
		color[comps[0][0]] = 0;
		second[0] = comps[0][1];
		color[comps[0][1]] = 1;
		vis[0] = true;
		for(int j = 0; j < vert[first[0]].size(); j++)
		{
			if(vis[vert[first[0]][j]])
				continue;
			if(cnt[vert[first[0]][j]] == 0)
			{
				cnt[vert[first[0]][j]] = 1;
				first[vert[first[0]][j]] = first[0];
			} else if(cnt[vert[first[0]][j]] == 1)
			{
				cnt[vert[first[0]][j]] = 2;
				second[vert[first[0]][j]] = first[0];
				vis[vert[first[0]][j]] = true;
				toProcess.push(vert[first[0]][j]);
			}
		}
		for(int j = 0; j < vert[second[0]].size(); j++)
		{
			if(vis[vert[second[0]][j]])
				continue;
			if(cnt[vert[second[0]][j]] == 0)
			{
				cnt[vert[second[0]][j]] = 1;
				first[vert[second[0]][j]] = second[0];
			} else if(cnt[vert[second[0]][j]] == 1)
			{
				cnt[vert[second[0]][j]] = 2;
				second[vert[second[0]][j]] = second[0];
				vis[vert[second[0]][j]] = true;
				toProcess.push(vert[second[0]][j]);
			}
		}
		
		int cur = 0; 
		int idx;
		bool placed = false;
		int other;
		while(!toProcess.empty())
		{
			cur = toProcess.front();
			if(first[cur] > second[cur])
				swap(first[cur], second[cur]);
			if(first[cur] == comps[cur][0] && second[cur] == comps[cur][comps[cur].size() - 1])
				swap(first[cur], second[cur]);
			toProcess.pop();
			placed = false;
			idx = 0;
			while(idx == color[first[cur]] || idx == color[second[cur]])
				idx = (idx + 1) % minm;
			other = idx;
			for(int i = 0; i < comps[cur].size(); i++)
			{
				if(color[comps[cur][i]] != -1)
					continue;
				color[comps[cur][i]] = idx;
				for(int j = 0; j < vert[comps[cur][i]].size(); j++)
				{
					if(vis[vert[comps[cur][i]][j]])
						continue;
					if(cnt[vert[comps[cur][i]][j]] == 0)
					{
						cnt[vert[comps[cur][i]][j]] = 1;
						first[vert[comps[cur][i]][j]] = comps[cur][i];
					} else if(cnt[vert[comps[cur][i]][j]] == 1)
					{
						cnt[vert[comps[cur][i]][j]] = 2;
						second[vert[comps[cur][i]][j]] = comps[cur][i];
						vis[vert[comps[cur][i]][j]] = true;
						toProcess.push(vert[comps[cur][i]][j]);
					}
					else
					{
						throw "BIG problem!";
					}
				}
				if(placed)
					second[cur] = comps[cur][i];
				if(idx == minm - 1)
				{
					placed = true;
					second[cur] = comps[cur][i];
				}
				idx = (idx + 1) % minm;
				while(idx == color[first[cur]] || idx == color[second[cur]])
				{
					if(idx == minm - 1)
					{
						placed = true;
						second[cur] = comps[cur][i];
					}
					idx = (idx + 1) % minm;
				}
			}
		}

		printf("%d\n", minm);
		printf("%d", color[0] + 1);
		for(int i = 1; i < n; i++)
			printf(" %d", color[i] + 1);
		printf("\n");

	}
	return 0;
}
