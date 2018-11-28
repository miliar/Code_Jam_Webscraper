#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
	long double weight;
	char feature[100];
	
	struct Node* hasF;
	struct Node* hasntF;
} Node;

typedef struct Animal {
	char name[100];
	char features[10][100];
	int n;
} Animal;

void printNode(Node *node) {
	return;
	if(node == NULL) {
		printf("\n");
		return;
	}
	printf("W:%Lf F:%s\n", node->weight, node->feature);
	//printf("%s 1:", node->feature);
	//printNode(node->hasF);
	//printf("%s 2:", node->feature);
	//printNode(node->hasntF);
}

Node* parseTree() {
	char c;
	char str[100];
	scanf(" (");
	//if(c != '(') printf("Something wrong... [%c]", c);
	Node *ret = (Node*)malloc(sizeof(Node));
	double a;
	scanf(" %Lf", &ret->weight);
	scanf(" %c", &ret->feature[0]);
	//printf("--- %Lf %c\n", ret->weight, ret->feature[0]);
	printNode(ret);
	if(ret->feature[0] != ')') {
		//if(scanf("%s (", &ret->feature[1]) <= 0) ret->feature[1] = 0;
		//scanf("%s", &ret->feature[1]);
		for(int i = 1; i < 20; i++) {
			scanf(" %c", &ret->feature[i]);
			if(ret->feature[i] == '(') {
				ret->feature[i] = 0;
				break;
			}
		}
		printNode(ret);
		ret->hasF = parseTree();
		ret->hasntF = parseTree();
		scanf(" %c", &c);
		if(c != ')') printf("Something wrong2... [%c]", c);
	} else {
		printNode(ret);
	}
		
	return ret;
}

long double calc(Animal *a, Node *node) {
	if(node->feature[0] == ')') return node->weight;
	for(int i = 0; i < a->n; i++) {
		if(strcmp(a->features[i], node->feature) == 0) {
			return node->weight * calc(a, node->hasF);
		}
	}
	return node->weight * calc(a, node->hasntF);
}

int main() {
	
	int N;
	
	scanf("%d", &N);
	for(int n = 1; n <= N; n++) {
		int L, A;
		Animal animals[15];
		scanf("%d", &L);
		Node *root = parseTree();
		scanf(" %d", &A);
		for(int i = 0; i < A; i++) {
			scanf("%s %d", &animals[i].name, &animals[i].n);
			for(int j = 0; j < animals[i].n; j++) {
				scanf("%s", &animals[i].features[j]);
			}
			//printf("A:%s F:%d\n", animals[i].name, animals[i].n); 
			
		}
		
		printf("Case #%d:\n", n);
		for(int i = 0; i < A; i++) {
			printf("%.7Lf\n", calc(&animals[i], root));
		}
	}
	
	return 0;	
}
