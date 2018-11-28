
#include <iostream>
#include <string>
#include <map>
#include <cstdio>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

int main()
{
	const int oo = 1000000000;
	string line;
	int n;
	getline(cin, line);
	sscanf(line.c_str(), "%d", &n);
	for (int kase=1; kase<=n; kase++)
	{
		int s, q;
		getline(cin, line);
		sscanf(line.c_str(), "%d", &s);
		map<string,int> m;
		for (int i=0; i<s; i++)
		{
			getline(cin, line);
			m[line] = i;
		}
		getline(cin, line);
		sscanf(line.c_str(), "%d", &q);
		VVI a(s, VI(q+1, oo));
		for (int i=0; i<s; i++)
			a[i][0] = 0;
		for (int j=1; j<=q; j++) // O(q * s^2)
		{
			getline(cin, line);
			int t = m[line];
			for (int i=0; i<s; i++)
			{
				if (i == t)
					continue;
				a[i][j] = a[i][j-1];
				for (int k=0; k<s; k++)
					a[i][j] = min(a[i][j], a[k][j-1]+1);
			}
		}
		int sol = oo;
		for (int i=0; i<s; i++)
			sol = min(sol, a[i][q]);
		cout << "Case #" << kase << ": " << sol << endl;

	}
	return 0;
}
