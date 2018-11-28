#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cmath>

using namespace std;

struct node {
	bool leaf;
	int changeable;
	int gate;
	int value;
	node(int g, int c) : leaf(false), gate(g), changeable(c) {}
	node(int v) : leaf(true) ,value(v) {}
};

int fn(vector<node>& nodes, int x, int d);


int fn2(vector<node>& nodes, int x, int d, int g)
{
	if (g)
	{
		// and
		int c1 = fn(nodes, 2 * x, d);
		int c2 = fn(nodes, 2 * x+1, d);
		if (d == 0)
		{
			if (c1 != -1 || c2 != -1)
			{
				if (c1 == -1) return c2;
				if (c2 == -1) return c1;
				return min(c1,c2);
			}
		}
		else
		{
			if (c1 != -1 && c2 != -1)
				return c1+c2;
		}
	}
	else
	{
		// or
		int c1 = fn(nodes, 2 * x, d);
		int c2 = fn(nodes, 2 * x+1, d);
		if (d == 0)
		{
			if (c1 != -1 && c2 != -1)
				return c1+c2;
		}
		else
		{
			if (c1 != -1 || c2 != -1)
			{
				if (c1 == -1) return c2;
				if (c2 == -1) return c1;
				return min(c1,c2);
			}
		}
	}
	return -1;
}

int fn(vector<node>& nodes, int x, int d)
{
	if (nodes[x-1].leaf)
	{
		return nodes[x-1].value == d ? 0 : -1;
	}

	int cnt = fn2(nodes, x, d, nodes[x-1].gate);
	if (nodes[x-1].changeable)
	{
		int c = fn2(nodes, x, d, 1-nodes[x-1].gate);
		if (c != -1 && (cnt == -1 || c < cnt))
			cnt = c+1;
	}
	return cnt;
}

int main()
{
	int N;
	cin>>N;
	for (int i = 0;i<N;i++)
	{
		int M,V;
		cin>>M>>V;

		vector<node> nodes;
		for(int j=0;j<(M-1)/2; j++)
		{
			int G,C;
			cin>>G>>C;
			nodes.push_back(node(G,C));
		}

		for(int j=0;j<(M+1)/2; j++)
		{
			int l;
			cin>>l;
			nodes.push_back(node(l));
		}

		int c = fn(nodes, 1, V);
		if (c == -1)
			printf("Case #%d: IMPOSSIBLE\n", i+1);
		else
			printf("Case #%d: %d\n", i+1, c);
	}

	return 0;
}
