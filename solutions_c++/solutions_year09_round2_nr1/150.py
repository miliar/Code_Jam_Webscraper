#include <cstdio>
#include <set>
#include <vector>
#include <string>

using namespace std;

typedef struct{
	string cl;
	double p;
	int yes, no;
}tnode;

vector<tnode> tree;

void ReadTree()
{
	tnode n;

	char c;
	scanf(" %c", &c);

	double p;
	scanf("%lf", &n.p);

	scanf(" %c", &c);
	if( c == ')' )
	{
		tree.push_back(n);
		return;
	}

	char auxS[100];
	int i = 0;
	while( c >= 'a' && c <= 'z' )
	{
		auxS[i++] = c;
		scanf("%c", &c);
	}

	auxS[i] = 0;
	n.cl = auxS;
	n.yes = tree.size() + 1;
	tree.push_back(n);	

	ReadTree();
	tree[n.yes - 1].no = tree.size();
	ReadTree();

	scanf(" %c", &c);
}

double Evaluate(set<string> &s, double p, int x)
{
	p *= tree[x].p;

	if( tree[x].cl.size() == 0 )
	{
		return p;
	}

	if( s.find( tree[x].cl ) != s.end() )
	{
		return Evaluate(s, p, tree[x].yes);
	}
	else
	{
		return Evaluate(s, p, tree[x].no);
	}
}

int main()
{
	int K;
	scanf("%d", &K);
	for(int k = 1; k <= K; k++)
	{
		printf("Case #%d:\n", k);
		tree.clear();

		int L;
		scanf("%d", &L);
		ReadTree();

		scanf("%d", &L);
		for(int i = 0; i < L; i++)
		{
			int n;
			set<string> s;
			scanf("%*s %d", &n);
			for(int j = 0; j < n; j++)
			{
				char auxS[100];
				scanf("%s", auxS);
				
				s.insert( auxS );
			}

			printf("%.7lf\n", Evaluate(s, 1, 0));
		}
	}
}