#include <stdio.h>
#include <vector>
#include <string>
#include <set>

using namespace std;

struct s_tree {
	bool leaf;
	int left, right;
	double percentage;
	string feature;
};
typedef struct s_tree tree;

tree trees[10000];

char buffer[100000];
char buffer2[100000];
int numTrees;
int actPos;

set<string> animalFeatures;

double
comp(int curTree, double curP)
{
	curP *= trees[curTree].percentage;
	
	if (trees[curTree].leaf) {
		return curP;
	}

	if (animalFeatures.find(trees[curTree].feature) != animalFeatures.end()) {
		return comp(trees[curTree].left, curP);
	} else {
		return comp(trees[curTree].right, curP);
	}
}

int
getTree()
{
	while (buffer[actPos] != '(') {
		actPos++;
	}
	actPos++;
	while (buffer[actPos] == ' ' || buffer[actPos] == '\t') {
		actPos++;
	}
	int curTree = numTrees;
	numTrees++;
	trees[curTree].leaf = false;
	sscanf(buffer + actPos, "%lf", &trees[curTree].percentage);

	while (buffer[actPos] != ' ' && buffer[actPos] != '\t' && buffer[actPos] != ')') {
		actPos++;
	}
	while (buffer[actPos] == ' ' || buffer[actPos] == '\t') {
		actPos++;
	}
	if (buffer[actPos] == ')') {
		actPos++;
		trees[curTree].leaf = true;
		return curTree;
	}
	while (buffer[actPos] == ' ' || buffer[actPos] == '\t') {
		actPos++;
	}
	char featBuf[1024];
	sscanf(buffer + actPos, "%s", featBuf);
	trees[curTree].feature = string(featBuf);

	while (buffer[actPos] != ' ' && buffer[actPos] != '\t' && buffer[actPos] != ')') {
		actPos++;
	}
	trees[curTree].left = getTree();
	trees[curTree].right = getTree();

	while (buffer[actPos] != ')') {
		actPos++;
	}
	actPos++;

	return curTree;
}

const char *whitespace = " ";

int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);

	for (int i = 0; i < numCases; i++) {
		int numLines = 0;
		scanf("%d", &numLines);
		buffer[0] = '\0';
		char tmp[1024];
		fgets(tmp, sizeof(tmp), stdin);
		
		for (int j = 0; j < numLines; j++) {
			fgets(tmp, sizeof(tmp), stdin);
			if (tmp[strlen(tmp) - 1] == '\n') {
				tmp[strlen(tmp) - 1] = '\0';
			}
			strcat(buffer, whitespace);
			strcat(buffer, tmp);
		}
		strcpy(buffer2, buffer);
		int p = 0;
		for (int j = 0; j < strlen(buffer2); j++) {
			if (buffer2[j] == ')' || buffer2[j] == '(') {
				buffer[p] = ' ';
				p++;
				buffer[p] = buffer2[j];
				p++;
				buffer[p] = ' ';
				p++;
			} else {
				buffer[p] = buffer2[j];
				p++;
			}
		}
		buffer[p] = '\0';
		numTrees = 0;
		actPos = 0;
		int root = getTree();

		printf("Case #%d:\n", i + 1);

		int numAnimals;
		scanf("%d", &numAnimals);
		for (int j = 0; j < numAnimals; j++) {
			char bluber[1000];
			scanf("%s", bluber);
			animalFeatures.clear();
			int numFeatures;
			scanf("%d", &numFeatures);
			for (int k = 0; k < numFeatures; k++) {
				char blub[1000];
				scanf("%s", blub);
				string tmpString(blub);
				animalFeatures.insert(tmpString);
			}

			double ret = comp(root, 1.0);
			
			printf("%12.12lf\n", ret);
		}
		
	}

	return 0;
}
