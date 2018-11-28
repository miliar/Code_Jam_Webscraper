#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include "string.h"
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	string s1 = " zyqeeejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
	string s2 = " qazooourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";

	map<char, char> M;

	REP (i, s1.size())
		M[s1[i]] = s2[i];

	char ss[250];
	gets(ss);

	int tt;
	sscanf(ss, "%d", &tt);

	REP (t, tt)
	{
		cout << "Case #" << t+1 <<": ";
		gets(ss);
		string s(ss);

		REP(i, s.size()) {
			if (M.count(s[i]))
				cout << M[s[i]];
			else
				cout << s[i];
		}

		cout << endl;
	}



	return 0;
}
