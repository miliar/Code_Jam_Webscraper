#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
	ifstream inFile("C-small-attempt0.in");
	ofstream outFile("C-small-attempt0.out");

	int T;
	inFile >> T;

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		int R, k, N;
		inFile >> R >> k >> N;
		vector<int> g(N);
		for (int i = 0; i < N; i++)
			inFile >> g[i];
		int head = 0;
		unsigned long long money = 0;

		while (R > 0)
		{
			R--;
			int load = k;
			int oldHead = head;
			while (load > 0)
			{
				if (g[head] > load)
					break;
				load -= g[head];
				money += g[head];
				head = (head + 1) % N;
				if (head == oldHead)
					break;
			}
		}

		outFile << "Case #" << nTestCase << ": " << money << endl;
	}

	return 0;
}
