/**
 * Google code jam 2010 Qualification Round
 * A. Snapper Chain
 * snapper.cc
 *
 * singleheart@gmail.com
 */

#include <cstdio>
#include <fstream>

using namespace std;

int main(int argc, char* argv[])
{
	ifstream fin(argv[1]);

	int T;
	fin >> T;

	for (int i=1; i <= T; ++i)
	{
		unsigned int N, K;
		fin >> N >> K;

		unsigned int mask = (1 << N) - 1; // N 1's
		const char* y = ((K & mask) == mask) ? "ON" : "OFF";
		printf("Case #%d: %s\n", i, y);
	}
}
