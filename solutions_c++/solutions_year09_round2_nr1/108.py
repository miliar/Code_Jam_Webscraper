#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

typedef long long int64;
typedef double real;

#define inf 0x3f3f3f3f

#define maxn (1 << 14)

std::string stree;
int pos;
char buf[1 << 12];

struct node {
	real prob;
	std::string property;
	int left, right;
} nodes[maxn];
int nc, root;

int new_node() {
	assert(nc < maxn);
	nodes[nc].property = "";
	nodes[nc].left = nodes[nc].right = -1;
	nodes[nc].prob = 0.0;
	return nc++;
}

void skip_sp() {
	while(pos < stree.length() && isspace(stree[pos]))
		pos++;
}

int parse() {
	int cur = new_node();
	skip_sp();
	assert(pos < stree.length() && stree[pos] == '(');
	pos++;
	skip_sp();
	std::string num;
	while(!isspace(stree[pos]) && stree[pos] != ')')
		num += stree[pos++];
	//Eo(num);
	std::stringstream(num) >> nodes[cur].prob;
	skip_sp();
	if(stree[pos] != ')') {
		while(!isspace(stree[pos]) && stree[pos] != '(')
			nodes[cur].property += stree[pos++];
		nodes[cur].left = parse();
		nodes[cur].right = parse();
		skip_sp();
	}
	assert(pos < stree.length() && stree[pos] == ')');
	pos++;
	return cur;
}

std::set<std::string> features;

real go(int v) {
	long double ans = 1.0L;
	while(nodes[v].property.length() > 0) {
		ans *= nodes[v].prob;
		if(features.find(nodes[v].property) != features.end())
			v = nodes[v].left;
		else
			v = nodes[v].right;
	}
	ans *= nodes[v].prob;
	return ans;
}

int main() {
	int t = 1, tc;
	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d:\n", t);
		stree = "";
		int n, i, j, q;
		scanf("%d", &n); gets(buf);
		for(i = 0; i < n; i++) {
			gets(buf);
			stree += buf;
		}
		//Eo(stree);
		pos = nc = 0;
		root = parse();
		scanf("%d", &n);
		for(i = 0; i < n; i++) {
			scanf(" %s%d", buf, &q);
			features.clear();
			for(j = 0; j < q; j++) {
				scanf(" %s", buf);
				features.insert(buf);
			}
			printf("%.7lf\n", go(root));
		}

	}
	return 0;
}
