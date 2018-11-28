#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<iostream>
#include<sstream>

using namespace std;

const int MAX_NODE = 30000000;

char desc[30000];
char line[300];
char tmp[300];
set<string> feature;
istringstream iss;

struct Node {
	char feat[12];
	double p;
	int lc;
	int rc;
	void clear() {
		feat[0] = 0;
		p = 1;
		lc = -1;
		rc = -1;
	}
}nodes[MAX_NODE];
int num;

void build_sub_tree(int root) {
	char str[15];
	double w;

	iss >> str;  // '('
	iss >> w;  // weight
	int curr = num++;
	nodes[curr].clear();
	nodes[curr].p = w;
	nodes[root].lc = curr;

	iss >> str;
	if (str[0] == ')') {  // leaf node
		;
	} else {  // inner node
		strcpy(nodes[curr].feat, str);
		build_sub_tree(curr);
		iss >> str;  // ')'
	}

	iss >> str;  // '('
	iss >> w;  // weight
	curr = num++;
	nodes[curr].clear();
	nodes[curr].p = w;
	nodes[root].rc = curr;

	iss >> str;
	if (str[0] == ')') {  // leaf node
		;
	} else {  // inner node
		strcpy(nodes[curr].feat, str);
		build_sub_tree(curr);
		iss >> str;  // ')'
	}
}

void build_tree() {
	iss.str(desc);
	char str[15];
	double w;

	num = 1;

	iss >> str;  // '('
	iss >> w;  // weight
	nodes[0].clear();
	nodes[0].p = w;

	iss >> str;
	if (str[0] == ')') {  // leaf node
		return;
	} else {  // inner node
		strcpy(nodes[0].feat, str);
		build_sub_tree(0);
		iss >> str;  // ')'
	}
}

int isempty(char c) {
	return c == ' ';
}

void proc(char *s) {
	while (*s) {
		if (*s == '(' && !isempty(*(s + 1))) {
			strcpy(tmp, s + 1);
			*(s + 1) = ' ';
			strcpy(s + 2, tmp);
		}

		if (*s == ')' && !isempty(*(s - 1))) {
			strcpy(tmp, s);
			*s = ' ';
			strcpy(s + 1, tmp);
		}
		++s;
	}

	if (*(s - 1) != ' ') {
		*s = ' ';
		*(s + 1) = '\0';
	}
}

void show_tree(int r, int indent) {
	for (int i = 0; i < indent; i++) putchar(' ');
	printf("%lf ", nodes[r].p);
	if (nodes[r].lc != -1) {
		printf("%s\n", nodes[r].feat);
		show_tree(nodes[r].lc, indent + 2);
		show_tree(nodes[r].rc, indent + 2);
	} else {
		puts("");
	}
}

double go(int r, double p) {
	p *= nodes[r].p;
	if (nodes[r].lc == -1) {
		return p;
	}
	if (feature.find(string(nodes[r].feat)) != feature.end()) {
		return go(nodes[r].lc, p);
	} else {
		return go(nodes[r].rc, p);
	}
}

void solve(int cn) {
	memset(desc, 0, sizeof(desc));

	int L;
	scanf("%d", &L);
	gets(line);

	while (L--) {
		gets(line);
		proc(line);
		strcat(desc, line);
	}

	build_tree();
	//show_tree(0, 0);
	
	printf("Case #%d:\n", cn);

	int A;
	scanf("%d", &A);
	while (A--) {
		char name[15];
		scanf("%s", name);
		int n;
		scanf("%d", &n);
		feature.clear();
		while (n--) {
			char feat[15];
			scanf("%s", &feat);
			feature.insert(string(feat));
		}
		double ans = go(0, 1);
		printf("%.10lf\n", ans);
	}
}


int main() {
	int T;
	scanf("%d", &T);
	for (int cn = 1; cn <= T; cn++) {
		solve(cn);
	}
	return 0;
}

