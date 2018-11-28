
#include <iostream>
#include <vector>
#include <cstdlib>

main ()
{
	int cases;
	std::cin >> cases;

	for (int x = 1; x <= cases; ++x) {
		int presses;
		std::cin >> presses;
		std::vector<char> colours;
		std::vector<int> blue, orange;
		for (int p = 0; p < presses; ++p) {
			char c;
			std::cin >> c;
			int button;
			std::cin >> button;
			colours.push_back (c);
			if (c == 'B')
				blue.push_back (button);
			else
				orange.push_back (button);
		}
		blue.push_back (1);
		orange.push_back (1);
		int time = 0;
		std::vector<char>::iterator cPos = colours.begin ();
		std::vector<int>::iterator bPos = blue.begin ();
		std::vector<int>::iterator oPos = orange.begin ();
		int bLoc = 1;
		int oLoc = 1;
		while (cPos != colours.end ()) {
			if (*cPos == 'B') {
				++cPos;
				int thisTime = std::abs (*bPos - bLoc) + 1;
				time += thisTime;
				bLoc = *bPos;
				int distNeeded = std::abs (*oPos - oLoc);
				int distTraveled = std::min (thisTime, distNeeded);
				if (oLoc > *oPos)
					oLoc -= distTraveled;
				else
					oLoc += distTraveled;
				++bPos;
			} else {
				++cPos;
				int thisTime = std::abs (*oPos - oLoc) + 1;
				time += thisTime;
				oLoc = *oPos;
				int distNeeded = std::abs (*bPos - bLoc);
				int distTraveled = std::min (thisTime, distNeeded);
				if (bLoc > *bPos)
					bLoc -= distTraveled;
				else
					bLoc += distTraveled;
				++oPos;
			}
		}
		std::cout << "Case #" << x << ": " << time << std::endl;
	}

}

