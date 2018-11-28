#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int tc=1; tc<=t; tc++)
	{
		int n;
		unsigned long k;
		cin >> n >> k; 
		if (k == 0)
		{
			cout << "Case #" << tc << ": OFF" << endl;
		} else {
			bool ok = true;
			for (int i=0; i<n; i++)
			{
				if ((k & 1) == 0)
				{
					ok = false;
					break;
				}
				k = k >> 1;
			}
			if (ok)
			{
				cout << "Case #" << tc << ": ON" << endl;
			} else {
				cout << "Case #" << tc << ": OFF" << endl;
			}
		}
	}
	return 0;
}
