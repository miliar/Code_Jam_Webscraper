#include <NTL/ZZ.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

// Library used for Big Integer calculations : NTL
// Link to the library : http://www.shoup.net/ntl/index.html

NTL_CLIENT

ZZ ti[1001];
ZZ tif[1001];

int main()
{
	ifstream cin("B-large.in");
	ofstream cout("B-large_out.out");
	// freopen("test.in", "w", stdout);
	// freopen("A-small-attempt0.in", "r", stdin);
	// freopen("A-small.out", "w", stdout);
	// freopen("A-large.in", "r", stdin);
	// freopen("A-large-out.out", "w", stdout);
	int T;
	cin >> T;
	for(int test = 1; test <= T; ++test)
	{
		int N;
		cin >> N;
		for(int i = 0; i < N; ++i)
			cin >> ti[i];
		sort(ti, ti + N);
		int pos = 0;
		tif[pos] = ti[0];
		for(int i = 1; i < N; ++i)
			if(tif[pos] != ti[i])
			{
				++pos;
				tif[pos] = ti[i];
			}
		N = pos + 1;
		for(int i = 0; i < N - 1; ++i)
			ti[i] = tif[i + 1] - tif[i];
		ZZ gcd = ti[0];
		for(int i = 1; i < N - 1; ++i)
			gcd = GCD(gcd, ti[i]);
		// cout << gcd << endl;
		ZZ ans = gcd * ((tif[0] + gcd - 1) / gcd) - tif[0];
		cout << "Case #" << test << ": " << ans << endl;
	}

	return 0;
}