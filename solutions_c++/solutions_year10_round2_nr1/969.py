//2010 Google Code Jam - Round 1B - A.
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

class TreeNode
{
public:
	string value;
	vector<TreeNode> nextNodes;

	TreeNode(string value)
	{
		this->value = value;
	}
};

vector<string> ParsePath(string path)
{
	vector<string> returnStrVector;
	
	int startIndex = 1;

	for (int i = 1;i < (int)path.length();i++)
	{
		if (path[i] == '/')
		{
			returnStrVector.push_back(path.substr(startIndex, i - startIndex));
			startIndex = i + 1;
		}
	}

	returnStrVector.push_back(path.substr(startIndex));

	return returnStrVector;
}

TreeNode* FindNode(TreeNode* nodePtr, string value)
{
	for (int i = 0;i < (int)nodePtr->nextNodes.size();++i)
	{
		if (nodePtr->nextNodes[i].value == value)
		{
			return &nodePtr->nextNodes[i];
		}
	}

	return NULL;
}

int main()
{
	//Open files
	//ifstream fin("I:\\GoogleCodeJam\\sampleData.in");
	//ifstream fin("I:\\GoogleCodeJam\\A-small-attempt0.in");
	ifstream fin("I:\\GoogleCodeJam\\A-large.in");
	ofstream fout("I:\\GoogleCodeJam\\output.txt");

	if(!fin)
	{    
		cout << "File loading fails." << endl;   
	}

	int cases; 

	fin >> cases;

	//Handle Input
	for (int caseNumber = 1;caseNumber <= cases;++caseNumber)
	{
		int n, m;
		string temp;

		fin >> n >> m;

		vector<string> existPaths;
		vector<string> createdPath;

		//Main algo.
		TreeNode root("");

		for (int i = 0;i < n;i++)
		{
			fin >> temp;
			existPaths.push_back(temp);

			vector<string> parsedPath = ParsePath(temp);
			TreeNode* startNode = &root;

			for (int j = 0;j < (int)parsedPath.size();j++)
			{
				TreeNode* nextNodePtr = FindNode(startNode, parsedPath[j]);

				if (nextNodePtr == NULL)
				{
					TreeNode newNode(parsedPath[j]);
					startNode->nextNodes.push_back(newNode);
					startNode = &startNode->nextNodes[startNode->nextNodes.size() - 1];
				}
				else
				{
					startNode = nextNodePtr;
				}
			}
		}

		int mkdirCounter = 0;

		for (int i = 0;i < m;i++)
		{
			fin >> temp;
			
			vector<string> parsedPath = ParsePath(temp);

			TreeNode* startNode = &root;

			for (int j = 0;j < (int)parsedPath.size();j++)
			{
				TreeNode* nextNodePtr = FindNode(startNode, parsedPath[j]);

				if (nextNodePtr == NULL)
				{
					mkdirCounter ++;

					TreeNode newNode(parsedPath[j]);
					startNode->nextNodes.push_back(newNode);
					startNode = &startNode->nextNodes[startNode->nextNodes.size() - 1];
				}
				else
				{
					startNode = nextNodePtr;
				}
			}
		}

		//Output
		fout << "Case #" << caseNumber << ": " <<  mkdirCounter << endl;
	}
	
	//Close files
	fin.close();   
	fout.close();

	return 0;
}