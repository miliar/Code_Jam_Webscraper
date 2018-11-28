/* 
 * File:   main.cpp
 * Author: tom
 *
 * Created on 22 May 2011, 10:04 PM
 */

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

vector<int> playerFreq;

int main()
{
	ifstream in("in");
	ofstream out("out");

	int numT;
	in >> numT;

	for (int t = 1; t <= numT; t++)
	{
		out << "Case #" << t << ": ";

		int numPlayers, min, max;
		in >> numPlayers >> min >> max;

		playerFreq = vector<int>(numPlayers);

		for (int i = 0; i < numPlayers; i++)
		{
			in >> playerFreq[i];
		}
		
		bool possible = false;
		int pF;
		int f;
		for (f = min; !possible && f <= max; f++)
		{
			possible = true;

			for (int p = 0; p < numPlayers; p++)
			{
				pF = playerFreq[p];
				if (f < pF)
				{
					if (pF % f != 0)
					{
						possible = false;
						break;
					}
				}
				else if (f > pF)
				{
					if (f % pF != 0)
					{
						possible = false;
						break;
					}
				}
			}
		}

		if (possible)
			out << f - 1 << "\n";
		else
			out << "NO" << "\n";
	}

	return 0;
}

