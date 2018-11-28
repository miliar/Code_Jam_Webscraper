#include <cstdio>
#include <cstdlib>

#define MAXL 15
#define MAXD 5000
#define MAXN 500
#define MAXA 26

int l,d,n;

struct tree {
	char label;
	tree *son, *sibling;
	tree() {
		son = NULL; sibling = NULL;
		label = 0;
	}
	long long sum(char pattern[MAXL][MAXA+1], int level) {
		if(level == l)
			return 1;
		long long ret = 0;
		for(int i = 0; pattern[level][i] != 0; i++) {
			for(tree *j = son; j != NULL; j = j->sibling) {
				if(j->label == pattern[level][i])
					ret += j->sum(pattern, level+1);
			}
		}
		return ret;
	}
	
} root;

int main() {
	scanf("%d%d%d\n", &l, &d, &n);
	char buf[MAXL+1];
	
	// input dict
	for(int i = 0; i < d; i++) {
		scanf("%s\n", buf);
		tree *cur = &root;
		for(int j = 0; j < l; j++) {
			if(cur->son == NULL) {
				tree *tmp = new tree();
				tmp->label = buf[j];
				cur->son = tmp; cur = tmp;
			} else {
				for(cur = cur->son; ; cur = cur->sibling) {
					if(cur == NULL) {
						printf("PANIC!\n");
						exit(1);
					}
					if(cur->label == buf[j])
						break;
					if(cur->sibling == NULL) {
						tree *tmp = new tree();
						cur->sibling = tmp;
						tmp->label = buf[j];
						cur = tmp;
						break;
					}
				}
			}
		}
	}
	
	// input testcases.
	char pattern[MAXL][MAXA+1];
	for(int i = 0; i < n; i++) {
		char b;
		for(int j = 0; j < l; j++) {
			scanf("%c", &b);
			if(b == '(') {
				for(int k = 0; ; k++) {
					scanf("%c", &b);
					if(b == ')') { 
						pattern[j][k] = 0;
						break;
					} else
						pattern[j][k] = b;
				}
			} else {
				pattern[j][0] = b;
				pattern[j][1] = 0;
			}
		}
		scanf("\n");
		long long ret = root.sum(pattern, 0);
		printf("Case #%d: %lld\n", i+1, ret);
	}
	
}