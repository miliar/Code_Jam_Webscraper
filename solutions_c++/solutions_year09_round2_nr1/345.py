
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int U32;

struct node {
	double p;
	char f[90];
	node *n1,*n2;
};

node *parse() {
	node *root = new node;
	scanf("( %lg %s ",&(root->p),root->f);

	if(root->f[0] != ')') {
		root->n1 = parse();
		root->n2 = parse();
		scanf(" ) ");
	} else {
		root->f[0] = 0;
	}
	return root;
}

double decide(node *root, int fc, char fl[][90]) {
	double p = root->p;
	if( root->f[0] != 0 ) {
		int x;
		for(x=0;x<fc;x++){
			if( strcmp(root->f,fl[x]) == 0 ) {
				p *= decide(root->n1,fc,fl);
				break;
			}
		}
		if( x >= fc ) {
			p *= decide(root->n2,fc,fl);
		}
	}
	return p;
}

int main() {
	setbuf(stdout,0);

	int N;
	scanf("%d",&N);

	for( int n=0; n<N; n++ ) {
		int L;
		scanf("%d ",&L);

		node *root = parse();

		printf("Case #%d:\n",n+1);

		int A;
		scanf("%d ",&A);
		for(int a=0;a<A;a++) {
			char buf[90];
			int fc;
			scanf("%s %d",buf,&fc);

			char fl[100][90];
			for(int x=0;x<fc;x++) {
				scanf("%s",fl[x]);
			}

			printf("%lf\n",decide(root,fc,fl));
		}
	}

	return 0;
}

