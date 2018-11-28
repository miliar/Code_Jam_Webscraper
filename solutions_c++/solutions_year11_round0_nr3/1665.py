// Candy_Splitting.cpp : main project file.
#include "stdafx.h"
#include <ios>
#include <iostream>
#include <fstream>
#include <list>
using namespace std;

int SplitCandy(list<int> remaining, list<int> chosen, int chosenX, int sum, int leftX, int osum)
{
	if(remaining.size() == 1)
	{
		if(chosen.size() == 0)
			return -1;
		if(chosenX == leftX)
			return sum;
		else
			return -1;
	}
	else
	{
		if(chosenX == leftX &&  chosen.size() != 0 && remaining.size() != 0)
			return sum;
		else
		{
			for(int i = 0; i < remaining.size(); i++)
			{
				list<int> nextc = chosen;
				int nvalue = remaining.front();
				remaining.pop_front();
				nextc.push_back(nvalue);
				int ncx = chosenX^nvalue;
				int nsum = sum - nvalue;
				int nlx = leftX^nvalue;
				int nosum = osum + nvalue;
				int nresult = SplitCandy(remaining, nextc, ncx, nsum, nlx, osum);
				if(nresult > 0)
					return nresult;
				remaining.push_back(nvalue);
				if(nsum < nosum)
					break;
			}
		}
	}
	return -1;
}

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
		list<int> values;
		int total = 0;
		int XOR = 0;
		for(int n = 0; n < N; n++)
		{
			int C;
			inp >> C;
			total += C;
			XOR = XOR^C;
			values.push_back(C);
		}
		list<int> taken;
		values.sort();
		int value;
		if(XOR == 0)
			value = SplitCandy(values, taken, 0, total, XOR, 0);
		else
			value = -1;

		if(value > 0)
			ou << "Case #" << t << ": " << value << "\n";
		else
			ou << "Case #" << t << ": " << "NO" << "\n";
	}
	inp.close();
	ou.close();
	return 0;

}
