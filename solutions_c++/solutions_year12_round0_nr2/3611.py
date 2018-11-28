#include <iostream>
#include <algorithm>
#include <string.h>
#include <cstdlib>
using namespace std;

int t, n, s, p;
int a[128];

int main()
{
	cin >> t;
	for(int cas = 1; cas <= t; cas ++)
	{
		cin >> n >> s >> p;
		int res = 0;
		int val;
		for(int i = 0; i < n; i ++)
		{
			cin >> val;
			if(3*p-2 <= val)
				res ++;
			else if(3*p-4 <= val && s > 0 && val != 0 && val != 1 && val != 29 && val != 30)
			{
				s --;
				res ++;
			}
		}
		cout << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}