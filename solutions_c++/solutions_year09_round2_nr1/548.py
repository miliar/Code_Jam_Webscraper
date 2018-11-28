#include <cstdio>
#include <iostream>
#include <set>

using namespace std;

struct tree {
	double w;
	char name[400];
	struct tree *left, *right;
};

struct tree *parsetree() {
	// cerr << "recur\n";
	struct tree *ret = new struct tree;
	char c = fgetc(stdin);
	while ((c == ' ') || (c == '\n')) {
		// cerr << "read whitespace" << endl;
		c = fgetc(stdin);
	}
	if (c != '(') cerr << "ehm\n";
	double weight;
	scanf("%lf", &weight);
	ret->w = weight;
	// cerr << "read weight " << weight << endl;

	scanf("%s", ret->name);
	if (ret->name[0] == ')') {
		ret->left = NULL;
		ret->right = NULL;
		ret->name[0] = 0;
		return ret;
	}
	// cerr << "read name " << ret->name << endl;
	ret->left = parsetree();
	ret->right = parsetree();
	c = fgetc(stdin);
	while ((c == ' ') || (c == '\n')) {
		c = fgetc(stdin);
	}
	if (c != ')') cerr << "ehm2\n";
	return ret;
}

double find(const struct tree *n, const set<string> &feats, double prob) {
	if (n->name[0] == 0) return n->w*prob;
	if (feats.find(n->name) == feats.end()) {
		return find(n->right, feats, prob*n->w);
	} else {
		return find(n->left, feats, prob*n->w);
	}
}

int main(int argc, char **argv) {
	int nTests;
	scanf("%d", &nTests);
	for (int i = 1; i <= nTests; ++i) {
		int lines;
		scanf("%d", &lines);
		struct tree *root = parsetree();
		int nQueries;
		scanf("%d", &nQueries);
		printf("Case #%d:\n", i);
		for (int j = 0; j < nQueries; ++j) {
			char name[300];
			int nFeats;
			scanf("%s%d", name, &nFeats);
			set<string> feats;
			for (int k = 0; k < nFeats; ++k) {
				string f;
				cin >> f;
				feats.insert(f);
			}
			double prob = find(root, feats, 1);
			printf("%.7lf\n", prob);
		}
	}
}
