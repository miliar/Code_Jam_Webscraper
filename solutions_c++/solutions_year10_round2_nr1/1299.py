#include <cstdio>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

const int maxn = 100000;

int next[maxn][37];
bool leaf[maxn];
int nextv;

vector< int > leafs;

void flush()
{
	for (int i = 0; i < maxn; i++)
	{
		for (int j = 0; j < 37; j++) next[i][j] = -1;
		leaf[i] == false;
	}
	nextv = 1;
}

int lett(char c)
{
	if (c == '/') return 27;
	else if ((c <= 'z') && (c >= 'a')) return (int) c-'a';
	else return c-'0'+28;
}

int add(string s)
{
	int res = 0, v = 0, i = 0;
	while (true)
	{
		if ((i < s.length()) && (next[v][lett(s[i])] != -1))
		{
			v = next[v][lett(s[i])];
			i++;
		}
		else break;
	}

	if (i == s.length())
	{
		cerr << "exist " << v << ' ' << leaf[v] << ' ' << next[v][lett('/')] << endl;
		if (leaf[v] || (next[v][lett('/')] != -1)) return 0;
		else return 1;
	}
	if (s[i] != '/') res++;

	while (i < s.length())
	{
		next[v][lett(s[i])] = nextv;
		cerr << "add " << s[i] << ": " << v << " -> " << nextv << endl;
		v = nextv++;
		if (s[i] == '/') res++;
		i++;
	}
	leaf[v] = true;
	leafs.push_back(v);
	cerr << "marked " << v << " as leaf" << endl;

	return res;
}

int main()
{
	freopen ("a.in", "rt", stdin);
	freopen ("a.out", "wt", stdout);
	freopen ("a.err", "wt", stderr);

	int t;
	string s;
	scanf ("%d", &t);

	int r, n, m, cr;
	for (int i = 1; i <= t; i++)
	{
		cerr << endl << "test " << i << endl;
		leafs.resize(0);
		flush();
		r = 0;
		scanf ("%d%d", &n, &m);
		for (int j = 0; j < n; j++)
		{
			cin >> s;
			add(s);
		}
		for (int j = 0; j < m; j++)
		{
			cin >> s;
			cr = add(s);
			r += cr;
			cerr << "added " << s << " with cost " << cr << endl;
		}
		for (int j = 0; j < leafs.size(); j++)
		{
			leaf[leafs[j]] = false;
			cerr << "unmarked " << leaf[leafs[j]] << " as leaf" << endl;
		}
		printf ("Case #%d: %d\n", i, r);
	}
	return 0;
}