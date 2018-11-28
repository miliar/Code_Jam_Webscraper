// jam2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <map>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>



int _tmain(int argc, _TCHAR* argv[])
{
	freopen("C:\\EmguCam\\codeJam1\\jam2\\C-small-attempt.out","wt",stdout);
	freopen("C:\\EmguCam\\codeJam1\\jam2\\test.in","rt",stdin);
	int testCases = 0, tc = 1;
	int googlers = 0, suprice = 0, minScore = 0;

	std::cin >> testCases;
	for(; tc <= testCases; tc++)
	{
		std::cin >> googlers;
		std::cin >> suprice;
		std::cin >> minScore;

		int * scores = new int[googlers];
		int idx = 0;
		int p = 0; //possible googlers
		int spesialsDetected = 0;

		for(;idx < googlers; idx++)
		{
			std::cin >> scores[idx];	
			if(scores[idx] < minScore)
				continue;
			int partial = scores[idx]/3;
			bool isSpecial = false;
			
			//spesials
			if((partial < minScore) && ((minScore-partial) <= 2))
			{
				int delta = minScore - partial;
				if(delta == 1)
				{
					if((scores[idx] % 3 == 0) && (suprice != 0))
					{
						isSpecial = true;
						suprice--;
					}
					if(scores[idx] % 3 != 0)
					{
						isSpecial = true;
					}
				}		
				if(delta == 2)
				{
					if((scores[idx] % 3 == 2) && (suprice != 0))
					{
						isSpecial = true;
						suprice--;
					}
				}
			}
			if ((partial >= minScore) || isSpecial) 
			{
				p++;
			}
		}
		std::cout << "Case #" << tc << ": "<< p << std::endl;
	}
	
	return 0;
}

