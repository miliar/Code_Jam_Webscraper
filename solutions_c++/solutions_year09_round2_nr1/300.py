#include <cstdio>
#include <string>
#include <set>

using std::string;
using std::set;

struct DecTree {
	double weight;
	string name;
	struct DecTree *yes;
	struct DecTree *no;
	DecTree():weight(1),yes(0),no(0) {}
};

char c;
void inputTree(FILE *f, DecTree *tree) {
	while (c != '(')
		fscanf(f, "%c", &c);
	fscanf(f, "%lf", &tree->weight);
	fscanf(f, "%c", &c);
	while (c != ')' && (c < 'a' || c > 'z')) {
		fscanf(f, "%c", &c);
	}
	if (c == ')') {
		tree->name = "";
		tree->yes = 0;
		tree->no = 0;
		fscanf(f, "%c", &c);
	} else {
		char buf[2];
		buf[0]=buf[1]=0;
		tree->name = "";
		while (c >= 'a' && c <= 'z') {
			buf[0] = c;
			tree->name = tree->name + string(buf);
			fscanf(f, "%c", &c);
		}
		tree->yes = new DecTree();
		tree->no = new DecTree();
		inputTree(f, tree->yes);
		inputTree(f, tree->no);
		while (c != ')')
			fscanf(f, "%c", &c);
		fscanf(f, "%c", &c);
	}
}

double getProb(DecTree *tree, const set<string> &ss) {
	double p = tree->weight;
	if (tree->name.length() > 0) {
		if (ss.find(tree->name) != ss.end()) {
			p *= getProb(tree->yes, ss);
		} else {
			p *= getProb(tree->no, ss);
		}
	}
	return p;
}

int main(int argc, char **argv)
{
	FILE *f = fopen(argv[1], "r");
	FILE *out = fopen("out.out", "w");
	int N;
	fscanf(f, "%d", &N);
	for (int i = 0; i < N; i++) {
		DecTree tree;
		fprintf(out, "Case #%d:\n", i+1);
		fscanf(f, "%c", &c);
		inputTree(f, &tree);
		int A;
		fscanf(f, "%d", &A);
		for (int j = 0; j < A; j++) {
			double res;
			int n;
			char buf[100];
			fscanf(f, "%s", buf);
			fscanf(f, "%d", &n);
			set<string> ss;
			for (int k = 0; k < n; k++) {
				char buf[100];
				fscanf(f, "%s", buf);
				ss.insert(string(buf));
			}
			res = getProb(&tree, ss);
			fprintf(out, "%.10lf\n", res);
		}
	}
	fclose(out);
	fclose(f);
}
