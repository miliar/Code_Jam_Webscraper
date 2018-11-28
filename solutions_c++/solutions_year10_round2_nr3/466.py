#include <iostream>
#include <fstream>
#include <vector>
#include <bitset>
#include <algorithm>

using namespace std;

int main()
{
	ifstream inFile("C-small-attempt1.in");
	ofstream outFile("C-small-attempt1.out");

	int T;
	inFile >> T;

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		int n;
		inFile >> n;

		int y = -1;
		if (n == 2)
			y = 1;
		else
		{
			vector<int> ranks(n + 1);
			unsigned mask = 1;
			mask <<= n - 2;
			mask--;
			y = 0;
			for (unsigned i = 0; i <= mask; i++)
			{
				fill(ranks.begin(), ranks.end(), 0);
				bitset<sizeof(unsigned) * 8> m(i);
				int r = 1;
				for (int j = 0; j < n - 2; j++)
					if (m[j])
						ranks[j + 2] = r++;
				ranks[n] = r;
				while (r > 1)
					r = ranks[r];
				if (r == 1)
				{
					y++;
					y %= 100003;
				}
			}
		}


		outFile << "Case #" << nTestCase << ": " << y << endl;
	}

	return 0;
}
