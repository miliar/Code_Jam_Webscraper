#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <string>

using namespace std;

typedef vector<int> VI;
typedef set<int> SI;
typedef set<string> SS;
typedef vector<string> VS;

const int OO = 1000000000;

int main()
{
	int kases;
	cin >> kases;
	for (int kase=1; kase<=kases; kase++)
	{
		int n;
		cin >> n;
		VI from(n), to(n);
		VS color(n);
		VI use(n);
		for (int i=0; i<n; i++)
		{
			cin >> color[i] >> from[i] >> to[i];
			from[i]--;
			to[i]--;
		}
		int upto = (1 << n);
		int sol = OO;
		for (int mask=0; mask<upto; mask++)
		{
			int m = mask;
			for (int i=0; i<n; i++)
			{
				use[i] = m % 2;
				m /= 2;
			}
			SS s;
			VI fence(10000, 0);
			int num = 0;
			bool legal = true;
			for (int i=0; i<n; i++)
			{
				if (use[i])
				{
					num++;
					s.insert(color[i]);
					if (s.size() > 3)
					{
						legal = false;
						break;
					}
					for (int j=from[i]; j<=to[i]; j++)
						fence[j] = 1;
				}
			}
			for (int j=0; j<10000; j++)
				if (!fence[j])
				{
					legal = false;
					break;
				}
			if (legal)
				sol = min(sol, num);
		}
		cout << "Case #" << kase << ": ";
		if (sol != OO)
			cout << sol << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
