#include <algorithm>
#include <cassert>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

struct node {
	node() : left(0), right(0), s(0) {}
	node *left, *right;
	double p;
	string *s;
};

void skip_ws() {
	int c;
	do {
		c = getchar();
	} while (isspace(c));
	ungetc(c, stdin);
}

char feature[20];

node* do_read() {
	node* res = new node;
	skip_ws();
	assert(getchar() == '(');
	double p;
	scanf("%lf", &res->p);
	skip_ws();
	int c = getchar();
	if (c != ')') {
		ungetc(c, stdin);
		scanf("%s", feature);
		res->s = new string(feature);
		res->left = do_read();
		res->right = do_read();
		skip_ws();
		assert(getchar() == ')');
	}
	return res;
}

double calculate(node *root, const vector<string>& features) {
	double res = 1;
	while (true) {
		res *= root->p;
		if (!root->s) break;
		if (binary_search(features.begin(), features.end(), *root->s))
			root = root->left;
		else
			root = root->right;
	}
	return res;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int T=1; T<=t; T++) {
		int l;
		scanf("%d", &l);
		node *root = do_read();
		int a;
		scanf("%d", &a);
		printf("Case #%d:\n", T);
		char buf[100];
		for (int j=0; j<a; j++) {
			scanf("%s", buf);
			int n;
			scanf("%d", &n);
			vector<string> features(n);
			for (int i=0; i<n; i++) {
				scanf("%s", buf);
				features[i] = string(buf);
			}
			sort(features.begin(), features.end());
			printf("%.7lf\n", calculate(root, features));
		}
	}
	return 0;
}