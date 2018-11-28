#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <climits>
#include <cstdio>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int xor(vector<int> a)
{
	int sa = 0;
	for (int i=0; i<a.size(); i++)
		sa ^= a[i];

	return sa;
}

bool notCry(vector<int> a, vector<int> b)
{
	return xor(a) == xor(b);
}

int main()
{
	freopen("data.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T; cin >> T;
	
	for (int x=1; x<=T; x++)
	{
		cout << "Case #" << x << ": "; 

		int n; cin >> n;
		vector<int> c;
		for (int i=0; i<n; i++)
		{
			int t; cin >> t;
			c.push_back(t);
		}

		int stop = (1<<n)-1, best = 0;

		for (int i=1; i<stop; i++)
		{
			vector<int> va, vb;
			int mySum = 0;
			for (int j=0; j<n; j++)
				if ( ((i>>j)&1) == 1 )
				{
					mySum += c[j];
					va.push_back(c[j]);
				}
				else vb.push_back(c[j]);

			if (mySum > best && notCry(va, vb))
				best = mySum;
		}

		if (best == 0) cout << "NO\n";
		else cout << best << endl;
	}
}