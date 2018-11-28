#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int T; cin >> T;
	for (int C = 1; C <= T; ++C)
	{
		int n; cin >> n;
		vector<int> v(n);
		int xr = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> v[i];
			xr ^= v[i];
		}
		
		cout << "Case #" << C << ": ";
		
		if (xr != 0) cout << "NO\n";
		else
		{
			sort( v.begin(), v.end() );
			int ret = 0;
			for (int i = 1; i < v.size(); ++i) ret += v[i];
			cout << ret << endl;
		}
	}
}
