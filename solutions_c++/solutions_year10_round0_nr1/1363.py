#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream inFile("A-large.in");
	ofstream outFile("A-large.out");

	int T;
	inFile >> T;

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		int N, K;
		inFile >> N >> K;

		bool on = true;
		for (int i = 0; on && i < N; i++, K >>= 1)
			if (!(K & 1))
				on = false;

		outFile << "Case #" << nTestCase << ": " << (on ? "ON" : "OFF") << endl;
	}

	return 0;
}
