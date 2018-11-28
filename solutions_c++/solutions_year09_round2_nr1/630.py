#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <list>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define sz(a) ((int)a.size())
#define cl clear()
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define ALL(a) a.begin(), a.end()
#define sqr(a) ((a)*(a))

typedef long long ll;

string s, e;
map <string, int> a;

double strtofloat(string s)
{
	stringstream ss(s);
	double e;
	ss >> e;
	return e;
}

double prob(string s)
{
//	cerr << s << endl;
//	REP(i, 10000000)
//	{
//		int j = i % 100;
//	}
	int i = 0;
	while (i < sz(s) && s[i] != '(')
		i++;
	i++;
	while (i < sz(s) && !(s[i] >= '0' && s[i] <= '9'))
		i++;
	string t = "";
	while (i < sz(s) && (s[i] == '.' || (s[i] >= '0' && s[i] <= '9')))
		t += s[i++];
	double p = strtofloat(t);
	t = "";
	while (i < sz(s) && !(s[i] <= 'z' && s[i] >= 'a') && s[i] != ')')
		i++;
	if (s[i] == ')')
		return p;
	while (i < sz(s) && (s[i] <= 'z' && s[i] >= 'a'))
	{
		t += s[i];
		i++;
	}
	int q = a[t];
	t = "";
	while (i < sz(s) && s[i] != '(')
		i++;
	int ee = 1;
	t = "(";
	i++;
	while (ee != 0)
	{
		t += s[i];
		if (s[i] == ')')
			ee--;
		if (s[i] == '(')
			ee++;
		i++;
	}
	i++;
	if (q)
		return (p * prob(t));
	t = "";
	while (i < sz(s) && s[i] != '(')
		i++;
	ee = 1;
	t = "(";
	i++;
	while (ee != 0)
	{
		t += s[i];
		if (s[i] == ')')
			ee--;
		if (s[i] == '(')
			ee++;
		i++;
	}
	return p * prob(t);
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int t;
	scanf("%d\n", &t);
	REP(tt, t)
	{
		printf("Case #%d:\n", tt + 1);
		int n;
		scanf("%d\n", &n);
		s = "";
		REP(i, n)
		{
			getline(cin, e);
			s += e;
		}
		scanf("%d\n", &n);
		REP(i, n)
		{
			stringstream ss;
			getline(cin, e);
			a.cl;
			int m;
			ss << e;
			ss >> e >> m;
			REP(j, m)
			{
				ss >> e;
				a[e] = 1;
			}
			printf("%.7lf\n", prob(s));
		}
	}
	return 0;
}
