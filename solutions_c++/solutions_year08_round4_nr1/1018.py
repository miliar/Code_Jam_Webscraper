#include <iostream>
#include <cstdlib>
#include <vector>
using namespace std;

int V;

struct node {
	int value, gate, changeable;
};

int eval(vector<node>& tree, int n)
{
	switch (tree[n].gate) {
		case -1:
			return tree[n].value;
		case 0: 
			return (eval(tree,2*n+1) || eval(tree,2*n+2)) ? 1 : 0;
		case 1: 
			return (eval(tree,2*n+1) && eval(tree,2*n+2)) ? 1 : 0;
	}
	return -1;	
}

int search(vector<node>& tree, vector<int>& c, int n, int p, int i)
{
	if (eval(tree, 0) == V)
	{
		return p;
	}
	else if (p != n)
	{
		for (int j=i; j<c.size(); ++j)
		{
			tree[c[j]].gate = (V+1)%2;
			
			int t = search(tree,c,n,p+1,j+1);
			if (t != -1)
			{
				return t;
			}
			
			tree[c[j]].gate = V;
		}
	}
	return -1;
}

int main() 
{
	int C;
	
	cin >> C;
	for (int cas=1; cas<=C;++cas)
	{
		int M;
		cin >> M >> V;
		
		vector<node> tree;
		node temp;
		temp.value = -1;
		int m;
		for (m=0; m < (M-1)/2; ++m)
		{
			cin >> temp.gate >> temp.changeable;
			tree.push_back(temp);
		}
		temp.gate = temp.changeable = -1;
		for (m=0; m < (M+1)/2; ++m)
		{
			cin >> temp.value;
			tree.push_back(temp);
		}
		
		
		/*
		bool success = false;
		int count = 0;
		for (int i=0; i<tree.size(); ++i)
		{
			if (eval(tree,0) == V)
			{
				success = true;
				break;
			} 
			else 
			{
				if (tree[i].changeable == 1 && tree[i].gate == V)
				{
					tree[i].gate = (V+1)%2;
					++count;
				}
			}
		}*/
		vector<int> c;
		for (int i=0; i<tree.size(); ++i)
		{
			if (tree[i].changeable == 1 && tree[i].gate == V)
			{
				c.push_back(i);
			}
		}
		
		int res = -1;
		for (int n=0; n <= c.size(); ++n)
		{
			res = search(tree, c, n, 0, 0);
			if (res != -1) break;
		}
		
		
		cout << "Case #" << cas << ": ";
		if (res != -1)
		{
			cout << res << endl;
		}
		else
		{
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}