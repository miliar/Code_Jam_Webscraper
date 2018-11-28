#include <iostream>
#include <list>
#include <vector>
#include <cstdio>
#include <string>
#include "tree.h"
using namespace std;

list<string> split(string s, char cut = ' ') //字符串转化为链表
{
	list<string> input;
	s.append(1, ' '); //尾部加一个空格
	string tmp = "";
	for(unsigned int i = 0; i < s.length(); i++)
	{
		if(s[i] == ' ' || s[i] == 0)
		{
			if(tmp != "")
			{
				input.push_back(tmp);
				tmp = "";
			}
			continue;
		}
		else
		{
			tmp.append(1, s[i]);
		}
	}
	return input;
}


int main()
{
	int T;
	cin>>T;
	for(int t = 1; t <= T; t++)
	{
		int N,M;
		cin>>N>>M;
		string* exist = new string[N];
		string* create = new string[M];
		int tot = 0;
		for(int i = 0; i < N; i++)
		{
			cin>>exist[i];
		}
		for(int i = 0; i < M; i++)
		{
			cin>>create[i];
		}
		Tree* Tr;
		InitTree(Tr);
		TreeNode* root = Tr->root;
		for(int i = 0; i < N; i++)
		{
			list<string> lstr = split(exist[i], '/');
			list<string>::iterator lit = lstr.begin();
			TreeNode* node = root;
			while(lit != lstr.end())
			{
				if(node->firstChild == NULL)
				{
					node->firstChild = new TreeNode();
					node->firstChild->str = (*lit);
					lit++;
					continue;
				}
				if(node->firstChild->str == (*lit))
				{
					node = node->firstChild;
					lit++;
					continue;
				}
				node = node->firstChild;
				while()
				{
					
				}
				lit++;
			}
		}
		DestroyTree(Tr);
		cout<<"Case #"<<t<<": "<<4<<endl;

		delete []exist;
		delete []create;
	}


	return 0;
}
