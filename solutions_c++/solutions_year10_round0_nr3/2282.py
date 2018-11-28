
	#include <iostream>
	#include <string>

	using namespace std;

	int main ()
	{
		int TestCases, NumRounds, NumSeats, NumGroups;
		int NextGroup, TotalIncome, *GroupSize;
		int i, g;

		cin >> TestCases;

		for (int TestCase = 0; TestCase++ < TestCases; )
		{
			cin >> NumRounds;
			cin >> NumSeats;
			cin >> NumGroups;

			int *GroupSize = new int[NumGroups];

			for (i = 0; i < NumGroups; i++) cin >> GroupSize[i];

			NextGroup = TotalIncome = 0;

			while (NumRounds--)
			{
				int SeatsLeft = NumSeats;
				
				for (i = 0, g = NextGroup; i < NumGroups; i++, g++)
				{
					/* Wraparound. */
					if (g >= NumGroups) g -= NumGroups;

					if (SeatsLeft < GroupSize[g])
						break;

					TotalIncome += GroupSize[g];
					SeatsLeft -= GroupSize[g];
				}

				NextGroup = g;
			}

			cout << "Case #" << TestCase << ": " << TotalIncome << endl;
		}

		return 0;
	}