#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		long long n, k;
		cin >> n >> k;
		
		bool on = true;
		for (int i = 0; i < n; ++i)
		{
			if (!(k & (1 << i)))
				on = false;
		}
		
		cout << "Case #" << t << ": ";
		cout << (on ? "ON" : "OFF");
		cout << endl;
	}
}