#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int tc = 0; tc < t; tc++)
	{
		int n, k;
		cin >> n >> k;
		if((k + 1) % (1 << n) == 0)
			cout << "Case #" << (tc + 1) << ": " << "ON" << endl;
		else
			cout << "Case #" << (tc + 1) << ": " << "OFF" << endl;
	}
	return 0;
}

