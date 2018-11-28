// Bot_Trust.cpp : main project file.

#include "stdafx.h"
#include <ios>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
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

		int k;
		char last = 'N';
		char next = 'N';
		int extra = 0;
		int Bpos = 1;
		int Opos = 1;
		int turns = 0;

		for(int n = 0; n < N; n++)
		{
			inp >> next;
			inp >> k;
			if(next == last)
			{
				if(next == 'B')
				{
					turns += abs(k - Bpos) + 1;
					extra += abs(k - Bpos) + 1;
					Bpos = k;
				}
				else
				{
					turns += abs(k - Opos) + 1;
					extra += abs(k - Opos) + 1;
					Opos = k;
				}
			}
			else
			{
				if(next == 'B')
				{
					if(abs(k - Bpos) < extra)
					{
						turns += 1;
						extra = 1;
					}
					else
					{
						turns += (abs(k - Bpos) - extra) + 1;
						extra = (abs(k - Bpos) - extra) + 1;
					}
					Bpos = k;
				}
				else
				{
					if(abs(k - Opos) < extra)
					{
						turns += 1;
						extra = 1;
					}
					else
					{
						turns += (abs(k - Opos) - extra) + 1;
						extra = (abs(k - Opos) - extra) + 1;
					}
					Opos = k;
				}
			}
			last = next;
			
		}

		ou << "Case #" << t << ": " << turns << "\n";
		cout << "Case #" << t << ": " << turns << "\n";

	}
	inp.close();
	ou.close();
	return 0;

}
