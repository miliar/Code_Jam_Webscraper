#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
using namespace std;

struct node
{
	vector<node*> children;
	string name;
	void clean()
	{
		for(int i = 0; i < children.size(); ++i)
		{
			children[i]->clean();
			delete children[i];
		}
	}
};

node* root;
char name[1024];

int process(string name, node* nod, int pos)
{
	size_t s = name.find('/', pos);
	string dirname = name.substr(pos, s - pos);
	node* next = NULL;
	for(int i = 0; i < nod->children.size(); ++i)
		if(nod->children[i]->name == dirname)
		{
			next = nod->children[i];
		}
	int res = 0;
	if(next == NULL)
	{
		next = new node;
		next->name = dirname;
		nod->children.push_back(next);
		res = 1;
	}
	if(s != string::npos)
		res += process(name, next, s + 1);
	return res;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large-output.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for(int test = 1; test <= T; ++test)
	{
		int N, M;
		root = new node;
		scanf("%d %d", &N, &M);
		for(int i = 0; i < N; ++i)
		{
			scanf("%s", name);
			process(name, root, 1);
		}
		int res = 0;
		for(int i = 0; i < M; ++i)
		{
			scanf("%s", name);
			res += process(name, root, 1);
		}
		root->clean();
		root = NULL;
		printf("Case #%d: %d\n", test, res);
	}

	return 0;
}