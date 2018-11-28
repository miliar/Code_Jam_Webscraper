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

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define sz size()

typedef long long i64;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

struct Node
{
	double weight;
	string feature;
	Node *p1, *p2;

	Node() : p1(NULL), p2(NULL), feature("") {
	}

	~Node() {
		if (p1 != NULL) delete p1;
		if (p2 != NULL) delete p2;
	}
};

Node* read_tree()
{
	char ch;
	while ((ch = getchar()) != '(') {
	}

	Node* result = new Node();
	scanf("%lf", &result->weight);
	
	while (isspace(ch = getchar())) {
	}

	if (ch != ')') {
		result->feature += ch;
		while (!isspace(ch = getchar()))
			result->feature += ch;
		result->p1 = read_tree();
		result->p2 = read_tree();
	} 

	while (ch != ')')
		ch = getchar();

	return result;
}

string read_string()
{
	string result;
	char ch;
	while (isspace(ch = getchar())) {
	}
	result += ch;
	while (!isspace(ch = getchar()))
		result += ch;
	return result;
}

void solve()
{
	scanf("%*d");
	Node* root = read_tree();

	int A;
	scanf("%d", &A);
	REP(i, A) {
		set<string> features;
		string animal = read_string();
		int n;
		scanf("%d", &n);
		REP(j, n)
			features.insert(read_string());

		double res = 1.0;
		Node* p = root;
		while (true) {
			res *= p->weight;
			if (p->feature != "") {
				if (features.count(p->feature))
					p = p->p1; else
					p = p->p2;
			} else
				break;
		}
		printf("%.7lf\n", res);
	}

	delete root;
}

int main()
{
//	freopen("input.txt", "r", stdin);

	int n_test;
	scanf("%d\n", &n_test);
	REP(i_test, n_test) {
		printf("Case #%d:\n", i_test+1);
		solve();
	}

	return 0;
}
