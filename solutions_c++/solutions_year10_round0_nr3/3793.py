/**
 * [brief]
 *
 *  @author chris.bisnett
 *  @date May 8, 2010 chris.bisnett - Initial creation
 *
 **/

#include <iostream>
#include <vector>

using namespace std;

int main()
{
	unsigned int tc = 0;	// Test cases
	unsigned int c = 1;		// Current case
	unsigned int R = 0;		// Rides
	unsigned int k = 0;		// Maximum occupancy
	unsigned int N = 0;		// Number of groups
	vector<unsigned int> g;	// Groups
	unsigned int money = 0;	// Total money made
	unsigned int l = 0;		// Inded of the first group on the ride
	unsigned int i = 0;		// Index of first group in line
	unsigned int tmp = 0;	// Temporary holder

	// Get the number of test cases
	cin >> tc;

	// Loop the test cases
	while (c <= tc)
	{
		// Initialize the variables
		R = k = N = money = 0;
		g.clear();

		// Get the info
		cin >> R >> k >> N;

		// Get the groups
		while (N--)
		{
			cin >> tmp;
			g.push_back(tmp);
		}

		//cout << "R: " << R << endl << "k: " << k << endl << "N: " << g.size() << endl;
		//for (unsigned int i = 0; i < g.size(); i++)
		//	cout << g[i] << endl;

		i = l = 0;
		// Loop the rides
		while (R--)
		{
			tmp = 0;
			l = i;

			// Add the groups to the ride
			while ((tmp + g[i]) <= k)
			{
				// Add the next group
				tmp += g[i++];

				// Wrap the line
				if (i >= g.size())
					i = 0;

				// The same group can't get on the ride twice
				if (i == l)
					break;
			}

			// Add the money for this ride
			money += tmp;
		}

		cout << "Case #" << c++ << ": " << money << endl;
	}

	return 0;
}
