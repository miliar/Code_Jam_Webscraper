#include <algorithm>
#include <iostream>
#include <cassert>
#include <set>
using namespace std;

#define MAX 20

struct pNode {
	double weight;
	char name[MAX];
	pNode *left, *right;
};

pNode * parseTree() {
	pNode *p=new pNode();
	p->left=p->right=NULL;	
	
	char c; 
	do {scanf("%c", &c);} while (c=='\n' || c==' ');	
	assert(c=='(');
	
	scanf("%lf", &p->weight);
	
	do {scanf("%c", &c);} while (c=='\n' || c==' ');	
	
	if (c==')') return p;	
	
	p->name[0]=c;
	int i=1;
	while (1) {
		scanf("%c", &c); 
		if (!islower(c)) break;		
		p->name[i]=c;
		++i;
	}
	p->name[i]=0;

	p->left=parseTree();
	p->right=parseTree();
	do {scanf("%c", &c);} while (c=='\n' || c==' ');
	assert(c==')');
	return p;
}

pNode *tree;

struct animal {
	char name[MAX];
	set<string> fea;
};

double cuteProb(pNode *p, animal &an) {
	if (p->left==NULL) return p->weight;	
	
	double prob=p->weight;
	
	if (an.fea.find(p->name)!=an.fea.end()) 
		prob*=cuteProb(p->left, an);
	else 
		prob*=cuteProb(p->right, an);		
	
	return prob;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int nTest;
	scanf("%d", &nTest);
	for (int test=1; test<=nTest; ++test) {
		int l;	
		scanf("%d", &l);
		tree=parseTree();	
		int a;
		scanf("%d\n", &a);
		
		printf("Case #%d:\n", test);

		for (int i=0; i<a; ++i) {
			animal an;
			scanf("%s", &an.name);
			
			int nf;
			scanf("%d", &nf);
			
			for (int j=0; j<nf; ++j) {
				char fea[MAX];
				scanf("%s", &fea);
				an.fea.insert(fea);
			}
			
			printf("%.7lf\n", cuteProb(tree,an));
		}		
	}

	return 0;
}
