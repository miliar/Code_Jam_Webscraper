
#include <map>
#include <string>
#include <iostream>

using namespace std;

struct o
{
	map<string, o*> next;
};

o root;


int insert(const string &s)
{
	int res = 0;
	o *cur = &root;
	string dir = "";
	for (int i = 1; i <= s.size(); i++)
	{
		if (i < s.size() && s[i] != '/') dir += s[i];
		else
		{
			//cout << " - dir: " << dir << " ";
			map<string, o*>::iterator it = cur->next.find(dir);
			if (it == cur->next.end())
			{
				res++;
				o *sdir = new o;
				cur->next[dir] = sdir;
				cur = sdir;
				//cout << "created" << endl;
			} else
			{
				cur = it->second;
				//cout << "present" << endl;
			}
			dir = "";
		}
	}
	return res;
}

int main()
{
	int c, m, n;
	string s;

	cin >> c;

	for (int cn = 1; cn <= c; cn++)
	{
		root.next.clear();

		cout << "Case #" << cn << ": ";
		cin >> n >> m;

		for (int i = 0; i < n; i++)
		{
			cin >> s;
			insert(s);
			//cout << s << " in system" << endl;
		}

		int res = 0;
		for (int i = 0; i < m; i++)
		{
			cin >> s;
			res += insert(s);
			//cout << endl << "adding " << s << " needs " << res << endl;
		}

		cout << res << endl;
	}

	return 0;
}

