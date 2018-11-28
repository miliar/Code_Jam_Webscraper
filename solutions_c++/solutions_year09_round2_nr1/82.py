#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define MAX 1024

using namespace std;
FILE *in; FILE *out;

struct Node
{
	double weight;
	string feature;
	Node* left; Node* right;
	
	Node(double weight_ = 0.0, string feature_ = "")
	{
		weight = weight_;
		feature = feature_;
	}
};
Node* root;


int levels, queries;

Node* parseTree(string input)
{
	Node* ret = new Node();
	
//	cout << "Input = " << input << endl;
	
	int idx1 = 0, idx2 = input.size() - 1;
	while (input[idx1] != '(') idx1++; idx1++;
	while (input[idx2] != ')') idx2--; idx2--;
	
	string br1, br2;	
	stringstream ss(input);

	ss >> br1;
	ss >> ret->weight;
	ss >> br2;
	
	if (br2 != ")")
	{
		ret->feature = br2;

//		cout << "Adding node with weight " << ret->weight << " and feature: " << ret->feature << endl;
//		system("pause");

		string next1; int cnt1 = 1;
		while (input[idx1] != '(') idx1++; idx1++; next1 += input[idx1-1];
		while (cnt1 > 0)
		{
			if (input[idx1] == '(') cnt1++;
			if (input[idx1] == ')') cnt1--;
			next1 += input[idx1++];
		}
		
		string next2; int cnt2 = 1;
		while (input[idx1] != '(') idx1++; idx1++; next2 += input[idx1-1];
		while (cnt2 > 0)
		{
			if (input[idx1] == '(') cnt2++;
			if (input[idx1] == ')') cnt2--;
			next2 += input[idx1++];
		}
		
		ret->left = parseTree(next1);
		ret->right = parseTree(next2);		
	}
	/*
	else
	{
		cout << "Adding node with weight " << ret->weight << " and no feature." << endl;
		system("pause");
	}
	*/
	
	return ret;
}

double getVal(Node* node, set <string> chars)
{
	if (node->feature == "")
		return node->weight;
	
	if (chars.find(node->feature) != chars.end())
		return node->weight * getVal(node->left, chars);
	else
		return node->weight * getVal(node->right, chars);
}

void cleanTree(Node* node)
{
	if (node->feature != "")
	{
		cleanTree(node->left);
		cleanTree(node->right);
	}
	delete node;
}

void doWork(int testNum)
{
	char buff[128];

	fscanf(in, "%d", &levels);
	fgets(buff, 128, in);
	
	string input = "";
	for (int i=0; i<levels; i++)
	{
		fgets(buff, 128, in);
		for (int c=0; c<128; c++)
		{
			if (buff[c] == '\n') break;
			input += buff[c];
			if (input[input.size() - 1] == '(') input += ' ';
			if (input[input.size() - 1] == ')') {input[input.size() - 1] = ' '; input += ')';}
		}
	}
//	cout << input << endl;
//	system("pause");
	
	root = parseTree(input);

	fscanf(in, "%d", &queries);
//	cout << "Number of queries: " << queries << endl;
//	system("pause");
	for (int i=0; i<queries; i++)
	{
		fscanf(in, "%s", buff);
		int characteristics;
		set <string> chars;

		fscanf(in, "%d", &characteristics);
		for (int c=0; c<characteristics; c++)
		{
			fscanf(in, "%s", buff);
			chars.insert(buff);
		}
		double ans = getVal(root, chars);
		fprintf(out, "%.7lf\n", ans);
	}
	
	cleanTree(root);
	return;
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("DecisionTree.in", "rt");
	out = fopen("DecisionTree.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++)
	{
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d:\n", test);
		doWork(test);
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n", (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	system("pause");
	return 0;
}
