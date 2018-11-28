#include <iostream>
#include <vector>
#include <string>

using namespace std;
typedef vector<int> vi;
typedef vector<char> vc;
typedef vector<string> vs;

struct Node
{
	char c;

	vi chptr;

	Node() {}

	Node(char _c)
	{
		c = _c;
	}
};

typedef vector<Node> vn;

vn tree;
int size;
string s;

void BuildTree(int i, int j)
{
	if (i == s.length())
		return;

	Node node = tree[j];
	for (int k = 0; k < node.chptr.size(); k++)
	{
		if (tree[node.chptr[k]].c == s[i])
		{
			BuildTree(i + 1, node.chptr[k]);
			break;
		}
	}

	//create new Node
	tree.push_back(Node(s[i]));
	tree[j].chptr.push_back(size);
	size ++;
	
	BuildTree(i + 1, size - 1);
}

int Compare(int i, int j)
{
	if (i == s.length())
		return 1;

	vc arr;
	if (s[i] == '(')
	{
		i++;
		while (s[i] != ')')
		{
			arr.push_back(s[i]);
			i++;
		}
	}
	else
		arr.push_back(s[i]);

	int result = 0;
	Node node = tree[j];
	for (int t = 0; t < arr.size(); t++)
	{
		char c = arr[t];
		for (int k = 0; k < node.chptr.size(); k++)
		{
			if (c == tree[node.chptr[k]].c)
			{
				result += Compare(i + 1, node.chptr[k]);
				break;
			}
		}
	}

	return result;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int Len, n, m;
	cin >> Len >> n >> m;

	tree.push_back(Node(' '));
	size = 1;

	for (int i = 0; i < n; i++)
	{
		cin >> s;
		BuildTree(0, 0);
	}

	for (int i = 0; i < m; i++)
	{
		cin >> s;
		cout << "Case #" << i + 1 << ": " << Compare(0, 0) << endl;
	}

	return 0;
}