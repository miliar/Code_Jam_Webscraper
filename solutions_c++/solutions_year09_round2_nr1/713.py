// Round 1B: A.cpp

#include <cstdio>
#include <cstdlib>
#include <cstring>

struct Node {
	double w;
	char feature[15];
	Node* lc, *rc;
};

// construct a tree
Node* construct() {
	Node* pn=new Node(); pn->lc = pn->rc = NULL;

	char c; 
	while(scanf("%c", &c), c!='(') ;

	while(scanf("%c", &c), c==' '||c=='\n') ;

	char num[100]; memset(num, '\0', 100); int index=0;
	while(((c>='0' && c<='9')||(c=='.')))  {
		num[index++]=c;
		scanf("%c", &c);
	}
	pn->w=atof(num);

	while(c==' '||c=='\n') scanf("%c", &c) ;
	if(c==')') return pn;

	int k=0;  memset(pn->feature, '\0', 15);
	while(c>='a' && c<='z') {
		pn->feature[k++]=c;
		scanf("%c", &c);
	}	
	if(k) {
		pn->lc=construct(); 
		pn->rc=construct(); 
		while(scanf("%c", &c), c!=')' ) ;
	}
	return pn;
}

// compute value
double value = 1.0;
void getValue(Node* pn, char* name, char f[100][15], int fn) {
	value*=pn->w;
	if(pn->lc && pn->rc) {
		bool hasF=false;
		for(int i=0; i<fn; i++){
			if(strcmp(pn->feature, f[i])==0) {
				hasF=true; break;
			}
		}
		if(hasF) getValue(pn->lc, name, f, fn); 
		else getValue(pn->rc, name, f, fn);
	}
}

// compute prob. for one animal
void procOne(Node* pn) {
	char name[15], f[100][15]; int fn;
	scanf("%s %d", name, &fn); 
	for(int i=0; i<fn; i++) scanf("%s", &f[i]);

	value=1.0; getValue(pn, name, f, fn); 
	printf("%.9f\n", value);
}

// for one case
void proOnceCase(int caseNum) {
	int num; scanf("%d", &num);
	Node* pn=construct();

	printf("Case #%d: \n", caseNum);
	scanf("%d", &num);
	for(int i=1; i<=num; i++) 
		procOne(pn);
}

int main() {
	int cases; scanf("%d", &cases); 
	for(int i=1; i<=cases; i++) proOnceCase(i);
	return 0;
}
