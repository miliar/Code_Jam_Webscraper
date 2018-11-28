#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <cmath>
#include <set>
#include <map>
using namespace std;

#define OR 0
#define AND 1

int n, v;
int t[10010];
bool can[10010];
bool leaf[10010];

int mem[10010][2];

const int oo = 1<<20;

int go(int x, int val)
{
	int& ret = mem[x][val];
	if (ret != -1) return ret;
	ret = oo;

	if (leaf[x])
	{
		if (val == t[x]) return ret = 0;
		return ret = oo;
	}
	if (t[x] == AND || can[x])
	{
		int c = 0;
		if (t[x] == OR) c = 1;

		if (val == 1)
		{
			ret = min(ret, c + go(2*x, 1) + go(2*x+1, 1));
		}
		else
		{
			int t = c + min(go(2*x, 0), go(2*x+1, 0));
			ret = min(ret, t);
		}
	}
	if (t[x] == OR || can[x])
	{
		int c = 0;
		if (t[x] == AND) c = 1;

		if (val == 1)
		{
			int t = c + min(go(2*x, 1), go(2*x+1, 1));
			ret = min(ret, t);
		}
		else
		{
			ret = min(ret, c + go(2*x, 0) + go(2*x+1, 0));
		}
	}

	// cout<<x<<" with "<<v<<" = "<<ret<<endl;
	return ret;
}

int main()
{
	ifstream cin("A-large.in");
	ofstream cout("a.out");

	int z;
	cin>>z;
	int tc = 1;
	while(z--)
	{
		memset(leaf, 0, sizeof(leaf));

		cin>>n>>v;
		for (int i = 1 ; i <= n ; i++)
		{
			if (i <= (n-1)/2)	cin>>t[i]>>can[i];
			else
			{
				cin>>t[i];
				leaf[i] = true;
			}
		}

		memset(mem, -1, sizeof(mem));

		cout<<"Case #"<<tc++<<": ";
		int t = go(1, v);
		if (t > n) cout<<"IMPOSSIBLE"<<endl;
		else cout<<t<<endl;
	}

	return 0;
}

