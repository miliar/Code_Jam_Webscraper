#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t != T; ++t)
	{
		int N, K;
		cin >> N >> K;

		cout << "Case #" << t + 1 << ": ";
		if (K % (1 << N) == (1 << N) - 1)
		{
			cout << "ON\n";
		}
		else
		{
			cout << "OFF\n";
		}
	}
	return 0;
}