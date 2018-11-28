#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <complex>
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
typedef vector<string> VS;
struct Node
{
	double val;
	string feature;
	Node *left;
	Node *right;
	Node(double val) :  val(val), feature(""), left(0), right(0)
	{
	}
	Node(double val, string feature, Node *left, Node *right) : val(val), feature(feature), left(left), right(right)
	{
	}
};

char buffer[1024*1024];
typedef char * pchar;

Node *parseTree(pchar &p)
{
	while (*p++ != '(');
	double val;
	sscanf(p, "%lf ", &val);
	while (*p != ')' && (!('a' <= *p && *p <= 'z')))
		p++;
	if (*p == ')')
		return new Node(val);	
	sscanf(p, "%s", buffer);
	string feature = buffer;
	Node *right = parseTree(p);
	Node *left = parseTree(p);
	return new Node(val, feature, left, right);
}
double eval(Node *node, const set<string> &props)
{
	double res = node->val;
	if (node->feature == "")
		return res;
	if (props.find(node->feature) != props.end())
		res *= eval(node->right, props);
	else
		res *= eval(node->left, props);
	return res;
}
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w+", stdout);
	cin.getline(buffer, 1024*1024);
	int n;
	sscanf(buffer, "%d", &n);
	FOR(it,1,n+1)
	{
		cin.getline(buffer, 1024*1024);
		int t;
		sscanf(buffer, "%d", &t);
		VS tree;
		REP(i,t)
		{
			cin.getline(buffer, 1024*1024);
			tree.pb(buffer);
		}
		string tr = accumulate(ALL(tree), string());
		char *zz = (char *)tr.c_str();
		Node *root = parseTree(zz);
		printf("Case #%d:\n", it);
		cin.getline(buffer, 1024*1024);
		int q;
		sscanf(buffer, "%d", &q);
		REP(i,q)
		{
			cin.getline(buffer, 1024*1024);
			istringstream in(buffer);
			string sss;
			set<string> props;
			in >> sss;
			int nn;
			in >> nn;
			REP(j,nn)
			{
				in >> sss;
				props.insert(sss);
			}
			printf("%.7lf\n", eval(root, props));
		}
	}
}
