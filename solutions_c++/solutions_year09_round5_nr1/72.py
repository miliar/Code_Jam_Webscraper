#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"
#include <cmath>
#include <cassert>
#include "iostream"
#include "sstream"
#include "string"
#include "algorithm"
#include "vector"
#include "queue"
#include "map"

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;

#define all(s) s.begin(), s.end()

const int INF = 1000000000;

typedef pair<vi, bool> s_s;

int n, m, c;

int dx[] = {1, 0, -1, 0};
int dy[] = {0, -1, 0, 1};

int used[5];

int mymod = (1 << 6) - 1;

int rec (vi & a, int cur)
{
	int res = 1;
	used[cur] = 1;

	int y = a[cur] >> 6;
	int x = a[cur] & mymod;

	for (int i = 0; i < 4 ; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];

		vi::iterator it = find(all(a), (ny << 6) + nx);
		if (it != a.end())
			if (!used[it - a.begin()])
				res += rec(a, it - a.begin());
	}

	return res;
}

bool stable (vi & a)
{
	memset(used, 0, sizeof used);

	return (rec(a, 0) == c);
}

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);


	int test_count;
	cin >> test_count;


	for (int test = 0; test < test_count ; test++)
	{
		fprintf(stderr, "%d\n", test);

		vector<string> mp;

		s_s start;
		start.second = true; // stable

		vi goal;

		cin >> n >> m;
		c = 0;
		mp.push_back(string(m + 2, '#'));
		for (int i = 0; i < n ; i++)
		{
			string s;
			cin >> s;
			s = '#' + s + '#';
			mp.push_back(s);

			for (int j = 0; j < m + 2 ; j++)
			{
				if (s[j] == 'o' || s[j] == 'w')
				{
					start.first.push_back(((i + 1) << 6) + j);
					++c;
				}
				if (s[j] == 'x' || s[j] == 'w')
				{
					goal.push_back(((i + 1) << 6) + j);
				}
			}
		}
		mp.push_back(string(m + 2, '#'));

		sort(all(goal));
		sort(all(start.first));

		map<vi, int> d[2];
		int best = INF;

		d[0][start.first] = 0;

		queue<s_s> q;
		q.push(start);
		while (!q.empty())
		{
			s_s cur = q.front();
			q.pop();

			int cur_d = d[cur.second][cur.first];

			if (goal == cur.first)
			{
				best = min(best, cur_d);
				continue;
			}

			for (int i = 0; i < c ; i++)
			{
				int y = cur.first[i] >> 6;
				int x = cur.first[i] & mymod;

				for (int j = 0; j < 4 ; j++)
				{
					int nx = x + dx[j];
					int ny = y + dy[j];


					int nx_ = x + dx[(j + 2) & 3];
					int ny_ = y + dy[(j + 2) & 3];


					if (mp[ny][nx] != '#' && mp[ny_][nx_] != '#' && 
						find(all(cur.first), (ny_ << 6) + nx_) == cur.first.end() && 
						find(all(cur.first), (ny << 6) + nx) == cur.first.end())
					{
						vi n_s = cur.first;
						n_s[i] = (ny << 6) + nx;

						bool is_stable;

						is_stable = stable(n_s);
						if (!cur.second && !is_stable)
							continue;

						sort(all(n_s));

						if (d[is_stable].find(n_s) == d[is_stable].end() || 
							d[is_stable][n_s] > cur_d + 1)
						{
							d[is_stable][n_s] = cur_d + 1;
							q.push(make_pair(n_s, is_stable));
						}
					}

				}
			}
		}


		printf("Case #%d: %d\n", test + 1, best == INF ? -1 : best);


		/*
		printf("Case #%d: ", test + 1);
		int res = d[en.first][en.second];
		if (res == INF)
		printf("THE CAKE IS A LIE\n");
		else
		printf("%d\n", res);
		*/



	}

}
