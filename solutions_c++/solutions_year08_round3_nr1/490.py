#include <algorithm>
#include <iostream>

using namespace std;

int
main()
{
	int cases;
	cin >> cases;
	for (int c = 1; c != cases + 1; ++c) {
		int P, // Max letters on a key
			K, // Keys available
			L; // Letters in the alphabet
		cin >> P >> K >> L;

		int *freqs = new int[L];	// Letter frequencies in message
		for (int i = 0; i != L; ++i)
			cin >> freqs[i];

		// Strategy: assign most frequent letter to each key
		// until all keys are used up. Then assign the next
		// letters as the next letter of each key
		long long presses = 0;		// Number of key presses required
		
		sort(freqs, freqs + L, greater<int>());

		int key= 0,
			position = 1;
		for (int letter = 0; letter != L; ++letter) {
///			cout << "Letter: " << letter << " Position " << position
///				<< " on Key " << key << "; hit " << freqs[letter] << " times." << endl;

			presses += position * freqs[letter];

			if (key++ == K - 1) {	// All keys used up
				key = 0;
				++position;
			}
		}
		
		cout << "Case #" << c << ": ";
		if (P * K > L) // Impossible to place letters on keys
		{}
		cout << presses << endl;

		delete[] freqs;
	}

	return 0;
}
