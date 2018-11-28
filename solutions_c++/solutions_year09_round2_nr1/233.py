#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cfloat>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <bitset>

#define REP(i,a) for(i=0;i<a;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define sz(x) (int)(x).size()
using namespace std;

class node {
public:
	node() {
		parent = NULL;
		left = NULL;
		right = NULL;
		p = -1;
	}
	~node() {
		if (left)
			delete left;
		if (right)
			delete right;
	}

	void preorder() {
		cout << "root is " << p << ' ' << feature << endl;
		cout << "from " << feature << " going left..." << endl;
		if (left != NULL)
			left->preorder();
		else
			cout << "left not" << endl;
		cout << "from " << feature << " going right..." << endl;
		if (right != NULL)
			right->preorder();
		else
			cout << "right not" << endl;
	}
	node* left;
	node* right;
	node* parent;
	double p;
	string feature;
};

node* parse(string x) {
	int n = x.length();
	int i,j;
	node* now = NULL;
	double value = -1;
	string name;
	string valuest;
	REP(i,n) {
		if (x[i] == '(') {
			if (now != NULL && value != -1) {
				now->feature = name;
				now->p = value;
			}
			value = -1;
			name.clear();

			node* prev = now;
			now = new node();
			now->parent = prev;
		} else if (x[i] == ')') {
			if (value != -1) {
				now->p = value;
			}
			value = -1;
			node* prev = now->parent;
			if (prev == NULL) {
				continue;
			}

			if (prev->left == NULL) {
				prev->left = now;
			} else
				prev->right = now;
			now = prev;
		} else if (x[i] == '0' || x[i] == '1') {
			valuest.clear();
			while (i < n && x[i] != ' ' && x[i] != '\n' && x[i] != ')')
				valuest += x[i++];
			value = atof(valuest.c_str());
			--i;
		} else if (x[i] >= 'a' && x[i] <= 'z') {
			name += x[i];
		} else if (x[i] == ' ' || x[i] == '\n') {
		}
	}

	return now;
}

void parse_animal(char* x, string* name, set<string>* attr) {
	char* t = strtok(x, " ");
	(*name) = t;
	t = strtok(NULL, " ");
	int n = atoi(t);
	int i;
	REP(i,n) {
		t = strtok(NULL, " ");
		attr->insert(t);
	}
}

double traverse(node* root, set<string>* attr) {
	node* now = root;
	double p = 1;
	while (now != NULL) {
		p *= now->p;
		string at = now->feature;
		if (at.empty() || attr->count(at) == 0) {
			now = now->right;
		} else
			now = now->left;
	}
	return p;
}

int main() {
	int N;
	int L;
	int A;
	char buf[50000];

	gets(buf);
	sscanf(buf, "%d", &N);

	int i,j,k;

	REP(i,N) {
		gets(buf);
		sscanf(buf, "%d", &L);

		string tree_st;
		REP(j,L) {
			gets(buf);
			tree_st += buf;
		}
		node* tr = parse(tree_st);

		gets(buf);
		sscanf(buf, "%d", &A);

		printf("Case #%d:\n", i+1);
		REP(j,A) {
			gets(buf);
			string name;
			set<string> attr;
			parse_animal(buf, &name, &attr);

			double pr = traverse(tr, &attr);
			printf("%.7lf\n",pr);
		}
	}
}
