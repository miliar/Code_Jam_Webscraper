#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <cassert>
using namespace std;

struct dir {
	string name;
	dir *child;
	dir *next;
	dir *parent;
};

vector<string> parse(string path)
{
		int len = path.size();
		for(int k=0; k < len; k++)
			if (path[k] == '/')
				path[k] = ' ';
		vector<string> vpath;
		stringstream ss(path);
		string dirname;
		while(ss >> dirname)
		{
//			cout << "dirname: " << dirname << endl;
			vpath.push_back(dirname);
		}
		return vpath;
}

int update(dir *root, const vector<string> &vpath, int k)
{
//cout << "root " << root->name << " " << k << " " << vpath.size() << endl;
	if (!root) return 0;
	if (k >= vpath.size()) return 0;
	dir *last=0;
	for(dir *p=root->child; p; p = p->next)
	{
//	cout << "p " << p->name << endl;
		if (p->name == vpath[k])
			return update(p,vpath,k+1);
		last = p;
	}
	dir *newnode = new dir; newnode->name = vpath[k];
	newnode->parent = root; newnode->next = 0; newnode->child = 0;
	if (root->child)
	{
		assert(last);
		last->next = newnode;
	}
	else
		root->child = newnode;
	return 1+update(newnode,vpath,k+1);
}

void solve()
{
	int N, M; cin >> N >> M; //cout << "N M " << N << " " << M << endl;
	dir *root = new dir;
	root->name = ""; 
	root->child = root->next = root->parent = 0;

	// parse path of known dir
	for(int i=0; i < N; i++)
	{
		string path; cin >> path;
		vector<string> vpath = parse(path);
		update(root, vpath,0);
	}

	// add up cost
	int ret = 0;
	for(int i=0; i < M; i++)
	{
		string path; cin >> path; //cout << path << endl;
		vector<string> vpath = parse(path);
		ret += update(root, vpath,0);
	}
	
	cout << ret << endl;
}

int main()
{
	int ncase; cin >> ncase;
	for(int icase=0; icase < ncase; icase++)
	{
		cout << "Case #" << (icase+1) << ": ";
		solve();
	}
}
