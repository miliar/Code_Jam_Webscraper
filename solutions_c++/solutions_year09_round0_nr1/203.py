#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
struct node
{
	node* child[26];
	node()
	{
		memset(child, 0, sizeof child);
	}
	~node()
	{
		for (int i = 0; i < 26; i++)
			if (child[i])
				delete child[i];
	}
	void add(char* s)
	{
		if (!s[0]) return;

		if (!child[s[0]-'a'])
			child[s[0]-'a'] = new node();
		child[s[0]-'a']->add(s+1);
	}
};

int L, D, N;
char buf[1000];
node* trie;
string rule[20];

int go(node* u, int cur)
{
	if (cur == L) return 1;

	int res = 0;
	for (unsigned i = 0; i != rule[cur].size(); i++)
		if (u->child[rule[cur][i]-'a'])
			res += go(u->child[rule[cur][i]-'a'], cur+1);
	return res;
}


int main()
{
	scanf("%d%d%d", &L, &D, &N);
	trie = new node;
	for (int i = 0; i < D; i++)
	{
		scanf("%s", buf);
		trie->add(buf);
	}
	for (int n = 1; n <= N; n++)
	{
		scanf("%s", buf);
		bool par = false;
		int R = 0;
		for (int i = 0; i < L; i++)
			rule[i] = "";
		for (int i = 0; buf[i]; i++)
		{
			if (buf[i] == '(')
				par = true;
			else if (buf[i] == ')')
			{
				par = false;
				R++;
			}
			else
			{
				rule[R].push_back(buf[i]);
				if (!par)
					R++;
			}
		}
		printf("Case #%d: %d\n", n, go(trie, 0));
	}
}
