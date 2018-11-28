#include <iostream>
#include <map>

using namespace std;

int l, d, n;

char buf[255];

struct node
{
	int c;
	map<char, node> sub;
	node():c(0) {};
	void Add(int k)
	{
		if (k >= l)	c++; 
		else sub[buf[k]].Add(k+1);
	}
	long long Count(int k, int q)
	{
		if (q >= l) return c;
		if (buf[k] == '(')
		{
			long long res = 0;
			int j = k+1;
			while (buf[j] != ')') j++;
			for (int i=k+1;i<j;i++)
			{
				map<char, node>::iterator it = sub.find(buf[i]);
				if (it != sub.end())
				{
					res += it->second.Count(j+1, q+1);
				}
			}
			return res;
		} else
		{
			map<char, node>::iterator it = sub.find(buf[k]);
			if (it != sub.end())
			{
				return it->second.Count(k+1, q+1);
			} else return 0;
		}
	}
};

node root;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d%d%d", &l, &d, &n);
	for (int i=0;i<d;i++)
	{
		scanf("%s", buf);
		root.Add(0);
	}	
	for (int i=0;i<n;i++)
	{
		scanf("%s", buf);
		long long ans = root.Count(0, 0);
		printf("Case #%d: %I64i\n", (i+1), ans);
	}
	fclose(stdout);
}