#include <iostream>
#include <map>
using namespace std;

struct path
{
	map<string, path> dir;
	int count()
	{
		int r = 1;
		for(map<string, path>::iterator it=dir.begin(); it!=dir.end(); it++)
			r += it->second.count();
		return r;
	}
};

path root;

void add(string s)
{
	s = s.substr(1) + '/';
	path *p = &root;
	while(!s.empty())
	{
		int ps = s.find('/');
		string d = s.substr(0, ps);
		p = &(p->dir[d]);
		s = s.substr(ps+1);
	}
}

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int ts=1; ts<=t; ts++)
	{
		int f1, f2, c1, c2;
		cin >> f1 >> f2;
		root.dir.clear();
		for(int i=0; i<f1; i++)
		{
			string s;
			cin >> s;
			add(s);
		}
		c1 = root.count();
		for(int i=0; i<f2; i++)
		{
			string s;
			cin >> s;
			add(s);
		}
		c2 = root.count();
		cout << "Case #" << ts << ": " << c2 - c1 << endl;
	}
	return 0;
}
