#include <iostream>
#include <iomanip>
using namespace std;

typedef unsigned long long NATURAL;


bool snapper_chain(NATURAL n, NATURAL k)
{
	return ((k+1) & ((1 << n) - 1)) == 0;
}


int main(void)
{
	NATURAL T, N, K;
	NATURAL case_nr;

	cin >> T;
	for (case_nr = 1; case_nr <= T; case_nr++)
	{
		cin >> N >> K;
		bool res = snapper_chain(N, K);
		cout << "Case #" << case_nr << ": " << (res ? "ON" : "OFF") << endl;
	}

	return 0;
}

