
	#include <iostream>
	#include <string>

	using namespace std;

	bool SnapperChainState (int NumSnappers, int NumSnaps)
	{
		unsigned long M = (1UL << (unsigned long)NumSnappers) - 1;

		return M == (NumSnaps & M);
	}

	int main ()
	{
		int TestCases, NumSnappers, NumSnaps;

		cin >> TestCases;

		for (int TestCase = 0; TestCase++ < TestCases; )
		{
			cin >> NumSnappers;
			cin >> NumSnaps;

			cout << "Case #" << TestCase << ": " 
				 << (SnapperChainState(NumSnappers,NumSnaps) ? "ON" : "OFF") << endl;
		}

		return 0;
	}