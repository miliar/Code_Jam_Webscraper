#include <set>
#include <cctype>
#include <cstdio>
#include <string>

using namespace std;

struct Node {
	double p;
	string s;
	Node *t, *f;
	Node(double p, const string& s) : p(p), s(s) {
		t = f = NULL;
	}
	~Node() {
		delete t;
		delete f;
	}
	double eval(const set<string>& st) const {
		if (t == NULL) {
			return p;
		} else if (st.count(s) > 0) {
			return p * t->eval(st);
		} else {
			return p * f->eval(st);
		}
	}
};

Node* nextNode() {
	static double p;
	static char buf[1024];
	buf[0] = '\0';
	scanf(" ( %lf %[a-z]", &p, buf);
	Node* ret = new Node(p, buf);
	if (buf[0] != '\0') {
		ret->t = nextNode();
		ret->f = nextNode();
	}
	scanf(" )");
	return ret;
}

int main() {
	int re, n, m;
	char buf[1024];

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%*d");
		Node* tree = nextNode();
		scanf("%d", &n);
		printf("Case #%d:\n", ri);
		for (int i = 0; i < n; ++i) {
			scanf("%*s%d", &m);
			set<string> st;
			for (int i = 0; i < m; ++i) {
				scanf("%s", buf);
				st.insert(buf);
			}
			printf("%.7lf\n", tree->eval(st));
		}
		delete tree;
	}

	return 0;
}

