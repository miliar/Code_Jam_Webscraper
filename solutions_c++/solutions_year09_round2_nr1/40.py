// GCJ Round 1B - Problem A
// -- strapahuulius

// pre-written code follows
// #includes {{{
#include <algorithm>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
// }}}
// constants, typedefs, macros {{{
typedef long long LL;
typedef unsigned long long ULL;
const int oo = 1000000000;
const LL OO = 1000000000000000000LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef queue<int> QI;
typedef queue<PII> QPII;
typedef complex<double> tComp;
const double PI = 2.0 * acos(0.0);
const double EPS = 1e-9;
#define FORIT(i,c) for (typeof((c).end()) i=(c).begin(); i!=(c).end(); ++i)
#define CERR(x) cerr << (#x) << " = " << (x) << endl
#define COUT(x) cout << (#x) << " = " << (x) << endl
// }}}

// code written during the competition follows
int cnt = 0;
string eat_brackets(string s)
{
	assert(!s.empty());
	int a = 0, b = s.size() - 1;
	while (s[a] != '(')
		a++;
	while (s[b] != ')')
		b--;
	s = s.substr(a+1, b-a-1);
	return s;
}
char buf[128];
struct Node 
{
	Node() {}
	double weight;
	string fe;
	int ch0, ch1;
	Node(string);
	double get_prob(const set<string> &);
} node[1000000];
Node::Node(string tmp)
{
	tmp = eat_brackets(tmp);
	fe.clear();
	ch0 = ch1 = -1;
	if (sscanf(tmp.c_str(), "%lf %s", &weight, buf) == 2)
	{
		fe = buf;
		int z = 0;
		string all;
		FORIT(it, tmp)
		{
			if (z == 0)
				all.clear();
			all += *it;
			if (*it == '(')
			{
				z++;
			}
			else if (*it == ')')
			{
				z--;
				if (z == 0)
				{
					if (ch0 == -1)
					{
						ch0 = cnt++;
						node[ch0] = Node(all);
					}
					else
					{
						ch1 = cnt++;
						node[ch1] = Node(all);
					}
				}
			}
		}
		return;
	}
}
double Node::get_prob(const set<string> &st)
{
	if (fe.empty())
		return weight;
	return weight * (st.count(fe) ? node[ch0].get_prob(st) : node[ch1].get_prob(st));
}
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		int L;
		cin >> L;
		string tmp;
		getline(cin, tmp);
		string all;
		for (int i=0; i<L; i++)
		{
			string tmp;
			getline(cin, tmp);
			all += tmp;
		}
		cnt = 1;
		node[0] = Node(all);
		printf("Case #%d:\n", tkase+1);
		int q;
		cin >> q;
		while (q--)
		{
			set<string> st;
			cin >> tmp;
			int k;
			cin >> k;
			while (k--)
			{
				cin >> tmp;
				st.insert(tmp);
			}
			printf("%.7lf\n", node[0].get_prob(st));
		}
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
