#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	int t,c=1;
	cin >> t;
	while(t--)
	{
		int n, k;
		cin >> n >> k;
		int i;
		bool flag = true;
		for (i=0; i<n; i++) if((k & (1<<i)) <= 0)
		{
			flag = false;
			break;
		}

		cout << "Case #" << c++ << ": ";
		if(flag) cout << "ON\n";
		else cout << "OFF\n";
	}
	return 0;
}