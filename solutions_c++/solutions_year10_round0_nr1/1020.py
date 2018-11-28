#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int
main (
	int argc,
	char **argv
) {
	if (argc < 2)
	{
		cerr << "no input data specified." << endl;
		return -1;
	}

	fstream fin(argv[1], ios::in);

	int T;
	fin >> T;

	for (int t = 0; t < T; t++)
	{
		long N, K;
		fin >> N >> K;

		//cerr << "N: " << N << ", K: " << K << endl;

		cout << "Case #" << (t + 1) << ": ";

		for (long n = 0; n < N; n++)
		{
			if ((K / (1 << n)) % 2 == 0)
			{
				cout << "OFF" << endl;
				goto next;
			}
		}

		cout << "ON" << endl;

	next:
		;
	}

	fin.close();

	return 0;
}
