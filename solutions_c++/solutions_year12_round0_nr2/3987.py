#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<math.h>
#include<set>
#include<vector>
#include<string.h>
#include<string>
#include<map>
using namespace std;

int makeMeFully(int numb, int k)
{
	int x = numb / 3;
	if (numb % 3 == 0)
	{
		if (x >= k)
			return 2;
		if (x + 1 >= k && x - 1 >= 0)
			return 1;
		return 0;
	}
	if (numb % 3 == 2)
	{
		if (x + 1 >= k)
			return 2;
		if (x + 2 >= k)
			return 1;
		return 0;
	}
	if (numb % 3 == 1)
	{
		if (x+1 >= k)
			return 2;
		return 0;
	}
	return -1; // malo li chto
}

int main()
{
#ifdef _DEBUG
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif

	int t;
	cin >> t;

	for (int i=0; i<t; i++)
	{
		int n,s,p;
		cin >> n >> s >> p;
		int count = 0;
		int curr = -1;
		for (int j=0; j<n; j++)
		{
			cin >> curr;
			int r = makeMeFully(curr,p);
			if (r == 0)
				continue;
			if (r == 1)
			{
				if (s > 0)
					s--;
				else
					continue;
			}
			count++;
		}
		cout << "Case #" << i+1 << ": " << count << "\n";
	}

	return 0;
}

// q <-> z