#include <cstdio>
#include <fstream>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iterator>

using namespace std;

class Node
{
public:
	string name;
	vector<Node*> child;
	~Node()
	{
		for(int i = 0; i < child.size(); i++)
		{
			delete child[i];
		}
	}
};

int main()
{
	freopen("F:\\A-large.in", "r", stdin);
	freopen("F:\\result.txt", "w", stdout);
	int T;
	scanf("%d", &T);

	for(int l = 0; l < T; l++)
	{
		int M, N;
		scanf("%d %d", &N, &M);

		Node *root = new Node();

		string s;
		for(int i = 0; i < N; i++)
		{
			Node *n = root;
			cin >> s;
			while(s != "")
			{
				s = s.substr(1);
				int p = s.find("/");
				string name = s.substr(0, p);
				int j;
				for(j = 0; j < n->child.size(); j++)
				{
					if(n->child[j]->name == name)
					{
						break;
					}
				}
				if(j == n->child.size())
				{
					Node *p = new Node();
					p->name = name;
					n->child.push_back(p);
					n = p;
				}
				else
				{
					n = n->child[j];
				}

				if(p == -1)
				{
					s = "";
				}
				else
				{
					s = s.substr(p);
				}
			}
		}

		int number = 0;
		for(int i = 0; i < M; i++)
		{
			Node *n = root;
			cin >> s;
			while(s != "")
			{
				s = s.substr(1);
				int p = s.find("/");
				string name = s.substr(0, p);
				int j;
				for(j = 0; j < n->child.size(); j++)
				{
					if(n->child[j]->name == name)
					{
						break;
					}
				}
				if(j == n->child.size())
				{
					Node *p = new Node();
					p->name = name;
					n->child.push_back(p);
					n = p;
					number++;
				}
				else
				{
					n = n->child[j];
				}

				if(p == -1)
				{
					s = "";
				}
				else
				{
					s = s.substr(p);
				}
			}
		}

		printf("Case #%d: %d\n", l+1, number);
	}

}