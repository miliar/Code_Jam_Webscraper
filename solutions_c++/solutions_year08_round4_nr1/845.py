#include<iostream>
#include<cstdio>
#include<vector>

#define REP(i,n) for(int i=0; i<n; i++)                                                                                                                                  
#define FOR(i,c) for(__typedef(c.begin())i = c.begin(); i != c.end(); i++)                                                                                           
#define ALL(c) c.begin(), c.end()    

using namespace std;

struct node
{
	int best0;
	int best1;
	bool value;
	bool ope;
	bool changeable;
	bool isleaf;
};

int myplus(int x, int y)
{
	if (x == -1 or y == -1)
		return -1;
	else 
		return (x + y);
}

int mymin(int x, int y)
{
	if (x == -1 and y == -1)
		return -1;
	else if (x == -1) 
		return y;
	else if (y == -1)
		return x;
	else 
		return ((x < y) ? x : y);
		
}

void solve(vector<node>& tree, int index);
void solve(vector<node>& tree, int index)
{
	if (tree[index].isleaf)
	{
		if(tree[index].value)
		{
			tree[index].best0 = -1;
			tree[index].best1 = 0;
		}
		else 
		{
			tree[index].best0 = 0;
			tree[index].best1 = -1;
		}
	}
	else 
	{
		solve(tree, index*2+1);
		solve(tree, index*2+2);
		if(tree[index].ope) //case and
		{
			if(tree[index].changeable)
			{
				tree[index].best0 = mymin(myplus(1, myplus(tree[index*2+1].best0, tree[index*2+2].best0)),
						mymin(tree[index*2+1].best0, tree[index*2+2].best0));
				tree[index].best1 = mymin(myplus(1, mymin(tree[index*2+1].best1, tree[index*2+2].best1)),
						myplus(tree[index*2+1].best1, tree[index*2+2].best1));
			}
			else
			{
				tree[index].best1 = myplus(tree[index*2+1].best1, tree[index*2+2].best1);
				tree[index].best0 = mymin(tree[index*2+1].best0, tree[index*2+2].best0);
			}
		}
		else
		{
			if(tree[index].changeable)
			{
				tree[index].best1 = mymin(myplus(1,myplus(tree[index*2+1].best1, tree[index*2+2].best1)),
						tree[index].best1 = mymin(tree[index*2+1].best1, tree[index*2+2].best1));
				tree[index].best0 = mymin(myplus(1, mymin(tree[index*2+1].best0, tree[index*2+2].best0)),
						myplus(tree[index*2+1].best0, tree[index*2+2].best0));
			}
			else
			{
				tree[index].best0 = myplus(tree[index*2+1].best0, tree[index*2+2].best0);
				tree[index].best1 = mymin(tree[index*2+1].best1, tree[index*2+2].best1);
			}
		}
	}
}

int main()
{
	int n;
	cin >> n;
	REP(i,n)
	{
		int m, v;
		cin >> m >> v;
		vector<node> tree;
		REP(j,m)
		{
			if(j< (m-1)/2)
			{
				int foo,bar;
				cin >> foo >> bar;
				node tmp;
				tmp.ope = (foo == 1);
				tmp.changeable = (bar == 1);
				tmp.isleaf = false;
				tree.push_back(tmp);
			}
			else 
			{
				int foo;
				cin >> foo;
				node tmp;
				tmp.value = (foo == 1);
				tmp.isleaf = true;
				tree.push_back(tmp);
			}
		}
		solve(tree, 0);
		if(v == 1)
		{
			if(tree[0].best1 != -1)
				printf("Case #%d: %d\n", i+1, tree[0].best1);
			else 
				printf("Case #%d: IMPOSSIBLE\n", i+1);
		}
		else
		{
			if(tree[0].best0 != -1)
				printf("Case #%d: %d\n", i+1, tree[0].best0);
			else 
				printf("Case #%d: IMPOSSIBLE\n", i+1);
		}


	}
}
