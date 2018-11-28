//============================================================================
// Name        : round1BQ1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#include <set>
#include <vector>
#include <string.h>
#include <stdlib.h>
using namespace std;

char fileLine[600];

typedef struct {
	string name;
	set<string> features;
} Animal;

vector<Animal*> animalsVector;

typedef struct treeNode TreeNode;

struct treeNode{
	string feature;
	double weight;
	TreeNode *left;
	TreeNode *right;
};

typedef struct {
	TreeNode *root;
} Tree;

double weight;
int lines;

TreeNode *mountTree(FILE *input, TreeNode *root) {
	fgets(fileLine, 600, input);
	char *temp = fileLine;
	int i = 0;
	while(temp[i] != '(' && lines > 0) {
		temp++;
		if(temp[i] == '\n') {
			fgets(fileLine, 600, input);
			temp = fileLine;
			lines--;
		}
	}
	if(lines == 0)
		return root;

	if(temp[i] != '\0') {
		temp++;
		char *temp2 = strtok(temp, " \n()");
		if(temp2 != NULL) {
			root = new TreeNode();
			root->left = NULL;
			root->right = NULL;
			root->weight = atof(temp2);
			temp2 = strtok(NULL, " \n()");
			if(temp2 != NULL && temp2[0] != ')') {
				lines--;
				root->feature = string(temp2);
				root->left = mountTree(input, root->left);
			} else {
				lines--;
				return root;
			}
			root->right = mountTree(input, root->right);
		} else
			lines--;
	} else
		lines--;
	return root;
}

double cute(Animal *a, TreeNode *root) {
	double c = 1;
	set<string>::iterator iter;
	if(root->feature.empty())
		return c*root->weight;
	iter = a->features.find(root->feature);
	if(iter != a->features.end())
		c = c*root->weight*cute(a, root->left);
	else
		c = c*root->weight*cute(a, root->right);
	return c;
}

int main(int argc, char *argv[]) {
	if(argc < 2) {
		printf("No input file\nUsage: ./question1 <input_file_path>\n");
		return -1;
	}
	FILE *input = fopen(argv[1], "r");
	if(!input) {
		printf("Could not open file %s\n", argv[1]);
		return -2;
	}
	FILE *output = fopen("A-large1.out", "w");
	if(!output) {
		printf("Could not open output file\n");
		return -3;
	}
	int testCases;
	int currentTest = 1;
	int decisionTreeLength;
	int numberOfFeatures;
	int animals;
	int i;
	int features;
	char *temp;
	int j;
	fscanf(input, "%d\n", &testCases);
	while(testCases > 0) {
		testCases--;
		fscanf(input, "%d\n", &decisionTreeLength);
		lines = decisionTreeLength;
		TreeNode *node = NULL;
		node = mountTree(input, node);
		while(lines > 0) {
			fgets(fileLine, 600, input);
			lines--;
		}
		fscanf(input, "%d\n", &animals);
		i = 0;
		while(i < animals) {
			fgets(fileLine, 600, input);
			temp = strtok(fileLine, " \n");
			Animal *a = new Animal();
			a->name = string(temp);
			temp = strtok(NULL, " \n");
			features = atoi(temp);
			i++;
			j = 0;
			while(j < features) {
				temp = strtok(NULL, " \n");
				a->features.insert(string(temp));
				j++;
			}
			animalsVector.push_back(a);
		}
		vector<Animal*>::iterator iter;
		fprintf(output, "Case #%d:\n", currentTest);
		for(iter = animalsVector.begin(); iter != animalsVector.end(); iter++) {
			Animal *b = (*iter);
			double ccc = cute(b, node);
			fprintf(output, "%f\n", ccc);
		}
		animalsVector.clear();
		currentTest++;
	}
	fclose(input);
	fclose(output);
	return 0;
}
