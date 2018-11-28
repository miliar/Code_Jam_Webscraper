#include <set>
#include <string>
#include <sstream>
#include <stdio.h>
using namespace std;

struct Node {
	double w;
	string feature;
	Node *left, *right;
	Node(): left(0), right(0) { }
	~Node() { delete left; delete right; }
	void read();
};

void Node::read() {
	char name[16];
	scanf("%lf", &w);
	do {
		name[0] = (char)getc(stdin);
	} while (name[0]!=')' && (name[0]<'a'||name[0]>'z'));
	if (name[0]!=')') {
		int i;
		for (i=1; ; i++) {
			name[i] = (char)getc(stdin);
			if (name[i]<'a'||name[i]>'z')
				break;
		}
		if (name[i]!='(')
			while (getc(stdin)!='(');
		name[i] = 0;
		feature = string(name);
		left = new Node;
		left->read();
		while (getc(stdin)!='(');
		right = new Node;
		right->read();
		while (getc(stdin)!=')');
	}
}

void runTest(int testCase) {
	char buf[10000];
	int L;
	scanf("%d", &L);
	Node root;
	while (getc(stdin)!='(');
	root.read();
	int A;
	scanf("%d", &A);
	gets(buf);
	printf("Case #%d:\n", testCase);
	for (int i=0; i<A; i++) {
		gets(buf);
		istringstream fi(buf);
		int n;
		string animal, feature;
		fi >> animal >> n;
		set<string> features;
		for (int j=0; j<n; j++) {
			fi >> feature;
			features.insert(feature);
		}
		double p = 1;
		for (Node *node=&root; node;) {
			p *= node->w;
			node = features.find(node->feature)!=features.end() ? node->left : node->right;
		}
		printf("%.16lf\n", p);
	}
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int N;
	scanf("%d", &N);
	for (int i=0; i<N; i++)
		runTest(i+1);
	return 0;
}
