#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

const int maxm = 10000;

struct midnode {
	int g,c;
};

midnode mid[maxm+1];
int fin[maxm+1];
int val[maxm+1];
int m,v;

bool ismid(int node)
{
	return (node <= (m-1)/2);
}

bool isand(int node)
{
	return (mid[node].g == 1);
}

bool ischg(int node)
{
	return (mid[node].c == 1);
}

void calcinit(int node)
{
	if (ismid(node))
	{
		calcinit(2*node);
		calcinit(2*node+1);
		if (isand(node))
			val[node] = val[2*node] and val[2*node+1];
		else
			val[node] = val[2*node] or val[2*node+1];
	}
	else
		val[node] = fin[node];
}

int mini(int node, int value)
{
	int minv = m+100;
	if (ismid(node))
	{
		if (value == val[node])
			return 0;
		if (isand(node))
		{
			if (value == 1)
				minv = min(minv, mini(2*node, 1)+mini(2*node+1, 1));
			else
			{
				minv = min(minv, mini(2*node, 0)+mini(2*node+1, 0));
				minv = min(minv, mini(2*node, 0)+mini(2*node+1, 1));
				minv = min(minv, mini(2*node, 1)+mini(2*node+1, 0));
			}
			if (ischg(node))
			{
				if (value == 1)
				{
					minv = min(minv, 1+mini(2*node, 1)+mini(2*node+1,1));
					minv = min(minv, 1+mini(2*node, 0)+mini(2*node+1,1));
					minv = min(minv, 1+mini(2*node, 1)+mini(2*node+1,0));
				}
				else
					minv = min(minv, 1+mini(2*node, 0)+mini(2*node+1, 0));
			}
		}
		else
		{
			if (value == 0)
				minv = min(minv, mini(2*node, 0)+mini(2*node+1, 0));
			else
			{
				minv = min(minv, mini(2*node, 1)+mini(2*node+1, 1));
				minv = min(minv, mini(2*node, 0)+mini(2*node+1, 1));
				minv = min(minv, mini(2*node, 1)+mini(2*node+1, 0));
			}
			if (ischg(node))
			{
				if (value == 0)
				{
					minv = min(minv, 1+mini(2*node, 0)+mini(2*node+1,0));
					minv = min(minv, 1+mini(2*node, 0)+mini(2*node+1,1));
					minv = min(minv, 1+mini(2*node, 1)+mini(2*node+1,0));
				}
				else
					minv = min(minv, 1+mini(2*node, 1)+mini(2*node+1, 1));
			}
		}
		return minv;
	}
	else
	{
		if (value == val[node])
			return 0;
		else
			return m+100;
	}
}

int main()
{
	int N;
	cin >> N;
	for (int tc = 0; tc < N; tc++)
	{
		cin >> m >> v;
		for (int i=1; i<= (m-1)/2 ; i++)
		{
			cin >> mid[i].g >> mid[i].c;
		}
		for (int i=1; i<= (m+1)/2 ; i++)
		{
			cin >> fin[i+(m-1)/2];
		}
		calcinit(1);
		int x = mini(1, v);
		cout << "Case #" << tc+1 << ": ";
		if (x > m)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << x << endl;
	}
	return 0;
}

