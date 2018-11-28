#include <iostream>
#include <cstdio>

using std::cin;
using std::cout;
using std::endl;

int
main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int z = 1; z <= T; z++)
	{
		int N, K;
		cin >> N >> K;
		int p = 1 << N;
		cout << "Case #" << z << ": ";
		if (K % p == p - 1)
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
	return(0);
}
