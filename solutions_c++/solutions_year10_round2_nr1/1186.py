#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string.h>
using namespace std;

typedef struct node Node;

struct node {
	char path[128];
	vector<Node> sons;
};

typedef struct tree Tree;

struct tree {
	Node root;
};

int t;
char buffer[256];
int paths;
int exist, create;
char* tok;
Node* iter;

void printTree(Node* a) {
	printf("%s\n", a->path);
	
	for (int i=0; i<a->sons.size(); i++)
		printTree(&a->sons[i]);
}

int main() {
	scanf("%d", &t);
	freopen("a.out", "w", stdout);

	for (int it=0; it<t; it++) {	
		Tree dirTree;
		paths=0;		

		strcpy(dirTree.root.path, "");
		
		scanf("%d %d", &exist, &create);
		
		while (exist--) {
			scanf(" %s", buffer);

			tok = strtok(buffer, "/");
			iter = &dirTree.root;

			while (tok != NULL) {
				int i;
				int size = iter->sons.size();

				for (i=0; i<size; i++) {
					if (!strcmp(tok, iter->sons[i].path)) {
						iter = &iter->sons[i];
						break;
					}
				}

				if (i == size) {
					Node a;
					strcpy(a.path, tok);
					iter->sons.push_back(a);
					iter = &iter->sons[size];
				}

				tok = strtok(NULL, "/");
			}		
		}

		while (create--) {
			scanf(" %s", buffer);

			tok = strtok(buffer, "/");
			iter = &dirTree.root;

			while (tok != NULL) {
				int i;
				int size = iter->sons.size();

				for (i=0; i<size; i++) {
					if (!strcmp(tok, iter->sons[i].path)) {
						iter = &iter->sons[i];
						break;
					}
				}

				if (i == size) {
					Node a;
					strcpy(a.path, tok);
					iter->sons.push_back(a);
					iter = &iter->sons[size];
					paths++;
				}

				tok = strtok(NULL, "/");
			}
		}

		printf("Case #%d: %d\n", it+1, paths);
	}
}
