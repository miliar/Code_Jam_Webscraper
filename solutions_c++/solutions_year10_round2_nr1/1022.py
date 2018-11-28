#include <stdio.h>
#include <string>
#include <vector>
#include <set>

using namespace std;

struct Node
{
	string name;
	vector<Node*> childs;
	Node(string n)
	{
		name = n;
	}
};

void Del(Node *t)
{
	for(int i = 0; i < t->childs.size(); ++i)
	{
		Del(t->childs[i]);
	}
	delete t;
}

int IsExist(Node *N, const string & s)
{
	for(int i = 0; i < N->childs.size(); ++i)
	{
		if (N->childs[i]->name == s) return i;
	}
	return -1;
}

char str[100000];

set <string> SS; 

int main()
{
	freopen("A1.in", "r", stdin);
	freopen("A1.out", "w", stdout);
	Node *Root;
	int T, n, m;
	scanf("%d", &T);
	Node *t;
	for(int I = 0; I < T; ++I)
	{
		Root = new Node(string(""));
		int res = 0;
		SS.clear();
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; ++i)
		{
			scanf("%s", &str);
			string s(str);
			if (SS.find(s) != SS.end()) continue;
			t = Root;
			string st;
			for(int j = 1; j < s.size(); ++j)
			{
				if (s[j] == '/')
				{
					int x = IsExist(t, st);
					if (x == -1)
					{
						Node *node = new Node(st);
						t->childs.push_back(node);
						t = t->childs[t->childs.size() - 1];
						st.clear();
					}
					else
					{
						t = t->childs[x];
						st.clear();
					}
				}
				else st += s[j];
			}
			if (!st.empty())
			{
				int x = IsExist(t, st);
				if (x == -1)
				{
					Node *node = new Node(st);
					t->childs.push_back(node);
					st.clear();
				} 
			}
		}
		for(int i = 0; i < m; ++i)
		{
			t = Root;
			scanf("%s", &str);
			string s(str);
			if (SS.find(str) != SS.end()) continue;
			string st;
			for(int j = 1; j < s.size(); ++j)
			{
				if (s[j] == '/')
				{
					int x = IsExist(t, st);
					if (x == -1)
					{
						Node *node = new Node(st);
						++res;
						t->childs.push_back(node);
						t = t->childs[t->childs.size() - 1];
						st.clear();
					}
					else
					{
						t = t->childs[x];
						st.clear();
					}
				}
				else st += s[j];
			}
			if (!st.empty())
			{
				int x = IsExist(t, st);
				if (x == -1)
				{
					Node *node = new Node(st);
					++res;
					t->childs.push_back(node);
					st.clear();
				} 
			}
		}
		Del(Root);
		printf("Case #%d: %d\n", I + 1, res);
	}
	return 0;
}