
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int kases;
	cin >> kases;
	for (int kase=1; kase<=kases; kase++)
	{
		int n;
		cin >> n;
		vector<int> v(n, -1);
		int pos = -1;
		for (int k=1; k<=n; k++)
		{
			for (int step=0; step<k; step++)
			{
				do
				{
					pos++;
					if (pos >= n)
						pos = 1;
				} while (v[pos] != -1);
			}
			v[pos] = k;
		}
		cout << "Case #" << kase << ": ";
		int q;
		cin >> q;
		for (int i=0; i<q; i++)
		{
			int p;
			cin >> p;
			cout << " " << v[p-1];
		}
		cout << endl;
	}
	return 0;
}
