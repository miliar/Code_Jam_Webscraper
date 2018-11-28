#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <set>
#include <iostream>
//#include <map>
//#include <vector>

using namespace std;
#define dprintf debug && printf
const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

struct Tree {
	Tree(double p) : p(p), left(0), right(0), prop() {
	}

	double prob(const set<string> &props) {
		double ret = p;
		if(left) {
			if(props.find(prop) != props.end()) {
				ret *= left->prob(props);
			} else {
				ret *= right->prob(props);
			}
		}
		return ret;
	}

	~Tree() {
		if(left)
			delete left;
		if(right)
			delete right;
	}

	double p;
	Tree *left;
	Tree *right;
	string prop;
};

int nextchar() {
	int ch = getchar();
	while(isspace(ch)) {
		ch = getchar();
	}
	return ch;
}

Tree *parsetree() {

	int ch = nextchar();
	assert(ch == '(');
	double prob;
	if(scanf("%lf", &prob) != 1)
		assert(!"Failed to read prob");

	Tree *ret = new Tree(prob);
	ch = nextchar();
	if(ch == ')')
		return ret;
	ungetc(ch, stdin);
	char buf[2000];
	if(scanf("%s", buf) != 1)
		assert(!"Failed to read property");
	ret->prop = buf;
	ret->left = parsetree();
	ret->right = parsetree();
	ch = nextchar();
	assert(ch == ')');
	return ret;
}

bool solve(int P) {
	printf("Case #%d:\n", P+1);
	int n;
	if(scanf("%d", &n) != 1)
		assert(!"Couldn't read number of lines of tree");

	Tree *t = parsetree();
	if(scanf("%d", &n) != 1)
		assert(!"Couldn't read number of animals");
	for(int i = 0; i < n; ++i) {
		string animal;
		set<string> props;
		int k;
		cin >> animal >> k;
		while(k--) {
			string prop;
			cin >> prop;
			props.insert(prop);
		}
		printf("%.7lf\n", t->prob(props));
	}

	delete t;

	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
