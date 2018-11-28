// Candy_Splitting.cpp : main project file.
#include "stdafx.h"
#include <ios>
#include <iostream>
#include <fstream>
#include <list>
using namespace std;

int main(array<System::String ^> ^args)
{
	fstream inp;
	inp.open("input.in");
	fstream ou("out.txt");
	int T;
	inp >> T;
	for(int t = 1; t <= T; t++)
	{
		int N;
		inp >> N;
		int PD;
		inp >> PD;
		int PG;
		inp >> PG;
		bool result = true;
		if((PG != 0 && PG != 100))
		{
			double checkvalue = ((double)PD/100.0)* N;
			if(checkvalue < 1)
			{
				result = false;
			}

			else if(N < 100)
			{
				int reduced = PD;
				if(reduced % 2 == 0)
				{
					reduced /= 2;
				}
				if(reduced % 2 == 0)
				{
					reduced /= 2;
				}
				if(reduced % 5 == 0)
				{
					reduced /= 5;
				}
				if(reduced % 5 == 0)
				{
					reduced /= 5;
				}
				double calc = 100.0/PD;
				if(calc*reduced > N)
					result = false;
			}
		}
		else if(PG != PD)
		{
			result = false;
		}
		if(result)
			ou << "Case #" << t << ": " << "Possible" << "\n";
		else
			ou << "Case #" << t << ": " << "Broken" << "\n";
	}
	inp.close();
	ou.close();
	return 0;

}
