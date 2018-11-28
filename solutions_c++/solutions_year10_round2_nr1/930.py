#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <conio.h>
using namespace std;

class node
{
public:
	string name;
	vector<node*> children;
};

void eval_existing(node* root, string path)
{
	string::size_type pos = 1;
	string folder;
	node* current = root;
	while(path.find_first_of('/', pos) != string::npos)
	{
		string::size_type new_pos = path.find_first_of('/', pos);
		folder = path.substr(pos, (new_pos) - pos);
		pos = new_pos + 1;

		bool found = false;
		for(int i = 0; i < current->children.size(); ++i)
		{
			if(folder == current->children[i]->name)
			{
				current = current->children[i];
				found = true;
				break;
			}
		}
		if(!found)
		{
			node* new_node = new node();
			new_node->name = folder;
			current->children.push_back(new_node);
			current = new_node;
		}
	}
	folder = path.substr(pos);
	bool found = false;
	for(int i = 0; i < current->children.size(); ++i)
	{
		if(folder == current->children[i]->name)
		{
			current = current->children[i];
			found = true;
			break;
		}
	}
	if(!found)
	{
		node* new_node = new node();
		new_node->name = folder;
		current->children.push_back(new_node);
		current = new_node;
	}
	return;
}
int eval_new(node* root, string path)
{
	int mkdir = 0;
	string::size_type pos = 1;
	string folder;
	node* current = root;
	while(path.find_first_of('/', pos) != string::npos)
	{
		string::size_type new_pos = path.find_first_of('/', pos);
		folder = path.substr(pos, (new_pos) - pos);
		pos = new_pos + 1;

		bool found = false;
		for(int i = 0; i < current->children.size(); ++i)
		{
			if(folder == current->children[i]->name)
			{
				current = current->children[i];
				found = true;
				break;
			}
		}
		if(!found)
		{
			node* new_node = new node();
			new_node->name = folder;
			current->children.push_back(new_node);
			current = new_node;
			mkdir++;
		}
	}
	folder = path.substr(pos);
	bool found = false;
	for(int i = 0; i < current->children.size(); ++i)
	{
		if(folder == current->children[i]->name)
		{
			current = current->children[i];
			found = true;
			break;
		}
	}
	if(!found)
	{
		node* new_node = new node();
		new_node->name = folder;
		current->children.push_back(new_node);
		current = new_node;
		mkdir++;
	}
	return mkdir;
}
int main()
{
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");

	int cases = 0;
	cin >> cases;
	for(int i = 0; i < cases; ++i)
	{
		node* root = new node();
		int n = 0, m = 0;
		cin >> n >> m;
		int mkdir = 0;

		for(int j = 0; j < n; ++j)
		{
			string dir;
			cin >> dir;
			eval_existing(root, dir);
		}
		for(int j = 0; j < m; ++j)
		{
			string dir;
			cin >> dir;
			mkdir += eval_new(root, dir);
		}
		cout << "Case #" << i + 1 << ": " << mkdir << endl;
	}
	return 0;
}