#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <set>

using namespace std;

typedef struct _node
{
	double p;
	string fet;
	int l, r;
	_node(){ l = r = -1; }
}node;

int n, m;
char line[10000];
int par[10000];
int st[100];

vector<node> tree;
set<string> animalfet;

int maketree(int low, int high)
{
	node v;
	while(line[low] != '(') low++;
	while(line[high] != ')') high--;

	char tmp[15] = {0, };
	int i, j = 0;
	while(!(line[low] >= '0' && line[low] <= '9')) low++;
	for(; line[low] != ' ' && line[low] != ')' ; ++low) tmp[j++] = line[low];
	v.p = atof(tmp);

	while(line[low] == ' ') low++;

	if(line[low] == ')')
	{
		// leaf
		tree.push_back(v);
		return (int)tree.size() - 1;
	}

	j = 0;
	for(; line[low] != '('; ++low){ if(line[low] != ' '){tmp[j++] = line[low]; tmp[j] = 0;} }
	v.fet = tmp;
	v.l = maketree(low, par[low]);
	v.r = maketree(par[low] + 1, high - 1);

	tree.push_back(v);

	return (int)tree.size() - 1;
}

void solve(int v, double p)
{
	p *= tree[v].p;
	if( tree[v].l == -1 )
	{
		printf("%.8lf\n", p);
		return;
	}

	if( animalfet.count(tree[v].fet) ) solve(tree[v].l, p);
	else solve(tree[v].r, p);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int r, cs = 0;
	scanf("%d", &r);
	while(r--)
	{
		printf("Case #%d:\n", ++cs);
		int L;
		scanf("%d", &L);
		gets(line);
		char tmp[100];
		for(int i = 0; i < L; ++i)
		{
			gets(tmp);
			strcat(line, tmp);
		}
		n = strlen(line);
		int top = 0;
        for(int i = 0; i < n; ++i)
		{
			if(line[i] == '('){ st[++top] = i;}
			else if(line[i] == ')') par[st[top--]] = i;
		}
		tree.clear();
		int root = maketree(0, n - 1);
        int A;
		scanf("%d", &A);
		while(A--)
		{
			char animal[15] = {0};
			char fet[15] = {0};
			scanf("%s", animal);
			int m;
			scanf("%d", &m);
			animalfet.clear();
			while(m--)
			{
				scanf("%s", fet);
				animalfet.insert(fet);                
			}
			solve(root, 1.0);
		}
	}
	return 0;
}