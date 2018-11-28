#include <cstdio>
#include <string>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

struct Node {
	Node *next[32];
	Node() {
		for (int i = 0; i < 32; ++i) next[i] = NULL;
	}
};

char res[1024000];
vector<string> vs;
Node root;
int ccount;
int L;

void insert(char *);
void dfs(Node *, int);

int main(void)
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int D, N;
	int i, j;
	char input[32];
	
	scanf("%d%d%d", &L, &D, &N);
	for (i = 0; i < 32; ++i) root.next[i] = 0;
	for (i = 0; i < D; ++i) {
		scanf("%s", input);
		insert(input);
	}
	for (i = 0; i < N; ++i) {
		scanf("%s", res);
		vs.clear();
		for (char *p = res; *p; ++p) {
			if (*p == '(') {
				vs.push_back(string());
				while (*(++p) != ')') vs.back() += *p;
			}
			else vs.push_back(string(1, *p));
		}
		/*
		vector<string>::iterator vit;
		string::iterator sit;
		for (vit = vs.begin(); vit != vs.end(); ++vit) {
			cout << *vit << endl;
		}
		*/
		ccount = 0;
		dfs(&root, 0);
		printf("Case #%d: %d\n", i+1, ccount);
	}
	
	return 0;
}

void insert(char *str) {
	Node *p = &root;
	
	while (*str) {
		if (p->next[*str - 'a'] == NULL)
			p->next[(*str) - 'a'] = new Node();
		p = p->next[(*str) - 'a'];
		++str;
	}
	//p->IsString = true;
}

void dfs(Node *p, int i) {
	if (p == NULL) return;
	if (i == L) {
		++ccount;
		return;
	}
	
	string::iterator sit;
	
	for (sit = vs[i].begin(); sit != vs[i].end(); ++sit) {
		//printf("%c  %d\n", *sit, i+1);
		dfs(p->next[(*sit) - 'a'], i+1);
	}
}
