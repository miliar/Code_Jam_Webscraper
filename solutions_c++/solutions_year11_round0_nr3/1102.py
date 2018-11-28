#include <iostream>

using namespace std;
int test;
void go()
{
	cout << "Case #" << ++test << ": ";
	int n;
	cin >> n;
	int x = 0;
	int small = 0;
	int total = 0;
	for (int i = 0; i < n; ++i)
	{
		int y; cin >> y;
		if (i == 0) {small = x = total = y; continue;}
		x ^= y;
		if (y < small) small = y;
		total += y;
	}
	if (x) cout << "NO\n";
	else cout << total - small << '\n';
}
int main()
{
	int t;
	cin >> t;
	while (t--) go();
	return 0;
}
