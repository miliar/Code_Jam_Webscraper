//============================================================================
// Name        : task1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <stdint.h>
#include <string>

void getCheckNums(std::string s1[4],
		uint16_t& ox,
		uint16_t& oo,
		bool& hasdots)
{
	int ctr = 0;
	for (int i = 0; i < 4; ++i)
	{
		std::string& s = s1[i];
		for (int j = 0; j < 4; ++j)
		{
			switch(s[j])
			{
			case 'T':
				ox |= ((1 << j) << ctr);
				oo |= ((1 << j) << ctr);
				break;

			case 'O':
				oo |= ((1 << j) << ctr);
				break
				;
			case 'X':
				ox |= ((1 << j) << ctr);
				break;

			case '.':
				hasdots = true;
				break;
			}
		}
		ctr += 4;
	}
}

uint16_t masks[] =
{
		0xf000,
		0x0f00,
		0x00f0,
		0x000f,

		0x8888,
		0x4444,
		0x2222,
		0x1111,

		0x8421,
		0x1248
};

int main()
{
	std::fstream f;
	f.open("A-large.in");

	int T = 0;
	f >> T;

	for (int i = 0; i < T; ++i)
	{
		std::string rows[4];
		f >> rows[0];
		f >> rows[1];
		f >> rows[2];
		f >> rows[3];

		uint16_t ox = 0;
		uint16_t oo = 0;

		bool hasdots = false;
		getCheckNums(rows, ox, oo, hasdots);

		bool ok = false;
		for (int n = 0; n < 10; ++n)
		{
			if ((oo & masks[n]) == masks[n])
			{
				std::cout << "Case #" << i+1 << ": O won" << std::endl;
				ok = true;
				break;
			}
		}

		if (!ok)
		{
			for (int n = 0; n < 10; ++n)
			{
				if ((ox & masks[n]) == masks[n])
				{
					std::cout << "Case #" << i+1 << ": X won" << std::endl;
					ok = true;
					break;
				}
			}
		}

		if (!ok)
		{
			if (hasdots)
			{
				std::cout << "Case #" << i+1 << ": Game has not completed" << std::endl;
			}
			else
			{
				std::cout << "Case #" << i+1 << ": Draw" << std::endl;
			}
		}
	}
}












