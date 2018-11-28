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

#define all(s) s.begin(), s.end()

const int INF = 1000000000;

struct s_s
{
	int x, y;
	string row_cur, row_next;
};

bool operator< (const s_s & s1, const s_s & s2)
{
	return s1.x == s2.x ? 
		(s1.y == s2.y ? 
		(s1.row_cur == s2.row_cur ? s1.row_next < s2.row_next : s1.row_cur < s2.row_cur) :
		s1.y < s2.y) : s1.x < s2.x;
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

		string s;
//		getline(cin, s);
//		cin >> s;

		int n, m, f_max;
		cin >> n >> m >> f_max;
		vector<string> mp(n);

		for (int i = 0; i < n ; i++)
		{
			cin >> mp[i];
		}

		map<s_s, int> d;
		queue<s_s> q;

		s_s st;
		st.x = st.y = 0;
		st.row_cur = mp[0];
		st.row_next = mp[1];

		d[st] = 0;

		int best = INF;

		q.push(st);
		while (!q.empty())
		{
			s_s st = q.front();
			q.pop();
			int d_cur = d[st];

			int falled = 0;
			while (st.y < n - 1 && 
				(st.row_next[st.x] == '.'))
				falled++, st.y++, st.row_cur = st.row_next,
				st.row_next = st.y < n - 1 ? mp[st.y + 1] : string(m, '#');

			if (falled > f_max)
				continue;

			if (st.y == n - 1)
			{
				best = min(best, d_cur);
				continue;
			}



			s_s s_new = st;
			if (st.x < m - 1)
			{
				if (st.row_cur[st.x + 1] == '.')
				{
					s_new.x = st.x + 1;
					if (d.find(s_new) == d.end() || d[s_new] > d_cur)
						d[s_new] = d_cur,
						q.push(s_new);


					if (st.y < n - 1)
					{
						s_new = st;
						s_new.row_next[st.x + 1] = '.';
						if (d.find(s_new) == d.end() || d[s_new] > d_cur + 1)
							d[s_new] = d_cur + 1,
							q.push(s_new);
					}
				}


			}

			s_new = st;
			if (st.x > 0)
			{
				if (st.row_cur[st.x - 1] == '.')
				{
					s_new.x = st.x - 1;
					if (d.find(s_new) == d.end() || d[s_new] > d_cur )
						d[s_new] = d_cur,
						q.push(s_new);


					if (st.y < n - 1)
					{
						s_new = st;
						s_new.row_next[st.x - 1] = '.';
						if (d.find(s_new) == d.end() || d[s_new] > d_cur + 1)
							d[s_new] = d_cur + 1,
							q.push(s_new);
					}
				}


			}


		}
		


		printf("Case #%d: ", test + 1);
		if (best == INF)
			printf("No\n");
		else
			printf("Yes %d\n", best);
	}

}