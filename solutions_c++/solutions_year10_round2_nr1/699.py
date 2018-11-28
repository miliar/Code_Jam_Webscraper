#include <iostream>
#include <string>
#include <map>
#include <cstdio>
using namespace std;

struct T 
{
	bool in_new;
	map<string, T> files;  
};

void add(const bool is_new,const string path, const size_t p , T & root)
{
	map<string, T>::iterator i;
	string tdir;
	size_t tp;
	tp= path.find("/", p);
	if (tp==string::npos)
	{
		tdir= string(path.begin()+p, path.end());
		i= root.files.find(tdir);
		if (i==root.files.end())
		{
			T tmp;
			tmp.in_new= is_new;
			root.files[tdir]= tmp;
		}
	}
	else
	{
		tdir= string(path.begin()+p, path.begin()+tp);
		i= root.files.find(tdir);
		if (i==root.files.end())
		{
			T tmp;
			tmp.in_new= is_new;
			root.files[tdir]= tmp;
		}
		add(is_new, path, tp+1, root.files[tdir]);
	}
}

const int cnt(const T &root)
{
	map<string, T>::const_iterator i;
	int r(0);
	for(i=root.files.begin(); i!=root.files.end(); ++i)
	{
		if (i->second.in_new)
			r++;
		r+= cnt(i->second);
	}
	return r;
}

int main()
{
	int i, j, k, n, m, t;
	string str;
	T root;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	for(k=1; k<=t; ++k)
	{
		root.in_new= false;
		root.files.clear();
		cin >>n >>m;
		for(i=1; i<=n; ++i)
		{
			cin >> str;
			add(false, str, 1, root);
		}
		for(i=1; i<=m; ++i)
		{
			cin >> str;
			add(true, str, 1, root);
		}
		cout <<"Case #" <<k <<": " <<cnt(root) << endl; 
	}
	return 0;
}
