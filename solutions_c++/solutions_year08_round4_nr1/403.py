#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int OO = 1000000000;

typedef vector<int> VI;

int main()
{
	int kases;
	cin >> kases;
	for (int kase=1; kase<=kases; kase++)
	{
		int n, target;
		cin >> n >> target;
		VI v0(n+1, OO);
		VI v1(n+1, OO);
		VI type(n+1, 0);
		VI change(n+1, 0);
		for (int i=1; i<=(n-1)/2; i++)
		{
			cin >> type[i] >> change[i];
		}
		for (int i=(n-1)/2+1; i<=n; i++)
		{
			int val;
			cin >> val;
			if (val == 1)
				v1[i] = 0;
			else
				v0[i] = 0;
		}
		for (int i=(n-1)/2; i>=1; i--)
		{
			int left = 2*i;
			int right = 2*i+1;
			if (type[i] == 1) // AND
			{
				v1[i] = min(v1[i], v1[left] + v1[right]);
				v0[i] = min(v0[i], min(v0[left], v0[right]));
				if (change[i])
				{
					v1[i] = min(v1[i], 1 + min(v1[left], v1[right]));
					v0[i] = min(v0[i], 1 + v0[left] + v0[right]);
				}
			}
			if (type[i] == 0) // OR
			{
				v1[i] = min(v1[i], min(v1[left], v1[right]));
				v0[i] = min(v0[i], v0[left] + v0[right]);
				if (change[i])
				{
					v1[i] = min(v1[i], 1 + v1[left] + v1[right]);
					v0[i] = min(v0[i], 1 + min(v0[left], v0[right]));
				}
			}
		}
		cout << "Case #" << kase << ": ";
		if (target == 0 && v0[1] < OO)
		{
			cout << v0[1] << endl;
			continue;
		}
		if (target == 1 && v1[1] < OO)
		{
			cout << v1[1] << endl;
			continue;
		}
		cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
