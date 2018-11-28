/* Google Code Jam 2009
 * Round 1B
 * Problem A: Decision Trees
 */

#include <cstdio>
#include <vector>
#include <iostream>
#include <cstring>
#include <cctype>
#include <set>

#define DIRTYDEBUG 0
#define status(...) if (DIRTYDEBUG) fprintf(stderr, __VA_ARGS__)

#define INDENT level * 4, ""

struct tree {
	long double cutep;
	int leaf;
	std::string feature;
	tree *yes, *no;
};

void parsetree(tree *root, int level)
{
	int c;
	static char buff[80];

	root->leaf = 0;

	// Look for opening ( and cuteness probability
	scanf("\n(%Lf", &root->cutep);
	status("Probability %0.6Lf ", root->cutep);

	// Look for closing ) or feature
	while (isblank(c = getchar())) 
		;
	if (c == ')') {
		root->leaf = 1;
		status("for leaf node.\n");
		return;
	}

	buff[0] = c;
	int i;
	for (i = 1; isalpha(c = getchar()); i++) {
		buff[i] = c;
	}
	buff[i] = 0;
	root->feature = buff;
	status("for feature %s.\n", root->feature.c_str());

	//read yes and no subtrees
	root->yes = new tree;
	status("%*sYes path: ", INDENT);
	parsetree(root->yes, level + 1);
	root->no = new tree;
	status("%*sNo path: ", INDENT);
	parsetree(root->no, level + 1);

	//get final )
	scanf("\n");
	getchar();
}

void printtree(tree *root, int level)
{
	printf("%*s%0.6Lf %s\n", 4 * level, "", root->cutep, 
			root->leaf ? "!" : root->feature.c_str());

	if (root->leaf) {
		return;
	}
	printtree(root->yes, level + 1);
	printtree(root->no, level + 1);
}

long double getp(tree *root, std::set< std::string > &features)
{
	long double p = 1.0L;

	while (!root->leaf) {

		p *= root->cutep;

		status("  Cuteness probability is %0.6Lf. Is it %s?", p, root->feature.c_str());

		if (features.count(root->feature)) {
			status(" Yes.\n");
			root = root->yes;
		}
		else {
			status(" No.\n");
			root = root->no;
		}
	}

	status("  Final probability is ");
	return p * root->cutep;
}

int main()
{
	tree root;
	std::set< std::string > features;
	std::string feature;

	int ncases;
	scanf("%d", &ncases);
	for (int ncase = 1; ncase <= ncases; ncase++) {

		// discard number of lines, I don't care about it
		scanf("%*d");

		status("Reading tree...\n");
		parsetree(&root, 0);

		status("Printing tree...\n");
#if DIRTYDEBUG
		printtree(&root, 0);
#endif

		printf("Case #%d:\n", ncase);
		fflush(stdout);

		int nanimals;
		scanf("%d", &nanimals);
		status("Querying %d animals...\n", nanimals);
		while (nanimals--) {
			int nfeatures;
			static char animal[80];
			scanf("%s%d", animal, &nfeatures);
			features.clear();
			status("%s has %d features -->\n", animal, nfeatures);
			while (nfeatures--) {
				std::cin >> feature;
				features.insert(feature);
			}
			printf("%0.7Lf\n", getp(&root, features));
		}
	}
}
