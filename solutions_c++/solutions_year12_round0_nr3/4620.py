#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
#include <vector>
#include <sstream>
#include <math.h>
#include <map>
#include <set>

using namespace std;

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	#endif
	
	int q = 0;
	cin >> q;
	for (int _ = 1; _ <= q; _++)
	{
		set<long> mm;
		
		long long a, b;
		long long ans = 0;


		cin >> a >> b;
		string s = "", s1 = "";

		for (long n = a; n < b; n++)
		{
			long x = n;
			s1 = "";

			while (x > 0)
			{
				s1 = (char)((x%10) + '0') + s1;
				x /= 10;
			}
			
			for (int i = 1; i < s1.length(); i++)
			{	
				s = s1.substr(i) + s1.substr(0, i);
				
				long m = atol(s.c_str());
				
				if (m > n && m <= b)
				{
					ans++;
				}
			}
		}
		cout << "Case #" << _ << ": " << ans << endl;
	}
	
	
	return 0;
}