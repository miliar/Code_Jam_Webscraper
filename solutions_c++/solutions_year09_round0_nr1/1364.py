// Solution by Maxim Kulikov <maxim.coolikov@gmail.com>
// Compiled with Visual Studio 2005 Express Edition

#include <cstdio>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int l, d;

struct Node {
private:
	Node* next[26];
	Node* add (char c)
	{
		return next[c - 'a'] = new Node ();
	}
	Node* get (char c)
	{
		return next[c - 'a'];
	}
public:
	Node ()
	{
		memset (next, 0, sizeof (next));
	}
	void add (string s, int i)
	{
		if (i == l) return;
		Node* child = get (s[i]);
		if (!child) child = add (s[i]);
		child->add (s, i + 1);
	}
	int get (string s, int i, int deep)
	{
		if (deep == l) return 1;
		if (s[i] != '(')
		{
			Node* child = get (s[i]);
			return child ? child->get (s, i + 1, deep + 1) : 0;
		}
		else
		{
			int ret = 0;
			int j;
			for (j = i; s[j] != ')'; ++j);
			for (int k = i + 1; k < j; ++k)
			{
				Node* child = get (s[k]);
				ret += child ? child->get (s, j + 1, deep + 1) : 0;
			}
			return ret;
		}
	}
};

int main ()
{
	freopen ("A-large.in", "rt", stdin);
	freopen ("A-large.out", "wt", stdout);

	int test_n;
	Node *root = new Node ();
	cin >> l >> d >> test_n;
	for (int i = 0; i < d; ++i)
	{
		string s;
		cin >> s;
		root->add (s, 0);
	}
	for (int test = 1; test <= test_n; ++test)
	{
		string s;
		cin >> s;
		cout << "Case #" << test << ": " << root->get (s, 0, 0) << endl;
	}

	return 0;
}