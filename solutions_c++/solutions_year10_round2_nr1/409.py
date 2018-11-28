#include <iostream>
#include <list>
#include <string>

using std::cin;
using std::cout;
using std::endl;

struct treenode
{
	std::string name;
	std::list<treenode*> children;
	bool mark;
	void work(char* c, bool newmark);
	int sum();
	~treenode();
};
void treenode::work(char* c, bool newmark)
{
	std::string tmp = "";
	if(newmark) mark = true;
	char* t;
	for(t = c+1; *t != '/' && *t != '\0'; t++)
	{
		tmp = tmp + *t;
	}
	if(*c == 0) return;
	std::list<treenode*>::iterator it;
	for(it = children.begin(); it != children.end(); it++)
	{
		if(tmp == (*it)->name)
		{
			(*it)->work(t, newmark);
			break;
		}
	}
	if(it == children.end())
	{
		treenode* newnode = new treenode();
		newnode->mark = false;
		newnode->name = tmp;
		children.push_back(newnode);
		newnode->work(t, newmark);
	}
}
int treenode::sum()
{
	int y;
	if(mark) y = 0;
	else y = 1;
	std::list<treenode*>::iterator it;
	for(it = children.begin(); it != children.end(); it++)
	{
		y += (*it)->sum();
	}
	return y;
}
treenode::~treenode()
{
	std::list<treenode*>::iterator it;
	for(it = children.begin(); it != children.end(); it++)
	{
		delete *it;
	}
	children.clear();
}
void work()
{
	treenode* root = new treenode();
	root->mark = true;
	root->name = "wtf";
	int n, m;
	cin >> n >> m;
	std::string tmp;
	char g[200];
	for(int i=0; i<n; i++)
	{
		cin >> tmp;
		for(int j = 0; j<tmp.length(); j++) g[j] = tmp.c_str()[j];
		g[tmp.length()] = '\0';
		root->work(&(g[0]), true);
	}
	for(int i=0; i<m; i++)
	{
		cin >> tmp;
		for(int j = 0; j<tmp.length(); j++) g[j] = tmp.c_str()[j];
		g[tmp.length()] = '\0';
		root->work(&(g[0]), false);
	}
	cout << root->sum() << endl;
	delete root;
}
int main()
{
	int t;
	cin >> t;
	for(int i=1; i<=t; i++)
	{
		cout << "Case #" << i << ": ";
		work();
	}
	return 0;
}
