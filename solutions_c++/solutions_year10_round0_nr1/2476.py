#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char* argv[])
{
	ifstream infile;
	infile.open("A-large.in");

	int test_cases = 0;
	infile >> test_cases;

	for (int i = 0; i < test_cases; i++)
	{
		int snappers = 0, snaps = 0;
		infile >> snappers >> snaps;

		int possible_combos = (1 << snappers);
		if (possible_combos - 1 == snaps % possible_combos)
			printf("Case #%i: ON\n", i + 1);
		else
			printf("Case #%i: OFF\n", i + 1);
	}

	return 0;
}