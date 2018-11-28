#include <cstdio>
#include <cstring>

const int MAXS = 30;

class TreeNode {
public:
	TreeNode * children[MAXS];
	
	TreeNode() {
		for (int i = 0; i < MAXS; i++) children[i] = NULL;
	}
	
	~TreeNode(){
		for(int i = 0; i < MAXS; i++) {
			if (children[i]) delete children[i];
		}
	}
};

TreeNode * root;

inline void insert(char * str) {
	int L = (int)strlen(str);
	TreeNode * u = root;
	for (int i = 0; i < L; i++) {
		int ch = str[i] - 'a';
		if (!u->children[ch]) u->children[ch] = new TreeNode();
		u = u->children[ch];
	}
}

TreeNode * bfs[2][80000];
int bfs0[2];
int L, D, N;

inline int calc(char * str) {
	bfs0[0] = 1;
	bfs[0][0] = root;
	int len = (int)strlen(str), pt = 0, step = 0, t1 = 0, t2;
	while (true) {
		if (pt >= len || !bfs0[t1]) break;
		step++;
		t2 = t1 ^ 1;
		bfs0[t2] = 0;
		int end = pt;
		if (str[pt] != '(') end++;
		else {
			pt++;
			while (str[end] != ')') end++;
		}
		for (int o = bfs0[t1] - 1; o >= 0; o--) {
			for (int i = pt; i < end; i++) {
				TreeNode * nxt = bfs[t1][o]->children[(int)str[i] - 'a'];
				if (nxt) bfs[t2][bfs0[t2]++] = nxt;
			}
		}
		if (str[end] == ')') pt = end + 1;
		else pt = end;
		t1 = t2;
	}
	if (step != L) return 0;
	return bfs0[t1];
}

char str[1024];

int main() {
	scanf("%d%d%d", &L, &D, &N);
	root = new TreeNode();
	for (int o = 0; o < D; o++) {
		scanf("%s", str);
		insert(str);
	}
	for (int o = 0; o < N; o++) {
		scanf("%s", str);
		printf("Case #%d: %d\n", o + 1, calc(str));
	}
	return 0;
}
