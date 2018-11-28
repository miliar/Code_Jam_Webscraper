#include <iostream>
using namespace std;

bool solve(unsigned int n, unsigned int k)
{
	unsigned int m = (0x01 << n) - 1;
	return (k & m) == m;
}

int main()
{
	int t = 0;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		unsigned int n = 0, k = 0;
		cin >> n >> k;
		bool on = solve(n, k);
		cout << "Case #" << i + 1 << ": " << (on ? "ON" : "OFF") << endl;
	}
	return 0;
}
