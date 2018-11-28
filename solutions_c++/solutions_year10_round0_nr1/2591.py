#include <iostream>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 0; tc < t; tc++)
	{
		int n, k;
		cin >> n >> k;
		printf("Case #%d: ", tc + 1);
		if((((1 << n) - 1) & k) == (1 << n) - 1)
			cout << "ON";
		else
			cout << "OFF";
		cout << endl;
	}
	return 0;
}