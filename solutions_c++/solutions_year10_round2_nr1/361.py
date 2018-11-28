#define  _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <string>
#include <set>
#include <sstream>
#include <map>

#define sz(x) (int)((x).size())
#define all(x) (x).begin(), (x).end()
#define contains(x, y) ((x).find(y) != (x).end())

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

#define TASK "A-large"

struct Dir
{
	map<string, int> c;
};

vector<Dir> words;

int add(int n)
{
	int res = 0;
	for (int i = 0; i < n; i++)
	{
		char buf[1000];
		gets(buf);
		for (int j = 0; buf[j]; j++)
			if (buf[j] == '/') buf[j] = ' ';
		stringstream ss(buf);
		int cur = 0;
		string s;
		while (ss >> s)
		{
			if (!contains(words[cur].c, s))
			{
				res++;
				words.push_back(Dir());
				words[cur].c[s] = sz(words) - 1;
			}
			cur = words[cur].c[s];
		}
	}
	return res;
}

int main()
{
	freopen(TASK ".in", "r", stdin);
	freopen(TASK ".out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int c = 1; c <= t; c++)
	{
		words.clear();
		words.push_back(Dir());
		int n, m;
		scanf("%d%d ", &n, &m);
		add(n);
		printf("Case #%d: %d\n", c, add(m));
	}
	return 0;
}