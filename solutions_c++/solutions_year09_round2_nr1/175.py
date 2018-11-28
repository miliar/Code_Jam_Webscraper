#include <stdio.h>
#include <stdlib.h>

#include <algorithm>
#include <vector>
#include <string>
#include <stack>
using namespace std;

int L, A, n;

char line[1111];
char input[111111];

struct {
	string name;
	double p;
	int l, r;
}node[1111111];

int bracket[111111];

char temp_str[1111111];

int max_node=1;
vector<string> features;

void const_tree(int a, int b, int num_node) {
	int idx=a+1;
	while(input[idx]!=')' && input[idx]!='(') idx++;
	
	for(int i=a+1;i<idx;i++) {
		temp_str[i-(a+1)] = input[i];
	}
	temp_str[idx-(a+1)]=0;

	double p;
	char str[111];
	node[num_node].l=node[num_node].r=-1;
	if(sscanf(temp_str, "%lf %s", &p, str)==2) {
		node[num_node].p = p;
		node[num_node].name = str;		
	}
	else {
		node[num_node].p = p;
		node[num_node].name="";
	}

	if(input[idx]=='(') {
		node[num_node].l = ++max_node;
		const_tree(idx, bracket[idx], node[num_node].l);

		idx = bracket[idx]+1; while(input[idx]!='(') idx++;
		node[num_node].r = ++max_node;
		const_tree(idx, bracket[idx], node[num_node].r);
	}
}

double res;

void traverse(int v) {
	res *= node[v].p;

	for(int i=0;i<features.size();i++) {
		if(node[v].name == features[i]) {
			if(node[v].l!=-1) traverse(node[v].l);
			return;
		}
	}
	if(node[v].r!=-1) traverse(node[v].r);
}

int main(void) {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T; scanf("%d\n", &T);
	for(int tc=1;tc<=T;tc++) {
		memset(bracket, 0, sizeof(bracket));
		max_node=1;

		scanf("%d\n", &L);
		input[0]=0;
		for(int i=0;i<L;i++) {
			gets(line);
			strcat(input, line);
		}

		// construct tree
		int len = strlen(input);
		stack<int> stk;
		memset(bracket, 0, sizeof(bracket));
		for(int i=0;i<len;i++) {
			if(input[i]=='(') stk.push(i);
			else if(input[i]==')') {
				int t = stk.top(); stk.pop();
				bracket[i]=t;
				bracket[t]=i;
			}
		}

		const_tree(0, bracket[0], 1);
		
		printf("Case #%d:\n", tc);
		scanf("%d\n", &A);
		while(A--) {
			char s_animal[1111], s_feature[11111];
			scanf("%s %d", s_animal, &n);
			features.clear();
			for(int i=0;i<n;i++) {
				scanf("%s", s_feature);
				features.push_back(s_feature);
			}
			res = 1;
			traverse(1);
			printf("%.7lf\n", res);
		}
	}

	return 0;
}