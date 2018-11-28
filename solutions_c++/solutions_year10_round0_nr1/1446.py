#include <iostream>
#include <cstdio>

using namespace std;

int pow (int a, int p)
{
	return p == 0 ? 1 : a * pow(a, p - 1);
}

int main ()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		int x, y;
		cin >> x >> y;
		cout << "Case #" << i + 1 << ": ";
		cout << ((y + 1) % pow(2, x) == 0 ? "ON" : "OFF") << endl;
	}
}

