#include <iostream>
#include <string>
#include <list>
#include <map>

using namespace std;

list<string> tokenize(string path)
{
	list<string> tokens;
	size_t last;
	while ((last=path.find_last_of('/'))!=string::npos)
	{
		string sub=string(path, last+1);
		if (sub!="")
			tokens.push_front(sub);
		path.erase(last);
	}
	return tokens;
}

class tree
{
public:
	~tree()
	{
		//This leaks, but if I call deltree it coredumps
		//deltree();
	}

	unsigned int addchilds(const string &path)
	{
		return addchilds(tokenize(path));
	}

	unsigned int addchilds(list<string> path)
	{
		if (path.empty())
			return 0;
		string dir=path.front();
		if (childs[dir]!=NULL)
		{
			path.pop_front();
			return childs[dir]->addchilds(path);
		}
		childs[dir]=new tree;
		path.pop_front();
		return 1+childs[dir]->addchilds(path);
	}

	void deltree()
	{
		for (map<string, tree*>::iterator i=childs.begin(); i!=childs.end(); ++i)
		{
			i->second->deltree();
			delete i->second;
		}
	}
private:
	map<string, tree*> childs;
};

int main()
{
	unsigned int t;
	cin >> t;
	string s;
	for (unsigned int i=1; i<=t; ++i)
	{
		unsigned int n, m, count=0;
		cin >> n >> m;
		tree tr;
		while (n--)
		{
			cin >> s;
			tr.addchilds(s);
		}
		while (m--)
		{
			cin >> s;
			count+=tr.addchilds(s);
		}
		cout << "Case #" << i << ": " << count << endl;
	}
}
