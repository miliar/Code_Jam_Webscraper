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

int move[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
bool stable(const vector<string> & ve)
{
	vector<string> v(ve);
	int cnt = 0;
	int r = v.size();
	int c = v[0].size();
	for(int i = 0; i < r; i++)
	{
		for(int j = 0; j < c;  j++)
		{
			if(v[i][j] == 'x')
			{
				cnt ++;
				queue<pair<int, int> > toProcess;
				toProcess.push(make_pair(i, j));
				v[i][j] = '.';
				pair<int, int> cur;
				while(!toProcess.empty())
				{
					cur = toProcess.front();
					toProcess.pop();
					for(int k = 0; k < 4; k++)
					{
						if(v[cur.first + move[k][0]][cur.second + move[k][1]] == 'x')
						{
							v[cur.first + move[k][0]][cur.second + move[k][1]] = '.';
							toProcess.push(make_pair(cur.first + move[k][0], cur.second + move[k][1]));
						}
					}
				}
			}
		}
		
	}
	return cnt < 2;
}
vector<vector<string> > neighboursF(const vector<string> &ve)
{
	vector<string> v(ve);
	int r = v.size();
	int c = v[0].size();
	vector<vector<string> > res;
	for(int i = 0; i < r; i++)
	{
		for(int j = 0; j < c; j++)
		{
			if(v[i][j] == 'x')
			{
				for(int k = 0; k < 2; k++)
				{
					if(v[i + move[k * 2][0]][j + move[k * 2][1]] == '.' && v[i + move[k * 2 + 1][0]][j + move[k * 2 + 1][1]] == '.')
					{
						swap(v[i][j], v[i + move[k * 2][0]][j + move[k * 2][1]]);
						res.push_back(v);
						swap(v[i][j], v[i + move[k * 2][0]][j + move[k * 2][1]]);
						swap(v[i][j], v[i + move[k * 2 + 1][0]][j + move[k * 2 + 1][1]]);
						res.push_back(v);
						swap(v[i][j], v[i + move[k * 2 + 1][0]][j + move[k * 2 + 1][1]]);
					}
				}
			}
		}
	}
	return res;
}
int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		map<vector<string>, int > visited;
		int r, c;
		cin >> r >> c;
		vector<string> v(r + 2);
		string str;
		str.resize(c + 2, '#');
		v[0] = v[r + 1] = str;
		for(int i = 0; i < r; i++)
		{
			cin >> v[i + 1];
			v[i + 1] = "#" + v[i + 1] + "#";
		}
		c += 2;
		r += 2;
		vector<string> initial(r);
		vector<string> end(r);
		for(int i = 0; i < r; i++)
		{
			initial[i].resize(c);
			end[i].resize(c);
			for(int j = 0; j < c; j++)
			{
				if(v[i][j] == 'o' || v[i][j] == 'w')
					initial[i][j] = 'x';
				else if(v[i][j] == 'x')
					initial[i][j] = '.';
				else 
					initial[i][j] = v[i][j];
			}
			for(int j = 0; j < c; j++)
			{
				if(v[i][j] == 'x' || v[i][j] == 'w')
					end[i][j] = 'x';
				else if(v[i][j] == 'o')
					end[i][j] = '.';
				else 
					end[i][j] = v[i][j];
			}
		}
		queue<vector<string> > toProcess;
		visited[initial] = 0;
		toProcess.push(initial);
		vector<string> cur;
		int level;
		bool isStable;
		while(!toProcess.empty() && visited.find(end) == visited.end())
		{
			cur = toProcess.front();
			toProcess.pop();
			level = visited[cur];
			isStable = stable(cur);
			vector<vector<string> > neighbours = neighboursF(cur);
			for(int i = 0; i < neighbours.size(); i++)
			{
				if(stable(neighbours[i]))
				{
					if(visited.find(neighbours[i]) == visited.end())
					{
						visited[neighbours[i]] = level + 1;
						toProcess.push(neighbours[i]);
					}
				}
				else if(isStable)
				{
					if(visited.find(neighbours[i]) == visited.end())
					{
						visited[neighbours[i]] = level + 1;
						toProcess.push(neighbours[i]);
					}
				}
			}
		}
		if(visited.find(end) == visited.end())
			cout << -1 << endl;
		else
			cout << visited[end] << endl;
	}
	return 0;
}
