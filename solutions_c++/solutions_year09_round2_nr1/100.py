#include <cstdio>
#include <iostream>
#include <set>
#include <cctype>
#include <vector>
#include <cstring>
#include <string>

using namespace std;

struct node_s
{
	node_s() : right(-1), left(-1) {}
	double v;
	string name;
	int right, left;
};

vector<node_s> node;

void input(int idx)
{
	for (;;)
	{
		char c = fgetc(stdin);
		if (c == '(')
			break;
	}
	string q;
	for (;;)
	{
		char p = fgetc(stdin);
		if (!isspace(p))
		{
			q += p;
			break;
		}
	}
	char p;
	for (;;)
	{
		p = fgetc(stdin);
		if (!('0' <= p && p <= '9') && p != '.')
			break;
		q += p;
	}
	sscanf(q.c_str(), "%lf", &node[idx].v);
	for (;;)
	{
		if (!isspace(p))
			break; 
		p = fgetc(stdin);
	}

	if (p == ')')
		return;

	string na;
	for (;;)
	{
		na += p;
		p = fgetc(stdin);
		if (isspace(p))
			break;
	}

	node[idx].name = string() + na;
	
	node.push_back(node_s());
	node[idx].left = node.size() - 1;
	input(node.size() - 1);
	node.push_back(node_s());
	node[idx].right = node.size() - 1;
	input(node.size() - 1);

	for (;;)
	{
		p = fgetc(stdin);
		if (p == ')')
			break;
	}
}

int main()
{
	int t, ti;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		node.clear();
		node.push_back(node_s());

		int t;
		scanf("%d", &t);
		
		input(0);

		int N;
		scanf("%d", &N);
		printf("Case #%d:\n", ti);
		for (;N;N--)
		{
			set<string> props;
			int M;
			string q;
			cin >> q;
			scanf("%d", &M);
			for (;M;M--)
			{
				cin >> q;
				props.insert(q);
			}
			int idx = 0;
			double res = 1;
			for (;;)
			{
				res *= node[idx].v;
				if (node[idx].left == -1)
					break;
				if (props.find(node[idx].name) != props.end())
					idx = node[idx].left;
				else
					idx = node[idx].right;
			}
			printf("%.10lf\n", res);
		}
	}
	return 0;
}
