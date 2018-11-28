#include <iostream>
#include <cstring>

#define MAXL 64
#define MAXQ (MAXL*(26+2) + 10)

using namespace std;

struct node {
	struct node * next[26];
	node (void) {
		memset(next, 0, sizeof(next));
	}
};
struct node root;

int l;
char query[MAXQ];

int solve(int id, int len, struct node * n)
{
	if (n == NULL)
		return 0;
	if (len == l)
		return 1;

	if (query[id] != '(')
		return solve(id+1, len+1, n -> next[query[id]-'a']);

	int end = id+1;

	while (query[end] != ')')
		end ++;

	int ret = 0;
	for (int i = id+1; i < end; i++)
		ret += solve(end+1, len+1, n -> next[query[i]-'a']);

	return ret;
}

int main(int argc, char ** argv)
{
	int d, n;

	memset(root.next, 0, sizeof(root.next));

	scanf("%d %d %d", &l, &d, &n);

	for (int i = 0; i < d; i++) {
		struct node * n = &root;

		for (int j = 0; j < l; j++) {
			char c;

			scanf(" %c", &c);

			if (n -> next[c-'a'] == NULL)
				n -> next[c-'a'] = new node();
			n = n -> next[c-'a'];
		}
	}

	for (int i = 0; i < n; i++) {
		scanf(" %s", query);
		printf("Case #%d: %d\n", i+1, solve(0, 0, &root));
	}

	return 0;
}
