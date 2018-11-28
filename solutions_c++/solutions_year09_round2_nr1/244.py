#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <stack>

using namespace std;

struct node_t
{
	node_t(long double prob, bool hasFeature, const string& feature)
		: prob(prob), hasFeature(hasFeature), feature(feature), l(-1), r(-1)
	{
	}

	long double prob;
	bool hasFeature;
	string feature;
	int l, r;
};

typedef vector<node_t> tree_t;

struct animal_t
{
	set<string> features;
};

int getNum()
{
	string str;
	getline(cin, str);
	stringstream ss(str);
	int ans;
	ss >> ans;

	return ans;
}

tree_t makeTree(const string& s)
{
	tree_t tree;

	stack<int> nodes;
	int curPos = 0;
	while (curPos < s.length())
	{
		char curChar = s[curPos];
		if (curChar == '(')
		{
			// New node
			tree.push_back(node_t(0.0, false, ""));

			if (!nodes.empty())
			{
				if (tree[nodes.top()].l == -1)
					tree[nodes.top()].l = tree.size() - 1;
				else
					tree[nodes.top()].r = tree.size() - 1;
			}

			nodes.push(tree.size() - 1);
			++curPos;
		}
		else if (curChar == ')')
		{
			// End of node description
			nodes.pop();
			++curPos;
		}
		else if (curChar >= '0' && curChar <= '9')
		{
			// Prob
			string numStr = "";
			while (curPos < s.length() && (curChar >= '0' && curChar <= '9' || curChar == '.'))
			{
				numStr += curChar;
				++curPos;
				if (curPos < s.length())
					curChar = s[curPos];
			}

			stringstream ss(numStr);
			ss >> tree[nodes.top()].prob;
		}
		else if (curChar != ' ')
		{
			// Feature
			tree[nodes.top()].hasFeature = true;
			tree[nodes.top()].feature = "";
			while (curPos < s.length() && curChar >= 'a' && curChar <= 'z')
			{
				tree[nodes.top()].feature += curChar;
				++curPos;
				if (curPos < s.length())
					curChar = s[curPos];
			}
		}
		else
			++curPos;
	}

	return tree;
}

long double calcProb(const tree_t& tree, const animal_t& a)
{
	int curNode = 0;
	long double prob = 1.0;
	while (curNode <= tree.size())
	{
		node_t node = tree[curNode];
		prob *= node.prob;

		if (node.hasFeature && a.features.count(node.feature))
			curNode = node.l;
		else
			curNode = node.r;
	}

	return prob;
}

int main(int argc, char* argv[])
{
	int N = getNum();
	for (int test = 1; test <= N; ++test)
	{
		int L = getNum();

		string str;
		string treeStr = "";
		for (int i = 0; i < L; ++i)
		{
			getline(cin, str);
			treeStr += str + " ";
		}

		const tree_t tree = makeTree(treeStr);

		cout << "Case #" << test << ":" << endl;

		int A = getNum();
		for (int a = 0; a < A; ++a)
		{
			string animalStr;
			getline(cin, animalStr);
			stringstream ss(animalStr);

			int fn;
			ss >> animalStr >> fn;
			animal_t animal;
			for (int i = 0; i < fn; ++i)
			{
				ss >> animalStr;
				animal.features.insert(animalStr);
			}

			cout << fixed << calcProb(tree, animal) << endl;
		}
	}

	return 0;
}
