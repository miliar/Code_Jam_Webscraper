#include <iostream>
#include <cstdlib>

using namespace std;

int pow(int x, int n)
{
	int z = 1;
	for ( int i = 1; i <= n; i++)
	{
		z *= x;
	}
	return z;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;

	int N, K;
	for ( int i = 1; i <= T; i++)
	{
		cin >> N >> K;
		int res = pow(2, N);
		if ( K % res == res - 1)
		{
			cout << "Case" << " " << "#" << i << ":" << " " << "ON" << endl;
		}
		else
		{
			cout << "Case" << " " << "#" << i << ":" << " " << "OFF" << endl;
		}
	}
}