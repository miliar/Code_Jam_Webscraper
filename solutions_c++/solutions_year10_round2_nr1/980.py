// A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <cstdio>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

int T, N, M;
string str;
int result = 0;
struct node
{
	string name;
	vector< node > childs;
};

node root;

vector< string > parse(string s)
{
	vector< string > res;
	string temp;
	res.reserve(100);
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] == '/')
		{
			if (!temp.empty())
			{
				res.push_back(temp);
				temp.clear();
			}
		}
		else
		{
			temp += s[i];
		}
	}
	res.push_back(temp);
	return res;
}

void add(string s)
{
	vector< string > dirs = parse(s);
	node* curr = &root;
	bool adding = false;
	for (int i = 0; i < dirs.size(); i++)
	{
		if (adding)
		{
			result++;
			node newnode;
			newnode.name = dirs[i];
			curr->childs.push_back(newnode);
			curr = &curr->childs[curr->childs.size() - 1];
		}
		else
		{
			int index = -1;
			for (int j = 0; j < curr->childs.size(); j++)
			{
				if (curr->childs[j].name == dirs[i])
				{
					index = j;
				}
			}
			if (index == -1)
			{
				adding = true;
				result++;
				node newnode;
				//string ss = string(dirs[i].begin(), dirs[i].end());
				newnode.name = dirs[i];
				curr->childs.push_back(newnode);
				curr = &curr->childs[curr->childs.size() - 1];
			}
			else
			{
				curr = &curr->childs[index];
			}
		}
	}
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		scanf("%d %d", &N, &M);
		node n;
		n.name = "";
		root = n;
		for (int i = 0; i < N; i++)
		{
			cin >> str;
			add(str);
		}
		result = 0;
		for (int i = 0; i < M; i++)
		{
			cin >> str;
			add(str);
		}
		printf("Case #%d: %d\n", t + 1, result);
	}
	return 0;
}

