#include <cstdio>
#include <string>
#include <stack>
#include <set>
#include <sstream>
using namespace std;

int N, L, A;

struct node {
	node() { left = right = NULL; feat = ""; }
	double val;
	string feat;
	node *left, *right;
} *root;

stack<node *> S;
string line;

void clr(node *r) {
	if(r == NULL) return;
	clr(r->left);
	clr(r->right);
	delete r;
}

void wrt(node *r) {
	if(r == NULL) return;
	printf("%s(%lg)", r->feat.c_str(), r->val);
	printf(" ( "); wrt(r->left); printf(" ) ");
	printf(" ( "); wrt(r->right); printf(" ) ");
}

int main() {
	scanf("%d", &N);
	for(int z=0; z<N; ++z) {
		scanf("%d\n", &L); line = "";
		for(int i=0; i<L; ++i) {
			//printf("%d\n", i); // debug
			char aux[82];
			gets(aux);
			//printf("%s\n", aux); // debug
			line += " " + string(aux);
		}
		//printf("%s\n", line.c_str()); // debug
		int k = line.size();
		string buf = "";
		for(int j=0; j<k; ++j) {
			//printf("%d\n", j); // debug
			if(line[j] == '(') {
				S.push(new node()); ++j;
				while(line[j] == ' ') ++j;
				while(line[j] != ' ' && line[j] != ')') {
					buf += line[j]; ++j;
				}
				//printf("%s\n", buf.c_str()); // debug
				stringstream str;
				str << buf;
				str >> S.top()->val;
				//sscanf(buf.c_str(), "%f", &S.top()->val);
				//printf("%f\n", S.top()->val); // debug
				buf = ""; --j;
			} else if(line[j] == ')') {
				node *cur = S.top(); S.pop();
				if(S.empty()) {
					root = cur;
				} else {
					if(S.top()->left == NULL) S.top()->left = cur;
					else S.top()->right = cur;
				}
			} else if('a' <= line[j] && line[j] <= 'z') {
				while(line[j] != ' ') {
					buf += line[j]; ++j;
				}
				S.top()->feat = buf;
				buf = "";
			}
		}
		//printf("ok\n"); // debug
		//wrt(root); printf("\n"); // debug
		scanf("%d", &A);
		printf("Case #%d:\n", z + 1);
		for(int i=0; i<A; ++i) {
			char name[12]; int n;
			scanf("%s%d", name, &n);
			set<string> F;
			for(int j=0; j<n; ++j) {
				char fn[12];
				scanf("%s", fn);
				F.insert(fn);
			}
			double p = 1.0;
			node *tmp = root;
			while(true) {
				p *= tmp->val;
				if(tmp->left == NULL) break;
				if(F.find(tmp->feat) != F.end()) tmp = tmp->left;
				else tmp = tmp->right;
			}
			printf("%.7lf\n", p);
		}
		clr(root);
	}
	return 0;
}
