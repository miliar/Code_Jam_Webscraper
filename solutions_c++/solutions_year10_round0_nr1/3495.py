#include <iostream>
using namespace std;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int n, k;
		cin >> n >> k;
		cout << "Case #" << i << ": " << (((1 << n) - 1 == k % (1 << n)) ? "ON" : "OFF") << endl; 
	}
	return 0;
}