#define _CRT_SECURE_NO_DEPRECATE

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <string.h>

using namespace std;

#define pb push_back
#define pf push_front
#define mp make_pair
#define fi(a, b) for(i=a; i<=b; i++)
#define fj(a, b) for(j=a; j<=b; j++)
#define fo(a, b) for(o=a; o<=b; o++)
#define fdi(a, b) for(i=a; i>=b; i--)
#define fdj(a, b) for(j=a; j>=b; j--)
#define fdo(a, b) for(o=a; o>=b; o--)
#define ZERO(x) memset(x, 0, sizeof(x));
#define COPY(x, y) memcpy(x, y, sizeof(y));
#define SIZE(x) (int)x.size()
#define LEN(x) (int)x.length()

typedef long long int64;

int n, m;

char str[1000];

struct Node {
	map <string, Node *> next;
};

Node *root;

int ans;

void Create(Node *x, char *s) {
	if (s[0] == 0) return;
	if (s[0] == '/') s++;
	char t[200];
	int i;
	i = 0;
	while (s[i] != '/' && s[i] != 0) {
		t[i] = s[i];
		i++;
	}
	t[i] = 0;
	if (x->next.find(t) == x->next.end()) {
		ans++;
		Node *y;
		y = new Node;
		x->next[t] = y;
		Create(x->next[t], s + i);
	} else {
		Create(x->next[t], s + i);
	}
}

int test;
int testq;

int main() {
	int i;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		printf("Case #%d: ", test);
		scanf("%d %d", &n, &m);
		root = new Node;
		fi(1, n) {
			scanf("%s", str);
			Create(root, str);
		}
		ans = 0;
		fi(1, m) {
			scanf("%s", str);
			Create(root, str);
		}
		printf("%d\n", ans);
	}
	return 0;
}
