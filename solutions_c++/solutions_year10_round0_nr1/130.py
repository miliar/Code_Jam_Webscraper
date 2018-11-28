
#include <iostream>
#include <stdint.h>

using namespace std;

void DoCase ()
{
	int64_t N;
	int64_t K;
	cin >> N;
	cin >> K;

	K += 1;

	int64_t cycle = 1;
	for (int i = 1; i <= N; ++i)
		cycle *= 2;

	if (K % cycle == 0)
		cout << "ON";
	else
		cout << "OFF";
}

main ()
{
	int cases;
	cin >> cases;

	for (int i = 1; i <= cases; ++i) {
		cout << "Case #" << i << ": ";
		DoCase ();
		cout << endl;
	}
}
