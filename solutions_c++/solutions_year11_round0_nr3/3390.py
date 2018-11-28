#include <iostream>
using namespace std;

int main()
{
	int i, j, t, T, n, total;
	int candy[1001];
	
	cin >> t;
	for (T=1; T<=t; ++T)
	{
		cin >> n;
		total = 0;
		j = 0;
		for (i=0; i<n; ++i)
		{
			cin >> candy[i];
			j^=candy[i];
			total += candy[i];
		}
		sort(candy, candy+n);
		cout << "Case #" << T << ": ";
		if (j)
			cout << "NO\n";
		else
			cout << total - candy[0] << endl;
	}
	return 0;
}
