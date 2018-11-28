#include <cstdio>
#include <cstring>

class node {
public:
	node() {
		for (int i=0; i<26; ++i)
			child[i] = NULL;
	}
	~node() {
		for (int i=0; i<26; ++i)
			delete child[i];
	}
	node* child[26];
};

node* root;
int temp[15][26];

int getAns(int *str, node* dic, int L)
{
	if (L <= 0)
		return 1;
	int ans = 0;
	for (int k=0; k<26; ++k) {
		if (str[k]) {
			if (dic->child[k])
				ans += getAns(str+26, dic->child[k], L-1);
		}
	}
	return ans;
}

int main()
{
	int L, D, N;
	root = new node;
	scanf("%d %d %d", &L, &D, &N);
	getchar();
	for (int i=0; i<D; ++i) {
		node *current = root;
		for (int j=0; j<L; ++j) {
			char c = getchar();
			if (c<'a' || c>'z') {
				printf("error\n");
				break;
			}
			c -= 'a';
			if (!(current->child[c]))
				current->child[c] = new node;
			current = current->child[c];
		}
		getchar();
	}
	for (int i=1; i<=N; ++i) {
		memset(temp, 0, sizeof(temp));
		for (int j=0; j<L; ++j) {
			char c = getchar();
			if (c=='(') {
				while (c=getchar(), c!=')') {
					temp[j][c-'a'] = 1;
				}
			} else {
				temp[j][c-'a'] = 1;
			}
		}
		getchar();
		printf("Case #%d: ", i);
		int ans = getAns((int*)temp, root, L);
		printf("%d\n", ans);
	}
	delete root;
	return 0;
}

