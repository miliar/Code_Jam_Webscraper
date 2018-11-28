#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <string>
#include <cassert>
#include <list>
#include <algorithm>

using namespace std;
typedef vector<string> vs_t;

vector<string> SplitPath(string const& p)
{
	vector<string> res;
	string::const_iterator from = find(p.begin(), p.end(), '/');
	++from;
	while (from != p.end())
	{
		string::const_iterator to = from;
		res.push_back("");
		while (to != p.end() && *to != '/') 
		{
			res.back().push_back(*to);
			++to;
		}
		from = to;
		if (from != p.end())
		{
			assert(*from == '/');
			++from;
		}
	}
	return res;
}

struct FS
{
	string name;
	list<FS*> subDirs;
};

int FindPath(FS *root, vs_t const& p, int pos = 0)
{
	if (pos >= p.size())
		return pos;	
	for (list<FS*>::iterator it = root->subDirs.begin();
		it != root->subDirs.end(); ++it)
	{
		if (p[pos] == (*it)->name)
		{
			return FindPath(*it, p, pos + 1);
		}
	}
	return pos;
}

void CreatePath(FS *root, vs_t const& p, size_t pos = 0)
{
	if (pos >= p.size())
		return;
	for (list<FS*>::iterator it = root->subDirs.begin();
		it != root->subDirs.end(); ++it)
	{
		if (p[pos] == (*it)->name)
		{
			return CreatePath(*it, p, pos + 1);
		}
	}
	root->subDirs.push_back(new FS());
	root->subDirs.back()->name = p[pos];
	CreatePath(root->subDirs.back(), p, pos + 1);
}

void PrintPath (FS* r)
{
	cout << r->name << endl;
	for (list<FS*>::iterator it = r->subDirs.begin();
		it != r->subDirs.end(); ++it)
	{
		PrintPath(*it);
	}
}

int main(int ac, char* av[])
{
	ifstream cin(av[1]);
	int T;
	cin >> T; cin.ignore();
	for (int t = 1; t <= T; ++t)
	{
		int N, M;
		cin >> N >> M;
		cin.ignore();
		FS *root = new FS();
		root->name = "/";
		for (int i = 0; i < N; ++i)
		{
			string path;
			getline(cin, path);
			vs_t p = SplitPath(path);
			CreatePath(root, p);
		}
		//PrintPath(root);
		int count = 0;
		for (int m = 0; m < M; ++m)
		{
			string path;
			getline(cin, path);
			vs_t p = SplitPath(path);
			count += p.size() - FindPath(root, p);
			CreatePath(root, p);
		}
		cout << "Case #" << t << ": " << count << endl;
	}
	return 0;
}