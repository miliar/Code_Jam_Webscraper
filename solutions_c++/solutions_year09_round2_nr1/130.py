#include <algorithm>
#include <cassert>
#include <iostream>
#include <set>
#include <string>
#include <sstream>
#include <vector>

using namespace std;


// Vars

struct Node
{
	Node() : left(NULL), right(NULL) { }

	double prob;
	string feat;
	Node *left, *right;
};

string str;
char buf[1024];


// Func

void SkipSpace(string::size_type &index)
{
	while (isspace(str[index]))
	{
		++index;
	}
}

Node *Parse(string::size_type &index)
{
	SkipSpace(index);

	assert(str[index] == '(');
	++index;

	SkipSpace(index);

	Node *node = new Node();

	int cur = 0;

	while (!isspace(str[index]) && str[index] != ')')
	{
		buf[cur] = str[index];
		++index;
		++cur;
	}

	buf[cur] = 0;
	node->prob = atof(buf);

	SkipSpace(index);

	if (str[index] == ')')
	{
		++index;
		return node;
	}

	cur = 0;

	while (!isspace(str[index]) && str[index] != '(')
	{
		buf[cur] = str[index];
		++index;
		++cur;
	}

	buf[cur] = 0;
	node->feat = buf;

	node->left = Parse(index);
	node->right = Parse(index);

	SkipSpace(index);

	assert(str[index] == ')');
	++index;

	return node;
}

double GetProb(Node *root, const set<string> &feats)
{
	if (root->left == NULL)
	{
		assert(root->right == NULL);
		return root->prob;
	}

	assert(root->right != NULL);

	if (feats.find(root->feat) != feats.end())
	{
		return root->prob * GetProb(root->left, feats);
	}
	else
	{
		return root->prob * GetProb(root->right, feats);
	}
}


// Main

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testn;
	cin >> testn;

	string tmp;
	set<string> feats;

	for (int testi = 0; testi < testn; ++testi)
	{
		int linen;
		cin >> linen;
		cin.get();

		str.clear();

		for (int i = 0; i < linen; ++i)
		{
			getline(cin, tmp);
			str += ' ' + tmp;
		}

		string::size_type index = 0;
		Node *root = Parse(index);

		int ann;
		cin >> ann;

		cout << "Case #" << testi + 1 << ':' << endl;

		for (int i = 0; i < ann; ++i)
		{
			int num;
			cin >> tmp >> num;

			feats.clear();

			for (int j = 0; j < num; ++j)
			{
				cin >> tmp;
				feats.insert(tmp);
			}

			double prob = GetProb(root, feats);

			cout.precision(7);
			cout << fixed << prob << endl;
		}
	}

	return 0;
}