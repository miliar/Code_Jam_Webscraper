#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef struct NODE
{
	double weight;
	string name;
	NODE * left;
	NODE * right;
} NODE;

void DeleteTree(NODE * pRoot)
{
	if (NULL != pRoot->left)
		DeleteTree(pRoot->left);
	if (NULL != pRoot->right)
		DeleteTree(pRoot->right);
	delete pRoot;
}

void GetWeight(const char * pTreeLine, int & treeLineIndex, double & weight)
{
	char   l;
	bool   decimalPoint = false;
	bool   started      = false;
	double fraction     = 10.0;

	weight = 0.0;

	while (pTreeLine[treeLineIndex] != '\0')
	{
		l = pTreeLine[treeLineIndex++];

		if ('.' == l)
		{
			decimalPoint = true;
			started = true;
			continue;
		}

		if ('0' <= l && '9' >= l)
		{
			started = true;

			if (true == decimalPoint)
			{
				weight   += (l - '0') / fraction;
				fraction *= 10.0;
				continue;
			}

			weight *= 10.0;
			weight += l - '0';
			continue;
		}
		else
		{
			if (started)
				return;
		}
	}
}

void BuildTree(NODE * pRoot, const string & tree, int & treeIndex)
{
	enum
	{
		CLOSE_PAREN,
		FEATURE,
		LEFT_TREE,
		OPEN_PAREN,
		RIGHT_TREE,
		WEIGHT,
	};

	char   l;
	int    state = OPEN_PAREN;
	NODE * pNewNode;


	while (treeIndex < tree.length())
	{
		l = tree[treeIndex];

		switch (state)
		{
			case CLOSE_PAREN:
				treeIndex++;
				if (')' == l)
					return;
				break;

			case FEATURE:
				if (')' == l)
					return;

				if ('a' <= l && 'z' >= l)
				{
					pRoot->name += l;
					treeIndex++;
				}
				else
				{
					treeIndex++;
					if (pRoot->name.length())
					{
						if ('(' == l)
						{
							treeIndex--;
							state = LEFT_TREE;
						}
					}
				}
				break;

			case LEFT_TREE:
				pNewNode = new NODE;
				pNewNode->left = NULL;
				pNewNode->right = NULL;
				pRoot->left = pNewNode;
				BuildTree(pNewNode, tree, treeIndex);

				state = RIGHT_TREE;
				break;

			case OPEN_PAREN:
				if ('(' != l)
				{
					treeIndex++;
					continue;
				}

				state = WEIGHT;
				treeIndex++;
				break;

			case RIGHT_TREE:
				pNewNode = new NODE;
				pRoot->right = pNewNode;
				pNewNode->left = NULL;
				pNewNode->right = NULL;
				BuildTree(pNewNode, tree, treeIndex);

				state = CLOSE_PAREN;
				break;

			case WEIGHT:
				if (('0' <= l && '9' >= l) || '.' == l)
				{
					GetWeight(tree.c_str(), treeIndex, pRoot->weight);
					treeIndex--;
					state = FEATURE;
				}
				else
					treeIndex++;
				break;
			}
		}
}

int main()
{
	char outputLine[64];
	char     animalLine[1024];
	char     treeLine[256];
	double   weight;
	ifstream input;
	int      animalFeatures;
	int      animalLines      = 0;
	int      animalLinesIndex = 0;
	int      testCaseIndex    = 0;
	int      testCases        = 0;
	int      treeLineIndex    = 0;
	int      treeLines        = 0;
	int      treeLinesIndex   = 0;
	int      treeLineLength   = 0;
	NODE     *pNode;
	NODE     *pRoot;
	ofstream output;
	string   tree;
	vector <string> features;

	//
	//  Open the input file.
	//
	input.open("A-large.in", ios_base::in);
	if (false == input.is_open())
	{
		printf("Error opening the input file.");
		goto exit;
	}

	//
	//  Open the output file.
	//
	output.open("A-large.out", ios_base::out);
	if (false == output.is_open())
	{
		printf("Error opening the output file.");
		goto exit;
	}

	//
	//  Get the number of test cases.
	//
	input >> testCases;
	for (testCaseIndex = 0; testCaseIndex < testCases; testCaseIndex++)
	{
		input >> treeLines;
		tree = "";
		for (treeLinesIndex = 0; treeLinesIndex < treeLines; treeLinesIndex++)
		{
			//
			//  Read the next line.
			//
			memset(treeLine, 0, sizeof (treeLine));
			input.getline(treeLine, sizeof (treeLine));
			treeLineLength = strlen(treeLine);

			//
			//  First read will likely be an empty string.
			//
			if (0 == treeLineLength)
			{
				treeLinesIndex--;
				continue;
			}
			else
			{
				tree += treeLine;
				tree += "";
				continue;
			}
		}

		pRoot = new NODE;
		pRoot->left = NULL;
		pRoot->right = NULL;
		int treeIndex = 0;
		BuildTree(pRoot, tree, treeIndex);

		sprintf(outputLine, "Case #%d:\n", testCaseIndex + 1);
		output << outputLine;

		input >> animalLines;
		for (animalLinesIndex = 0; animalLinesIndex < animalLines; animalLinesIndex++)
		{
			//  Skip the name.
			input >> animalLine;

			weight = 1.0;
			pNode  = pRoot;
			features.erase(features.begin(), features.end());
			for (input >> animalFeatures; animalFeatures > 0; animalFeatures--)
			{
				input >> animalLine;
				features.push_back(animalLine);
			}

			while (NULL != pNode)
			{
				weight *= pNode->weight;
				int i;
				for (i = 0; i < features.size(); i++)
				{
					if (features[i] == pNode->name)
					{
						pNode = pNode->left;
						break;
					}
				}
				if (i >= features.size())
					pNode = pNode->right;
			}

			sprintf(outputLine, "%0.7f\n", weight);
			output << outputLine;
		}

		DeleteTree(pRoot);
	}

	exit : ;

	if (input.is_open())
		input.close();

	if (output.is_open())
		output.close();

	return 0;
}
