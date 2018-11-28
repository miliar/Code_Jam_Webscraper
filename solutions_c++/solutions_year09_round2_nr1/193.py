// ProbB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>

using namespace std;
vector<string> tokenize(const string& str, char delimiters)
{
	vector<string> tokens;
	int len = (int)str.length();
	int pos = 0;
	int i = 0;
	int quote = 0;
	for (;;)
	{
		while (pos<len && (str[pos]!=delimiters || (str[pos]==delimiters && quote!=0)))
		{
			if (str[pos]=='"')
				quote = 1-quote;
			pos++;
		}
		if (pos<len && str[pos]==delimiters)
		{
			if (str[i]=='"')
			{
				tokens.push_back(str.substr(i+1, pos-i-2));
			}
			else
			{
				tokens.push_back(str.substr(i, pos-i));
			}
			i = pos+1;
		}
		else
		{
			if (str[i]=='"')
			{
				tokens.push_back(str.substr(i+1, pos-i-2));
			}
			else
			{
				tokens.push_back(str.substr(i, pos-i));
			}
			break;
		}
		pos++;
	}
	return tokens;
}

struct Node
{
	double w;
	string name;
	Node *yes;
	Node *no;
	Node()
	{
		yes = 0;
		no = 0;
	}
};

string tree;
Node *root;
vector<Node*> toFree;

void build(Node* node, int &pos)
{
	node->yes = 0;
	node->no = 0;
	if (tree[pos]=='(')
	{
		pos++;
		// read w
		double w = 0;
		bool b = false;
		int cnt = 0;
		for (;;)
		{
			if (tree[pos]>='0' && tree[pos]<='9')
			{
				w = w*10.0 + (tree[pos]-'0');
				if (b) cnt++;
				pos++;
			}
			else if (tree[pos]=='.')
			{
				b = true;
				pos++;
			}
			else break;
		}
		for (int z=0;z<cnt;z++) w = w / 10.0;
		node->w = w;
		if (tree[pos]==')')
		{
			pos++;
			return;
		}
		// name
		stringstream sn;
		while (tree[pos]>='a' && tree[pos]<='z')
		{
			sn << tree[pos];
			pos++;
		}
		node->name = sn.str();
		Node *pY = new Node();
		toFree.push_back(pY);
		Node *pN = new Node();
		toFree.push_back(pN);
		node->yes = pY;
		node->no = pN;
		build(pY, pos);
		build(pN, pos);
		if (tree[pos]==')')
		{
			pos++;
		}
	}
}

map<string, int> feat;

void solve()
{
	root = new Node();
	char buf[16384];
	int T;
	cin >> T;
	for (int t=0;t<T;t++)
	{
		feat.clear();
		while (toFree.size()>0)
		{
			delete toFree.back();
			toFree.pop_back();
		}
		int L;
		cin >> L;
		cin.getline(buf, 16384);
		stringstream ss;
		for (int l=0;l<L;l++)
		{
			cin.getline(buf, 16384);
			string s = buf;
			for (int i=0;i<s.length();i++)
				if ((s[i]>='0' && s[i]<='9') || s[i]=='.' || s[i]=='(' || s[i]==')'  || (s[i]>='a' && s[i]<='z'))
				{
					ss << s[i];
				}
		}
		tree = ss.str();
		int pos = 0;
		build(root, pos);
		int Q;
		cin >> Q;
		cin.getline(buf, 16384);
		cout << "Case #" << (t+1) << ":" << endl;
		for (int i=0;i<Q;i++)
		{
			cin.getline(buf, 16384);
			string s = buf;
			vector<string> anim = tokenize(s, ' ');
			int n = atoi(anim[1].c_str());
			feat.clear();
			for (int z=0;z<n;z++)
			{
				feat[anim[z+2]]++;
			}
			Node *p = root;
			double d = root->w;
			for (;;)
			{
				if (p->yes && p->no)
				{
					if (feat.count(p->name)>0)
					{
						p = p->yes;
					}
					else
					{
						p = p->no;
					}
				}
				else
					break;
				d = d * p->w;
			}
			printf("%.7f\n",d);
			//cout << setw(7) << d << endl;
		}
	}

}

int _tmain(int argc, _TCHAR* argv[])
{
	solve();
	return 0;
}
