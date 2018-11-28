#include <set>
#include <cstdio>
#include <string>
using namespace std;

struct Node
{
	double prob;
	char name[80];
	Node *c[2];
	Node(double prob, char *Name) : prob(prob) {strcpy(name, Name); for(int i = 0; i < 2; ++i) c[i] = NULL;}
	Node() {name[0] = 0; for(int i = 0; i < 2; ++i)c[i] = NULL;}
};

char Name[88];

bool ReadName()
{
	char c = 0;
	/*while(c < 'a' && c > 'z')
		c = getchar();
	ungetc(c, stdin);*/
	int n = 0;
	while(1)
	{
		c = getchar();
		if(c == ')')
			return false;
		if(c >= 'a' && c <= 'z')
			break;
	}
	ungetc(c, stdin);
	while(1)
	{
		c = getchar();
		if(c >= 'a' && c <= 'z')
			Name[n++] = c;
		else
			break;
	}
	Name[n] = 0;
	ungetc(c, stdin);
	return true;
}

Node *Read()
{
	while(getchar() != '(');
	double prob;
	scanf("%lf", &prob);
	if(ReadName())
	{
		Node *ret = new Node(prob, Name);
		for(int i = 0; i < 2; ++i)
			ret->c[i] = Read();
		while(getchar() != ')')
			;
		return ret;
	}
	else
	{
		return new Node(prob, "");
	}

}

set<string> S;

void Solve(int test)
{
	printf("Case #%d:\n", test);
	int L;
	scanf("%d", &L);
	Node *root = Read();
	int n;
	scanf("%d", &n);
	for(int k = 0; k < n; ++k)
	{
		scanf("%s", Name);
		int q;
		scanf("%d", &q);
		S.clear();
		for(int i = 0; i < q; ++i)
		{
			scanf("%s", Name);
			S.insert(Name);
		}
		double ans = 1.0;
		Node *node = root;
		while(node)
		{
			ans *= node->prob;
			if(S.count(node->name))
				node = node->c[0];
			else
				node = node->c[1];
		}
		printf("%.7lf\n", ans);
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
		Solve(i);
	return 0;
}