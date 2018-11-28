#if 1
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <vector>
#include <string>
#include <iostream>
using namespace std;
const int MAXDEPTH = 100;
struct Node 
{
	vector<string> mNames;
	vector<Node *> pNodes;
} *root;
int main()
{
	int t;
	scanf("%d", &t);
	for (int c = 1; c <= t; c++)
	{
		int n, m;
		scanf("%d %d", &n, &m);
		root = new Node;
		for (int i = 0; i < n; i++)
		{
			char exist[300];
			scanf("%s", exist);
			for (int i = 0; exist[i]; i++)
				if (exist[i] == '/') exist[i] = ' ';
			Node *path = root;
			for (char *p = strtok(exist, " "); p; p = strtok(NULL, " "))
			{
				int i;
				for (i = 0; i < path->mNames.size(); i++)
					if (strcmp(p, path->mNames[i].c_str()) == 0) break;
				if (i == path->mNames.size()) {
					path->mNames.push_back(string(p));
					path->pNodes.push_back(new Node);
				}
				path = path->pNodes[i];
			}
		}
		int count = 0;
		for (int i = 0; i < m; i++)
		{
			char exist[300];
			scanf("%s", exist);
			for (int i = 0; exist[i]; i++)
				if (exist[i] == '/') exist[i] = ' ';
			Node *path = root;
			for (char *p = strtok(exist, " "); p; p = strtok(NULL, " "))
			{
				int i;
				for (i = 0; i < path->mNames.size(); i++)
					if (strcmp(p, path->mNames[i].c_str()) == 0) break;
				if (i == path->mNames.size()) {
					count++;
					path->mNames.push_back(string(p));
					path->pNodes.push_back(new Node);
				}
				path = path->pNodes[i];
			}
		}
		printf("Case #%d: %d\n", c, count);
	}
}
#endif