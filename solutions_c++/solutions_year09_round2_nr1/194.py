#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>

#include<algorithm>
#include<string>
using namespace std;

struct node {
	double val;
	int l, r;
	string text;
};

node *tree[8000];
int cur = 0;
string td;
int pos;

int feat;
char ft[128][128];

int parse()
{
	while (td[pos] == ' ' || td[pos] == '\n') ++pos;
	++pos; // skip '('
	double val;
	sscanf(td.substr(pos).c_str(), "%lf", &val);
	while (isdigit(td[pos]) || td[pos] == '.' || td[pos] == ' ' || td[pos] == '\n') ++pos;
	
	if (td[pos] == ')') {
		++pos; // skip ')'
		node *x = new node;
		x->val = val;
		x->l = x->r = -1;
		tree[cur++] = x;
		//printf("inserted %d %d %d\n", cur-1, x->l, x->r);
		return cur-1;
	}
	else {
		node *x = new node;
		char text[16];
		sscanf(td.substr(pos).c_str(), "%s", &text);
		x->text = text;
		x->val = val;
		while ((td[pos] >= 'a' && td[pos] <= 'z') || td[pos] == '.' || td[pos] == ' ' || td[pos] == '\n') ++pos;
		int c = cur++;
		x->l = parse();
		x->r = parse();
		tree[c] = x;
		while (td[pos] == ' ' || td[pos] == '\n') ++pos;
		++pos; // skip ')'
		//printf("inserted %d %d %d\n", c, x->l, x->r);
		return c;
	}
}

double compute(double val, int p)
{
	val *= tree[p]->val;
	//printf("%d\n", p);
	if (tree[p]->l != -1) {
		//printf("%s %d %d\n", tree[p]->text.c_str(), tree[p]->l, tree[p]->r);
		for (int i=0; i<feat; ++i)
			if (ft[i] == tree[p]->text)
				return compute(val, tree[p]->l);
		return compute(val, tree[p]->r);
	}
	else return val;
}

int main(void)
{
	freopen("A-large.in", "rt", stdin);
	freopen("pa.out", "wt", stdout);
	
	int tn;
	scanf("%d\n", &tn);
	for (int tc=0; tc<tn; ++tc) {
		cur = pos = 0;
		td = "";
		int l;
		scanf("%d\n", &l);
		for (int i=0; i<l; ++i) {
			char line[128];
			gets(line);
			td += ' ';
			td += line;
		}
		
		parse();
		
		printf("Case #%d:\n", tc+1);

		// animals
		int anim;
		scanf("%d\n", &anim);
		for (int i=0; i<anim; ++i) {
			char name[128];
			scanf("%s %d", name, &feat);
			for (int j=0; j<feat; ++j)
				scanf("%s", ft[j]);
			scanf("\n");
			
			printf("%.7lf\n", compute(1, 0));
		}
	}
	
	return 0;
}
