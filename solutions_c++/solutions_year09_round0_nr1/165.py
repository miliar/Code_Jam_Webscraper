#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>

using namespace std;

int dbg;

string readLine() {
	char sz[1000];
	fgets(sz, 1000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}

int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}

vector<int> readVI() {
	int n;
	scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}

class Tree {
public:
Tree() { kids = NULL; }
~Tree() { if (kids) { for (int i = 0; i < 27; i++) if (kids[i]) delete kids[i]; delete []kids; } }
void add(const char *wd) {
	if (!kids) { kids = new Tree*[27]; memset(kids, 0, sizeof(Tree*)*27); }
	if (*wd < 'a') {
		kids[26] = new Tree;
	} else {
		int c = *wd-'a';
		if (!kids[c]) kids[c] = new Tree;
		kids[c]->add(wd+1);
	}
}
int count(const char *wd) {
	if (*wd < ' ') return kids[26] != NULL;
	int sum = 0;
	if (*wd == '(') {
		const char *p = wd;
		while (*p >= ' ' && *p != ')') p++;
		p++;
		for (const char *q = wd+1; q+1 < p; q++) {
			int c = *q-'a';
			if (kids[c]) sum += kids[c]->count(p);
		}
	} else {
		int c = *wd-'a';
		if (kids[c]) sum = kids[c]->count(wd+1);
	}
	return sum;
}
Tree** kids;
};

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int L, D, CCT;
	scanf("%d %d %d ", &L, &D, &CCT);
	char sz[512];
	Tree root;
	for (int i = 0; i < D; i++) {
		scanf("%511s", sz);
		root.add(sz);
	}
	for (int cn = 1; cn <= CCT; cn++) {
		scanf("%511s", sz);
		int res = root.count(sz);
		printf("Case #%d: %d\n", cn, res);
	}
	return 0;
}

