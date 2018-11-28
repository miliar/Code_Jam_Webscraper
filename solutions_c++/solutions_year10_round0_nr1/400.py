#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

typedef long long i64;

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	i64 tcn, n, k;
	cin >> tcn;
	for (int tc = 1; tc <= tcn; tc++)
	{
		cin >> n >> k;
	
	    cout << "Case #" << tc << ": ";
	    if (k % (1 << n) == (1 << n) - 1)
	    	cout << "ON" << endl;
	    else
	    	cout << "OFF" << endl;
	}

	return 0;
}
