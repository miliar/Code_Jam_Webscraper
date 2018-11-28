#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define MAX_LEN 100
using namespace std;

struct node {
  string name;
  vector<node*> children;
	node(string _name) : name(_name) {};
};

node* root;

int add_dir(string path)
{
	path += "/";
	int mkdirs = 0;
	node* parent = root;
  int previ = 0;
	string name;
	for (int i = 1; i < path.size(); i++) {
		if (path[i] == '/') {
			name = path.substr(previ + 1, i - previ - 1);

			bool found = false;
			for (int j = 0; j < parent->children.size(); j++) {
				if (parent->children[j]->name.compare(name) == 0) {
					parent = parent->children[j];
					found = true;
					break;
				}
			}

			if (!found) {
				node* newChild = new node(name);
				parent->children.push_back(newChild);
				parent = newChild;
				mkdirs++;
			}

			previ = i;
		}
	}

	return mkdirs;
}

void cleanup(node* parent)
{
  for (int i = 0; i < parent->children.size(); i++)
	{
				cleanup(parent->children[i]);
	}

	delete parent;
}

void testCase(int number)
{
	int N, M;
	int result = 0;

	// input
	scanf("%d %d", &N, &M);
	string line;
	vector<string> paths;
	for (int i = 0; i < N; i++) 
	{
		cin >> line;
		paths.push_back(line);
	}

	sort(paths.begin(), paths.end());
	root = new node("root");

	for (int i = 0; i < N; i++) {	
		add_dir(paths[i]);
	}

	for (int i = 0; i < M; i++) {
		cin >> line;
		result += add_dir(line);
	}
	
  cleanup(root);
	// output
	printf("Case #%d: %d\n", number, result);
}

int main()
{
	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; i++)
	{
		testCase(i+1);
	}

	return 0;
}
