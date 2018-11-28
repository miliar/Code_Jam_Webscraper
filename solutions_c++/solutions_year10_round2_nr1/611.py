#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct dir
{
	string name;
	vector<dir *> child;
}*root;

int exist(string name, dir* father)
{
	int j = -1, i;
	for (i = 0; i < father->child.size(); i++)
	{
		if (father->child[i]->name == name) 
		{
			j = i;
			break;
		}
	}
	return j;
}

int init(string path)
{
	string temp;
	dir *td = root;
	dir *tt;
	int count = 0, i, j;
	path = path + '/';
	while(path.length() > 1)
	{
		//path = path.substr(1, path.length() - 1);
		temp = path.substr(1, path.find_first_of('/', 1) - 1);
		j = exist(temp, td);
		if (j < 0)
		{
			tt = new dir();
			tt->name = temp;
			td->child.push_back(tt);
			td = tt;
			count++;
		}
		else 
		{
			td = td->child[j];
		}
		path = path.substr(path.find_first_of('/', 1));
	}
	return count;
}

int main()
{
	int t, i, n, m, j, count;
	string str;
	cin >> t;	
	for (i = 0; i < t; i++)
	{
		root = new dir();
		count = 0;
		cin >> n >> m;
		for (j = 0; j < n; j++)
		{
			cin >> str;
			init(str);
		}
		for (j = 0; j < m; j++)
		{
			cin >> str;
			count += init(str);
		}
		cout << "Case #" << i + 1 << ": " << count << endl;
	}
}