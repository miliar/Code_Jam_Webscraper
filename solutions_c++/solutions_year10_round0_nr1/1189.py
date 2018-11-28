#include<iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int x = 1; x <= T; ++x)
	{
		unsigned N, K;
		cin >> N >> K;

		cout << "Case #" << x;

		unsigned const _2_N_1 = (1 << N) - 1;

		if((K & _2_N_1) == _2_N_1)
			cout << ": ON\n";
		else
			cout << ": OFF\n";
	}

	return 0;
}