#include <iostream>

using namespace std;

int main()
{
	int C, N, K;
	cin >> C;
	for (int c = 1; c <= C; c++)
	{
		int mask;
		cin >> N >> K;
		
		mask = 1;
		while (K & mask)
			mask = mask << 1;

		if ( mask >= (1 << N) )
			cout << "Case #" << c << ": " << "ON" << endl;
		else
			cout << "Case #" << c << ": " << "OFF" << endl;
	}
	return 0;
}
