#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <math.h>
#include <string.h>
#include <set>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

#define fi(a, b) for(i=a; i<=b; i++)
#define fj(a, b) for(j=a; j<=b; j++)
#define fo(a, b) for(o=a; o<=b; o++)
#define fdi(a, b) for(i=a; i>=b; i--)
#define fdj(a, b) for(j=a; j>=b; j--)
#define fdo(a, b) for(o=a; o>=b; o--)
#define ZERO(a) memset(a, 0, sizeof(a))
#define COPY(a, b) memcpy(a, b, sizeof(b))

int l, d, n;

#define LEN 2000

struct Node {
	char x;
	int f;
	Node *next[26];
};

Node *root;

char str[LEN];

void Insert(char *s) {
	int i;
	int l;
	char x;
	Node *y;
	Node *temp;
	l = (int)strlen(s);
	y = root;
	fi(0, l - 1) {
		x = s[i] - 'a';
		if (y->next[x] != NULL) {
			y = y->next[x];
		} else {
			temp = new Node;
			temp->x = x;
			temp->f = 0;
			ZERO(temp->next);
			y->next[x] = temp;
			y = temp;
		}
	}
	y->f = 1;
}

int ans;
int len;

void dfs(Node *y, int p) {
	if (y == NULL) return;
	if (y->f == 1) {ans++; return;}
	if (p >= len) return;
	int g;
	char x;
	if (str[p] == '(') {
		g = p;
		while (str[g] != ')') {
			g++;
		}
		g++;
		p++;
		while (str[p] != ')') {
			x = str[p] - 'a';
			dfs(y->next[x], g);
			p++;
		}
	} else {
		x = str[p] - 'a';
		dfs(y->next[x], p + 1);
	}
}

int main() {
	int i;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d %d %d", &l, &d, &n);
	root = new Node;
	root->f = 0;
	ZERO(root->next);
	fi(1, d) {
		scanf("%s", str);
		Insert(str);
	}
	fi(1, n) {
		scanf("%s", str);
		len = (int)strlen(str);
		ans = 0;
		dfs(root, 0);
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}