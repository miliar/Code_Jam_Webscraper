#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>
#include <set>
#include <string>

using std::set;
using std::string;

typedef set<string> string_set;

struct tree {
	double weight;
	char *feature;
	struct tree *left;
	struct tree *right;
};

struct tree* read_tree(FILE *f) {
	char buf[1000];
	struct tree *tree;
	char *token;

	do {
		if (!fgets(buf, 1000, f))
			exit(1);
		buf[strlen(buf) - 1] = 0;

		token = strtok(buf, " ");
	}
	while (token[0] == ')');

	if (token[0] == '(') {
		tree = (struct tree*)malloc(sizeof(struct tree));

		if (token[1] == 0)
			token = strtok(NULL, " ");
		else
			token = token + 1;

		if (token[strlen(token) - 1] == ')') {
			token[strlen(token) - 1] = 0;
			tree->weight = atof(token);
			tree->feature = NULL;
			tree->left = tree->right = NULL;
		}
		else {
			tree->weight = atof(token);
			token = strtok(NULL, " ");
			if (token == NULL || token[0] == ')') {
				tree->feature = NULL;
				tree->left = tree->right = NULL;
			}
			else {
				tree->feature = strdup(token);
				tree->left = read_tree(f);
				tree->right = read_tree(f);
			}
		}
	}
	else {
		assert(false);
	}

	return tree;
}

void free_tree(struct tree *tree) {
	if (tree->left)
		free(tree->left);
	if (tree->right)
		free(tree->right);
	if (tree->feature)
		free(tree->feature);
	free(tree);
}

void print_tree(struct tree *tree) {
	printf("%f", tree->weight);
	if (tree->feature) {
		printf(" %s\n", tree->feature);
		if (tree->left)
			print_tree(tree->left);
		if (tree->right)
			print_tree(tree->right);
	}
	else
		printf("\n");
}

int main(int argc, char *argv[]) {
	FILE *f;
	unsigned int num_cases;
	char buf[100000];
	char *token;

	f = fopen(argv[1], "r");
	fscanf(f, "%d\n", &num_cases);

	for (int i = 0; i < num_cases; ++i) {
		printf("Case #%d:\n", i+1);

		//read in unnecessary line
		if (!fgets(buf, 100000, f))
			break;
		struct tree *tree;
		tree = read_tree(f);
		//print_tree(tree);

		do {
			if (!fgets(buf, 100000, f))
				break;
			buf[strlen(buf) - 1] = 0;
			token = strtok(buf, " ");
		}
		while (token[0] == ')');

		int num_animals = atoi(token);
		for (int j = 0; j < num_animals; ++j) {
			string_set features;

			if (!fgets(buf, 100000, f))
				break;
			buf[strlen(buf) - 1] = 0;

			token = strtok(buf, " ");
			token = strtok(NULL, " ");
			token = strtok(NULL, " ");

			while (token) {
				features.insert(string(token));
				token = strtok(NULL, " ");
			}

			struct tree *curr_tree = tree;
			double prob = 1;
			do {
				prob *= curr_tree->weight;
				if (!curr_tree->feature) {
					assert(curr_tree->left == NULL);
					assert(curr_tree->right == NULL);
					curr_tree = NULL;
				}
				else { 
					assert(curr_tree->left != NULL);
					assert(curr_tree->right != NULL);
					if (features.find(string(curr_tree->feature)) != features.end())
						curr_tree = curr_tree->left;
					else
						curr_tree = curr_tree->right;
				}
			}
			while (curr_tree);
			printf("%f\n", prob);
		}

		free_tree(tree);
	}
	
	fclose(f);
}
