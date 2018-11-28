#include <iostream>
#include <fstream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <string>
using namespace std;

struct Node {
	string name;
	vector<Node *> nodes;
};
Node * root = new Node();

Node * isExist(Node * root, const char * str)
{
	for (int i = 0; i < root->nodes.size(); ++ i)
	{
		if (strcmp(str, root->nodes[i]->name.c_str()) == 0) return root->nodes[i];
	}
	return NULL;
}

int addNode(Node * root, char * path)
{
	char * token = strtok(path, "/");
	vector<string> dirs;
	while(token != NULL)
	{
		dirs.push_back(token);
		token = strtok(NULL, "/");
	}
	int ret = 0;
	for (int i = 0; i < dirs.size(); ++ i)
	{
		Node * next = isExist(root, dirs[i].c_str());
		if (next == NULL) {
			for (int j = i; j < dirs.size(); ++ j)
			{
				Node * tmp = new Node();
				tmp->name = dirs[j];
				root->nodes.push_back(tmp);
				root = tmp;
				++ ret;
			}
			break;
		}
		root = next;
	}
	return ret;
}

int main()
{
	fstream inputFile("F:/gcj/data1s.in", ios_base::in);
	fstream outputFile("F:/gcj/data1s.out", ios_base::out);

	int n = 0;
	inputFile >> n;
	int caseIndex = 0;
	char buffer[200];
	while (n -- > 0)
	{
		++ caseIndex;
		root->name = "";
		root->nodes.clear();

		int n, m;
		inputFile >> n >> m;

		for (int i = 0; i < n; ++ i)
		{
			inputFile >> buffer;
			addNode(root, buffer);
		}
		int ret = 0;
		for (int i = 0; i < m; ++ i)
		{
			inputFile >> buffer;
			ret += addNode(root, buffer);
		}
		outputFile << "Case #" << caseIndex << ": ";
		outputFile << ret << endl;
	}

	//inputFile.close();
	//outputFile.close();
	return 0;
}