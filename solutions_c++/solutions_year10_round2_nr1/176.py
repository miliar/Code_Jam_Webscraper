#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

struct Edge
{
	string name;
	vector<Edge*> son;
} e[1000000], *root;
int e_cnt;

Edge* newNode(const string &s)
{
	e[e_cnt].name = s;
	e[e_cnt].son.clear();
	return &e[e_cnt++];
}

int addDir(const vector<string> &vs)
{
	int ret = 0;
	Edge *r = root;
	for (int i = 0; i < vs.size(); i++)
	{
		bool has = false;
		for (int j = 0; j < r->son.size(); j++)
		{
			if (r->son[j]->name == vs[i])
			{
				has = true;
				r = r->son[j];
			}
		}
		if (has == false)
		{
			Edge *t = newNode(vs[i]);
			ret++;
			r->son.push_back(t);
			r = t;
		}
	}
	return ret;
}

int main()
{
	freopen("f:\\A-small-attempt0.in", "r", stdin);
	freopen("f:\\A-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		e_cnt = 0;
		root = newNode("");
		int N, M;
		scanf("%d %d", &N, &M);
		int res = 0;
		for (int i = 0; i < N; i++)
		{
			string s, token;
			cin >> s;
			for (int i = 0; i < s.size(); i++)
				if (s[i] == '/') s[i] = ' ';
			istringstream is(s);
			vector<string> vs;
			while (is >> token)
			{
				vs.push_back(token);
				addDir(vs);
			}
		}
		for (int i = 0; i < M; i++)
		{
			string s, token;
			cin >> s;
			for (int i = 0; i < s.size(); i++)
				if (s[i] == '/') s[i] = ' ';
			istringstream is(s);
			vector<string> vs;
			while (is >> token)
			{
				vs.push_back(token);
				res += addDir(vs);
			}
		}
		printf("Case #%d: %d\n", t_case, res);
	}
	return 0;
}
