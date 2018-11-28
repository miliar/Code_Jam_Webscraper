#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>

#define INFILE "A-small-attempt0.in"
#define OUTFILE "A-small-attempt0.out"

using namespace std;

unsigned long long cntMkdir;

typedef struct _node {
	string name;
	vector<struct _node *> pChild;
} node_t;

node_t root;


void add(char *path, bool flag = false) {
	int idx = 1;
	if (path[idx] == 0)
		return;

	int flagEnd = 0;
	node_t *parent = &root;

	while (1) {		
		char token[104];

		int i = 0;
		while (1) {
			if (path[idx] != '/' && path[idx] != 0) {
				token[i] = path[idx];
				idx++;
				i++;
			}
			else if (path[idx] == '/') {
				idx++;
				token[i] = 0;
				break;
			}
			else {
				token[i] = 0;
				flagEnd = 1;
				break;
			}
		}

		string name(token);

		printf("tocken: %s\n",token);
		printf("tocken: %s\n", name.c_str());
		
		vector<struct _node *>::iterator iter;
		for (iter = (parent->pChild).begin(); iter != (parent->pChild).end(); iter++) 
			if ( (*iter)->name == name) 
				break;
		if (iter == (parent->pChild).end()) {
			if (flag == true)
				cntMkdir++;

			node_t *pNodeNew = new node_t;
			pNodeNew->name = name;
			parent->pChild.push_back(pNodeNew);
			parent = pNodeNew;
		}
		else {
			parent = (*iter);
		}

		if (flagEnd)
			break;
	} // while (true)
} 

void del(node_t* pNode) {
	vector<struct _node *>::iterator iter;
	for (iter = (pNode->pChild).begin(); iter != (pNode->pChild).end(); iter++)
		del(*iter);
	delete pNode;
}

int main() {
	FILE *fpIn = freopen(INFILE, "r", stdin);
	if (fpIn == NULL) {
		printf("[main] Fail to call freopen()");
		return -1;
	}
	FILE *fpOut = fopen(OUTFILE, "w");
	if (fpOut == NULL) {
		printf("[main] Fail to call fopen()");
		return -1;
	}

	int T;
	scanf("%d", &T);

	printf("T = %d\n", T); // dbg
	
	for (int cnt1 = 0; cnt1 < T; cnt1++) {
		int N; int M;
		scanf("%d %d", &N, &M);

		printf("N = %d, M = %d\n", N, M); // dbg

		for (int i = 0; i < N; i++) {
			char path[104];
			scanf("%s", path);
			add(path);
		}

		cntMkdir = 0;

		for (int i = 0; i < M; i++) {
			char path[104];
			scanf("%s", path);

			printf("path = %s\n", path);
			add(path, true);
		}

		fprintf(fpOut, "Case #%d: %llu\n", cnt1+1, cntMkdir);

		vector<struct _node *>::iterator iter;
		for (iter = root.pChild.begin(); iter != root.pChild.end(); iter++) 
			del(*iter);

		root.pChild.clear();
	}


	return 0;
}