#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <set>
#include <map>
#include <math.h>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define REP(i, a, b) for (int (i) = (a); (i) <= (b); (i)++)
#define DFOR(i, a, b) for (int (i) = (a) - 1; (i) >= (b); (i)--)
#define CLR(a, b) memset(a, (b), sizeof(a))
#define VI vector <int>
#define VS vector <string>
#define PB push_back
#define MP make_pair
#define SS stringstream
#define INF 1073741824
#define PII pair <int, int>
#define ALL(a) a.begin(), a.end()
#define SZ(x) (int)x.size()

#define LL long long
#define X first
#define Y second

void init()
{
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
}

const int maxn = 60010;

double p[maxn];
string s[maxn];
vector < int > g[maxn];
set < string > features;
int n, pos, cur, lines;
char buf[maxn];

string t;

int parse()
{
	if (t[pos] == '(') pos++;
	string dig = "";
	while (isdigit(t[pos]) || t[pos] == '.') {
		dig += t[pos++];
	}
	int v = ++cur;
	sscanf(dig.c_str(), "%lf", &p[v]);
	if (islower(t[pos]))
	{
		s[v] = "";
		while (islower(t[pos]))
			s[v] += t[pos++];
		int a = parse();
		int b = parse();
		g[v].PB(a);
		g[v].PB(b);
	}
	if (t[pos] == ')') pos++;
	return v;
}

double calc(int v)
{
	double res = 1.0;
	if (SZ(g[v]) > 0) {
		if (features.find(s[v]) != features.end())
			res = calc(g[v][0]);
		else
			res = calc(g[v][1]);
	}
	return p[v] * res;
}

void solvecase(int test)
{
	cout << "Case #" << test << ":" << endl;	
	CLR(p, 0);
	CLR(g, 0);
	CLR(s, 0);
	//FOR(i, maxn) {
	//	p[i] = 0;
	//	s[i] = "";
	//	g[i].clear();
	//}

	t = "";
	scanf("%d\n", &lines);
	FOR(i, lines) {
		gets(buf);
		string r = string(buf);
		for (int i = SZ(r) - 1; i >= 0; --i)
			if (r[i] == ' ') r.erase(r.begin() + i);
		t += r;
	}

	cur = -1;
	pos = 0;
	parse();

	scanf("%d\n", &n);
	FOR(i, n) {
		features.clear();
		string name;
		int k;
		cin >> name >> k;
		FOR(j, k) {
			string f;
			cin >> f;
			features.insert(f);
		}
		double res = calc(0);
		printf("%.7lf\n", res);
	}
}

void solve()
{
	int T;
	scanf("%d\n", &T);
	FOR(i, T) solvecase(i + 1);
}

int main()
{
	init();
	solve();
	return 0;
}