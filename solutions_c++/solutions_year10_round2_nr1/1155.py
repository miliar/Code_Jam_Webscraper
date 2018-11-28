//============================================================================
// Name        : codejam_1Ba.cpp
// Author      : Ivan Sovic
// Version     :
// Copyright   : Copyright Ivan Sovic, 2010.
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

vector<unsigned long int> results;

class Node
{
public:
	string name;
	vector<Node *> child;

	Node()
	{
		name.clear();
		child.clear();
	}

	void print()
	{
		printf ("/%s", name.c_str());
	}
};

int treeRecursion(Node *currentNode, string parent)
{
//	if (currentNode->name == name)
//		return 1;

	string newParent;

	newParent = parent + "/" + currentNode->name;

	printf ("%s\n", newParent.c_str());

	for (unsigned int i=0; i<currentNode->child.size(); i++)
	{
		treeRecursion(currentNode->child[i], newParent);
	}

	return 0;
}



vector<string> splitPath(string newPath)
{
	string tempString;
	vector<string> ret;

//	printf ("newPath = '%s'\n", newPath.c_str());

	tempString = "";
	for (unsigned int i=0; i<newPath.size(); i++)
	{
		if (newPath[i] == '/')
		{
			if (i > 0)
			{
				ret.push_back(tempString);
				tempString = "";
			}
		}
		else
			tempString += newPath[i];
	}

	if (tempString.size() > 0)
		ret.push_back(tempString);

/*
	for (unsigned int i=0; i<ret.size(); i++)
	{
		printf ("-> %s\n", ret[i].c_str());
	}
*/

	return ret;
}

unsigned long int addPathRecursion(Node *currentNode, vector<string>& split, unsigned long int currentSplit)
{
	bool pathFound=false;
	unsigned long int ret=0;
	Node *newNode;

	if (currentSplit >= split.size())
		return 0;

	pathFound = false;
	for (unsigned int i=0; i<currentNode->child.size(); i++)
	{
		if (currentNode->child[i]->name == split[currentSplit])
		{
			ret = addPathRecursion(currentNode->child[i], split, (currentSplit+1));
			pathFound = true;
			break;
		}
	}

	if (pathFound == false)
	{
		newNode = new Node;
		newNode->name = split[currentSplit];

		currentNode->child.push_back(newNode);
		ret = addPathRecursion(currentNode->child[(currentNode->child.size()-1)], split, (currentSplit+1));
		ret += 1;
	}

	return ret;
}

unsigned long int addPath(Node *rootNode, string newPath)
{
	unsigned long int ret=0;
	vector<string> split;

	split = splitPath(newPath);

	ret = addPathRecursion(rootNode, split, 0);

	return ret;
}

void readInput()
{
	char existingPath[200], newPath[200];
	int i=0, j=0;
	int t=0;
	int n=0, m=0;
	unsigned long int numMake=0;
	Node homeNode;
	Node tempNode;



	scanf("%d", &t);

	for (i=0; i<t; i++)
	{
		scanf ("%d %d", &n, &m);

		homeNode.name = "";
		homeNode.child.clear();

		for (j=0; j<n; j++)
		{
			cin >> existingPath;

			addPath(&homeNode, existingPath);
//			printf ("--> Tu sam!\n");
		}

		tempNode = homeNode;
		numMake = 0;

		for (j=0; j<m; j++)
		{
			cin >> newPath;

			numMake += addPath(&tempNode, newPath);
		}

		results.push_back(numMake);
//		treeRecursion(&tempNode, "");
	}
}

void outputResults()
{
	for (unsigned int i=0; i<results.size(); i++)
	{
		printf ("Case #%d: %lu\n", (i+1), results[i]);
	}
}

int main()
{

/*
	Node test;
	Node test2;
	Node *noviNode;

	test.name = "home";

	noviNode = new Node;	noviNode->name = "test1";
	test.child.push_back(noviNode);
	noviNode = new Node;	noviNode->name = "test2";
	test.child.push_back(noviNode);
	noviNode = new Node;	noviNode->name = "test3";
	test.child.push_back(noviNode);

	noviNode = new Node;	noviNode->name = "test1";
	test.child[0]->child.push_back(noviNode);

	test2 = test;
	noviNode = new Node;	noviNode->name = "test4";
	test2.child.push_back(noviNode);

	treeRecursion(&test, "");
	printf ("\n");
	treeRecursion(&test2, "");
*/

//	splitPath("home/test1/test2/test3");



	readInput();
	outputResults();

	return 0;
}
