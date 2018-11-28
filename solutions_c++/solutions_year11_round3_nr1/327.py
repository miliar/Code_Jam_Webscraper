#include <iostream>
#include <sstream>
#include <math.h>
#include <set>
#include <vector>
#include <algorithm>


#define UInt64 unsigned long long


int main ()
{
	int	numberOfCases	= 0;
	int	counter			= 0;
	
	std::cin >> numberOfCases;
	while (counter < numberOfCases) {
		int	r	= 0;
		int	c	= 0;

		int table [50][50];

		std::cin >> r;
		std::cin >> c;
		
		bool	possible = true;
		int		numOfBlue = 0;
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				char input;
				std::cin >> input;

				if (input == '#') {
					table [i][j] = 1;
					++numOfBlue;
				} else
					table [i][j] = 0;
			}
		}

		if (numOfBlue % 4 != 0)
			possible = false;
		else {
			for (int i = 0; i < r - 1; ++i) {
				for (int j = 0; j < c - 1; ++j) {
					if (table [i][j] != 1)
						continue;

					if (table [i][j]			== 1	&&
						table [i + 1][j]		== 1	&&
						table [i][j + 1]		== 1	&&
						table [i + 1][j + 1]	== 1)
					{
						table [i][j]			= 2;
						table [i + 1][j]		= 3;
						table [i][j + 1]		= 4;
						table [i + 1][j + 1]	= 5;
					} else {
						possible = false;
						break;
					}
				}
				if (!possible)
					break;
			}
		}
		
		if (possible) {
			std::cout << "Case #" << ++counter << ":" << std::endl;
			
			for (int i = 0; i < r; ++i) {
				for (int j = 0; j < c; ++j) {
					if (table [i][j] == 0)
						std::cout << ".";
					else if (table [i][j] == 2)
						std::cout << "/";
					else if (table [i][j] == 3)
						std::cout << "\\";
					else if (table [i][j] == 4)
						std::cout << "\\";
					else if (table [i][j] == 5)
						std::cout << "/";
				}
				std::cout << std::endl;
			}
		} else
			std::cout << "Case #" << ++counter << ":" << std::endl << "Impossible" << std::endl;
	}
}