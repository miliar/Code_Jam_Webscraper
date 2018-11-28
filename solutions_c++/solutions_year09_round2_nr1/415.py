#include <iostream>
#include <string>
#include <set>

using namespace std;

set<string> features;

struct Node
{
	string feature;
	double w;
	Node *left, *right;
	bool is_leaf;

	Node()
	{
		feature = string();
		w = 0;
		left = right = (Node*)NULL;
		is_leaf = false;
	}

	void Read()
	{
		char c = 32;
		while (c != '(')
			cin >> c;
		cin >> w;

		c = 32;
		while (c != ')' && !('a' <= c && c <= 'z'))
			cin >> c;

		if (c == ')')
			is_leaf = true;
		else
		{
			while (('a' <= c && c <= 'z'))
			{
				feature += c;
				cin >> c;
			}
			cin.putback(c);

			left = new Node();
			left->Read();
			right = new Node();
			right->Read();
			c = 32;
			while (c != ')')
				cin >> c;
		}

	}

	double Go(double value)
	{
		value *= w;
		if (is_leaf)
			return value;
		if (features.find(feature) != features.end())
			return left->Go(value);
		return right->Go(value);
	}
};

int n, l, a, cnt;
Node *root;
string tmp;

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		root = new Node();
		cin >> l;
		root->Read();

		cin >> a;
		cout << "Case #" << i + 1 << ":" << endl;
		for (int j = 0; j < a; j++)
		{
			cin >> tmp;
			features.clear();
			cin >> cnt;
			for (int u = 0; u < cnt; u++)
			{
				cin >> tmp;
				features.insert(tmp);
			}
			double rez = root->Go((double)1.0);
			cout << rez << endl;
		}
	}
	return 0;
}