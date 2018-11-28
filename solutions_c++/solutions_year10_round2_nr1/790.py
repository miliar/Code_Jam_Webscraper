#include <iostream>
using namespace std;

const int maxn = 100;
const int maxm = 100;

string exist[maxn];
string need[maxm];

struct Node {
	string name;
	Node *brother;
	Node *children;
};

int main()
{
	int tt;
	cin >> tt;
	for (int tc = 1; tc <= tt; tc++)
	{
		Node root;
		root.name = "/";
		root.brother = NULL;
		root.children = NULL;
		int newcount = 0;
		int n,m;
		cin >> n >> m;
		string str;
		getline(cin, str);
		for (int i=0; i<n; i++)
		{
			getline(cin, str);
			string name = "";
			Node *curr = &root;
			for (int i=1; i<=str.length(); i++)
			{
				if ((i == str.length()) || (str[i] == '/'))
				{
					Node *child = curr->children;
					bool found = false;
					while (child != NULL)
					{
						if (child->name == name)
						{
							found = true;
							break;
						}
						child = child->brother;
					}
					if (found)
					{
						curr = child;
					} else {
						Node *newchild = new Node;
						newchild->name = name;
						newchild->brother = curr->children;
						newchild->children = NULL;
						curr->children = newchild;
						curr = newchild;
					}
					name = "";
				} else {
					name = name + str[i];
				}
			}
		}

		for (int i=0; i<m; i++)
		{
			string str;
			getline(cin, str);
			string name = "";
			Node *curr = &root;
			for (int i=1; i<=str.length(); i++)
			{
				if ((i == str.length())|| (str[i] == '/'))
				{
					Node *child = curr->children;
					bool found = false;
					while (child != NULL)
					{
						if (child->name == name)
						{
							found = true;
							break;
						}
						child = child->brother;
					}
					if (found)
					{
						curr = child;
					} else {
						Node *newchild = new Node;
						newchild->name = name;
						newchild->brother = curr->children;
						newchild->children = NULL;
						curr->children = newchild;
						curr = newchild;
						newcount ++;
					}
					name = "";
				} else {
					name = name + str[i];
				}
			}
		}
		cout << "Case #" << tc << ": " << newcount << endl;
	}
	return 0;
}

