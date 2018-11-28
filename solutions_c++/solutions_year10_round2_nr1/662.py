#include <iostream>
#include <map>
#include <string>
using namespace std;
struct Directory
{
	//string Name;
	//Directory* parent;
	map<string, Directory*> children;
};
int count;
Directory root;
int Add(string& s)
{
	int c = 0, p = 1, size = s.size();
	string cur;
	Directory* dir = &root;
	while (p < size)
	{
		while (p < size && s[p] != '/')
		{
			cur += s[p++];
		}
		if (dir->children.find(cur) == dir->children.end()) 
		{
			//create
			c++;
			Directory* tmp = new Directory; 
			dir->children[cur] = tmp;
		}
		p++;
		dir = dir->children[cur];
		cur.clear();
	}
	return c;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t, n, m;
	string tmp;
	cin >> t;
	for (int k = 1; k <= t; k++)
	{
		cin >> n >> m;
		for (int i = 0; i < n; i++)
		{
			cin >> tmp;
			Add(tmp);
		}
		for (int i = 0; i < m; i++)
		{
			cin >> tmp;
			count += Add(tmp);
		}
		cout << "Case #" << k << ": " << count << endl;
		count = 0;
		root.children.clear();
	}
	return 0;
}
