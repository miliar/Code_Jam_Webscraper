/**********************************************************************
Author: littlekid@whu
Created Time:  2009-9-13 0:46:51
File Name: 
Description: 
**********************************************************************/
#include <iostream>
#include <vector>
#include <cctype>
using namespace std;

typedef struct node_t {
	double p;
	node_t *lc, *rc;
	char pw[15];	
};

node_t root;
char features[88][15];

void make_tree(node_t *now, int lines) {
	char str[111], ch;
//	cout << " in" << endl;///
	ch = ' ';
	while (ch != '(') {
		scanf("%c", &ch);
	}
	scanf("%lf", &now->p);
//	cout << now->p << endl;///
	ch = ' ';
	while (isspace(ch)) {
		scanf("%c", &ch);	
	}
	if (ch == ')') {
		now->lc = now->rc = NULL;
	} else {
		now->lc = new node_t;
		now->rc = new node_t;
		int pos = 0;
		while (!isspace(ch)) {
			now->pw[pos++] = ch;
			scanf("%c", &ch);
		}
		now->pw[pos] = '\0';
//		printf("--%s--\n", now->pw);///
		make_tree(now->lc, lines);
		make_tree(now->rc, lines);
		ch = ' ';
		while (ch != ')') {
			scanf("%c", &ch);
		}
	}
//	cout << " out " << endl;///
}

double dfs(node_t *now, int cur, int up) {
	if (now == NULL) {
		return 1;	
	}
	double res = now->p;
	bool flag = false;
	for (int ix = 0; ix < up; ++ix) {
		if (strcmp(features[ix], now->pw) == 0) {
			flag = true;
			break;
		} 
	}
//	cout << flag << endl;///
	if (flag) {
		res *= dfs(now->lc, cur+1, up);	
	} else {
		res *= dfs(now->rc, cur+1, up);
	}
	return res;
}

int main() 
{
	//freopen("F:\\ACM\\gcj2009\\R1B\\A.in", "r", stdin);
	freopen("F:\\ACM\\gcj2009\\R1B\\A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ++ca) {
		int L, A;
		scanf("%d\n", &L);
		make_tree(&root, L);
		scanf("%d", &A);
		printf("Case #%d:\n", ca);
		char name[15];
		for (int q = 0; q < A; ++q) {
			scanf("%s", name);
			int m;
			scanf("%d", &m);
			for (int ix = 0; ix < m; ++ix) {
				scanf("%s", features[ix]);	
//				cout << features[ix] << endl;///
			}
			printf("%.7lf\n", dfs(&root, 0, m));
		}
	}
    return 0;
}

