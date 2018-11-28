#include <fstream>
#include <iostream>
using namespace std;

int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");

	long long test_cases, j, p, number_of_players, start, end, solved, players[100];
	fin >> test_cases;

    for (int kase = 0; kase < test_cases; kase++)
    {
		fin >> number_of_players >> start >> end;
		for (p = 0; p < number_of_players; p++)
			fin >> players[p];

		for (j = start; j <= end; j++)
		{
			solved = 1;
			for (p = 0; p < number_of_players; p++)
				if (players[p] % j && j % players[p])
				{
					solved = 0;
					break;
				}

			if (solved)
				break;
		}

		if (solved)
			fout << "Case #" << (kase + 1) << ": " << j << endl;
		else
			fout << "Case #" << (kase + 1) << ": NO" << endl;
    }

	return 0;
}

