#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>
#include <algorithm>

struct btree
{
	double weight;
	char name[16];
	
	struct btree* yes;
	struct btree* no;
};

struct btree* process_tree()
{
	char buf[81];
	
	struct btree* tree = (struct btree*) malloc(sizeof(struct btree));
	tree->yes = NULL; tree->no = NULL; *tree->name = '\0';

	while (getchar() != '(');
	scanf("%lf", &tree->weight);
	
	char c = getchar(); while (isspace(c)) c = getchar();
	if (c == ')') return tree;
	
	ungetc(c, stdin); scanf("%s", buf);
	strcpy(tree->name, buf);
	
	tree->yes = process_tree();
	tree->no = process_tree();
	
	c = getchar(); while (isspace(c)) c = getchar();
	if (c == ')') return tree;
};

void destroy_tree(struct btree* t)
{ if (!t) return; destroy_tree(t->yes); destroy_tree(t->no); free(t); };

bool isbranch(struct btree* t)
{ return t->yes && t->no; };

int main()
{
	int cases; scanf("%d", &cases);
	for (int t = 1; t <= cases; ++t)
	{
		printf("Case #%d:\n", t);
	
		struct btree* tree = process_tree();
		int animals; scanf("%d", &animals);
		
		for (int a = 0; a < animals; ++a)
		{
			int attc; scanf("%*s %d", &attc);
			std::vector<std::string> attrs;
			
			while (attc-- > 0)
			{
				char buf[16]; scanf("%s", buf);
				attrs.push_back(buf);
			};
			
			double res = 1.0;
			struct btree* node = tree;
			
			while (node != NULL)
			{
				res *= node->weight;
				if (!isbranch(node)) break;
				
				std::string thisattr(node->name);
				node = (std::find(attrs.begin(), attrs.end(), thisattr) != attrs.end()) ? node->yes : node->no;
			};
			
			printf("%.7lf\n", res);
		};
		
		destroy_tree(tree);
	};
};
