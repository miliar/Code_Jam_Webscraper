#include <iostream>
#include <string>
#include <map>
#include <cstdlib>

using	namespace	std;

struct	dir
{
	map<string, dir*> sub;
};

dir	*root;
int	count;

string	getSub(string &s)
{
	if (s[0] != '/')
	{
		cerr << "bad s " << s << endl;
		exit(1);
	}
	s.erase(s.begin());
	string	t;
	while (s.size() > 0 && s[0] != '/')
	{
		t += s[0];
		s.erase(s.begin());
	}
	return t;
}

void	add(string s)
{
	dir	*d = root;
	while (s.size() > 0)
	{
		string t = getSub(s);
		map<string, dir*>::iterator iter = d->sub.find(t);
		if (iter == d->sub.end())
		{
			dir *dd = new dir();
			d->sub.insert(make_pair(t, dd));
			d = dd;
		}
		else
			d = d->sub[t];
	}
}

void	mk(string s)
{
	dir	*d = root;
	while (s.size() > 0)
	{
		string t = getSub(s);
		map<string, dir*>::iterator iter = d->sub.find(t);
		if (iter == d->sub.end())
		{
			dir *dd = new dir();
			d->sub.insert(make_pair(t, dd));
			d = dd;
			++count;
		}
		else
			d = d->sub[t];
	}
}

void	solve()
{
	delete root;
	root = new dir();
	count = 0;
	int	n, m;
	cin >> n >> m;
	for (int i = 0; i < n; ++i)
	{
		string	s;
		cin >> s;
		add(s);
	}
	for (int i = 0; i < m; ++i)
	{
		string	s;
		cin >> s;
		mk(s);
	}
	cout << count << endl;
}

int	main()
{
	root = 0;
	int	t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return	0;
}

