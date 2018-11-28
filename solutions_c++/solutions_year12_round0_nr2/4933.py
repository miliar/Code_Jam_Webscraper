// GoogleCodeJam-cpp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <conio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{

	/*char *input[5];
	input[0]="4\n";
	input[1]="3 1 5 15 13 11\n";
	input[2]="3 0 8 23 22 21\n";
	input[3]="2 1 1 8 0\n";
	input[4]="6 2 8 29 20 8 18 18 21\n";*/

	//no surprise: x+y+z= 3x +|- 1|2 | 3*min(x,y,z) + 0|1|2
	//surprise: 3*min(x,y,z) + 0|1|2 + 0|1|2
	//ex: 2: 3 0 8 23 22 21 => no surprises so
	//	23=3*min(x,y,z) + 0|1|2 => odd but not div 3 => 3x+1 but 22 ndiv 3 so 3x+2 => 7 8 8
	//	22=3*min(x,y,z) + 0|1|2 => 22 = 21r1 = 7 7 8
	//	21=3*min(x,y,z) + 0|1|2 => 21 = 7 7 7
	//	case #2: 2
	//
	//ex: 2 1 1 8 0 => 1 surprise but with a 0 and p = 1
	// case #3: 1
	// 8 = 6r2 = 2 2 4
	// 8 = 3r5 = 1+1 1+1 1+3
	//ex: 3 1 5 15 13 11 => 1 surprise and p=5
	// 15 = 5 5 5 yes OR 12r3 = 4 5 6 no
	// 13 = 12r1 = 4 4 5 yes OR 9r4 = 3 5 5 yes
	// 11 = 9r2 = 3 4 4 OR 9r2 = 3 3 5 yes
	// 3
	// ex: 6 2 8 29 20 8 18 18 21 => 2 surprises and p = 8
	// 29 = 27r2
	// 20 = 18r2
	// 8 = 6r2 = 2 3 3 OR no no no
	// 18 = 6 6 6
	// 18 = 6 6 6
	// 21 = 7 7 7
	// for p = 8, min is 6 6 8 so 20. so only 3 are possible
	// for no surprises all number >= 2(p-1)+p
	// add to that the surprises S numbers that are >= 2(p-2)+p and not already accounted for.
	// 3p-2 vs 3p-4
	// for each in scores >= 3p-2 count++ else if surprises remaining and >= 3p-4 count++

	// for each in scores >= 3p-2 count++ else if surprises remaining and >= 3p-4 count++
	//for (int caseNum = 1; caseNum <= 100; caseNum++)
	string line;
	ifstream myfile ("b-large.in");
	if (myfile.is_open())
	{
		bool bSkippedFirstLine = false;
		int caseNum = 1;
		while ( myfile.good() )
		{
			if (!bSkippedFirstLine)
			{
				getline (myfile,line);
				bSkippedFirstLine = true;
			}
			getline (myfile,line);

			stringstream stream(line);
			string word;

			int wordIndex = 0;
			int surprises = 0;
			int threshold = 0;
			int positives = 0;
			while( getline(stream, word, ' ') )
			{
				switch(wordIndex)
				{
					case 0:
					{
						break;
					}
					case 1:
					{
						surprises = atoi(word.c_str());
						break;
					}
					case 2:
					{
						threshold = atoi(word.c_str());
						break;
					}
					default:
					{
						int score = atoi(word.c_str());
						if (score >= 3*threshold-2)
						{
							positives++;
						}
						else if (0 < surprises)
						{
							if (1 == threshold)
							{
								if (0 < score)
								{
									surprises--;
									positives++;
								}
							}
							else if (score >= 3*threshold-4)
							{
								surprises--;
								positives++;
							}
						}
						break;
					}
				}

				wordIndex++;
			}
			cout << "Case #" << caseNum++ << ": " << positives << "\n";
		}

		myfile.close();
	}

	else cout << "Unable to open file"; 


	_getch();

	return 0;
}
