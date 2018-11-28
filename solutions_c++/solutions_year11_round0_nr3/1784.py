#include <iostream>
#include <string>
#include <fstream>
#include <cstdio>
#include <deque>

#define forl(i,a,b) for(int i = a; i < b; ++i)

using namespace std;


main()
{
	int t;
	cin >> t;
	forl(i,1,t+1) {
		int n;
		cin >> n;
		long tot = 0;
		long sum = 0;
		long sml = 10000000;
		forl(k,0,n)
		{
			int num;
			cin >> num;
			if (sml > num) sml = num;
			tot ^= num;
			sum += num;
		}
		cout << "Case #" << i << ": ";
		if (!tot) cout << (sum-sml) << endl;
		else cout << "NO" << endl;
	}
}

