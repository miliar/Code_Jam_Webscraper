#define  _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<time.h>
#include<numeric>
#include<set>
#include<stack>
#include<deque>
#include<math.h>
#define epsilon 0.000000001
using namespace std;
vector<vector<pair<int, int> > > fathers;
vector<vector<int> > val;
void joinComponents(int i1, int j1, int i2, int j2)
{
	vector<pair<int, int> > toSet;
	int t;
	while(fathers[i1][j1].first != -1)
	{
		toSet.push_back(make_pair(i1, j1));
		t = i1;
		i1 = fathers[i1][j1].first;
		j1 = fathers[t][j1].second;
	}
	while(fathers[i2][j2].first != -1)
	{
		toSet.push_back(make_pair(i2, j2));
		t = i2;
		i2 = fathers[i2][j2].first;
		j2 = fathers[t][j2].second;
	}
	int bestx, besty;
	if(val[i1][j1] > val[i2][j2])
	{
		fathers[i2][j2] = make_pair(i1, j1);
		besty = j1;
		bestx = i1;
	}
	else
	{
		fathers[i1][j1] = make_pair(i2, j2);
		besty = j2;
		bestx = i2;
	}
	pair<int, int> best(bestx, besty);
	for(int i = 0; i < toSet.size(); i++)
	{
		fathers[toSet[i].first][toSet[i].second] = best;
	}
}
pair<int, int> father(int i, int j)
{
	vector<pair<int, int> > toSet;
	int t;
	while(fathers[i][j].first != -1)
	{
		toSet.push_back(make_pair(i, j));
		t = i;
		i = fathers[i][j].first;
		j = fathers[t][j].second;
	}
	pair<int, int> best(i, j);
	for(int i = 0; i < toSet.size(); i++)
	{
		fathers[toSet[i].first][toSet[i].second] = best;
	}
	return best;
}

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numtests;
	cin >> numtests;
	for(int o = 0; o < numtests; o++)
	{
		printf("Case #%d:\n", o + 1);
		int n, m;
		cin >> n >> m;
		vector<vector<int> > v(n);
		fathers.clear();
		val.clear();
		fathers.resize(n);
		val.resize(n);
		for(int i = 0; i < n; i++)
		{
			v[i].resize(m);
			fathers[i].resize(m, make_pair(-1, -1));
			val[i].resize(m, 1);
		}
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m ;j++)
				cin >> v[i][j];
		int mat[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				int minm = v[i][j];
				int idx = -1;
				for(int k = 0; k < 4; k++)
				{
					if(i + mat[k][0] >= 0 && i + mat[k][0] < n && j + mat[k][1] >= 0 && j + mat[k][1] < m)
					{
						if(minm > v[i + mat[k][0]][j + mat[k][1]])
						{
							minm = v[i + mat[k][0]][j + mat[k][1]];
							idx = k;
						}
					}
				}
				if(idx != -1)
				{
					joinComponents(i, j, i + mat[idx][0], j + mat[idx][1]);
				}
			}
		}
		map<pair<int, int>, char> ma;
		map<pair<int, int>, char>::iterator itr;
		char a = 'a';
		vector<vector<char> > toPrint(n);
		for(int i = 0; i < n; i++)
			toPrint[i].resize(m);
		pair<int, int> p;
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				p = father(i, j);
				if((itr = ma.find(p)) == ma.end())
				{
					ma[p] = a;
					toPrint[i][j] = a++;
				}
				else
					toPrint[i][j] = itr->second;
				if(j == 0)
				{
					cout << toPrint[i][j];
				}
				else
					cout << " " << toPrint[i][j];
			}
			cout << endl;
		}

	}
	return 0;
}
