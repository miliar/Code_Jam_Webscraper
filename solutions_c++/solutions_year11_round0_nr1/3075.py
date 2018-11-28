// codejamtemplate.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>  // I/O 
#include <fstream>   // file I/O
#include <iomanip>   // format manipulation
#include <list>
#include <ios>
#include <string>
#include <sstream>

using namespace std;

template<typename RT, typename T, typename Trait, typename Alloc>
RT ss_atoi(const basic_string<T, Trait, Alloc>& the_string)
{
    basic_istringstream< T, Trait, Alloc> temp_ss(the_string);
    RT num;
    temp_ss >> num;
    return num;
}

struct Two
{
	int move;
	int button;
};

void ProcessCase(int caseIndex, ifstream &inFile, ofstream &outFile)
{
	int N;
	inFile >> N;
	list<int> listO, listB;
	list<Two> common;	
	Two two;
	int posB = 1, posO = 1;
	for (int i = 0; i < N; i++)
	{
		string elem;
		int flag;
		inFile >> elem;
		if (elem.c_str()[0] == 'B')
			flag = 1;
		else
			flag = -1;		
		int button;
		inFile >> button;
		if (flag > 0)
			listB.push_back(button);
		else
			listO.push_back(button);
		two.move = flag;
		two.button = button;
		common.push_back(two);
	}

	int seconds = 0;
	while (listO.size() > 0 || listB.size() > 0)
	{
		Two t = common.front();
		common.pop_front();

		if (t.move > 0)
		{// B
			int time = abs(t.button - posB) + 1;
			posB = t.button;
			seconds += time;
			listB.pop_front();
			
			if (listO.size() > 0)
			{
				int t2 = abs(listO.front() - posO);
				if (t2 > 0)
				{ // if it need to move
					if (t2 <= time)
					{
						posO = listO.front();
					}
					else
					{
						if (posO > listO.front())
							posO -= time;
						else
							posO += time;
					}
				}
			}
		}
		else
		{// O
			int time = abs(t.button - posO) + 1;
			posO = t.button;
			seconds += time;
			listO.pop_front();
			
			if (listB.size() > 0)
			{
				int t2 = abs(listB.front() - posB);
				if (t2 > 0)
				{ // if it need to move
					if (t2 <= time)
					{
						posB = listB.front();
					}
					else
					{
						if (posB > listB.front())
							posB -= time;
						else
							posB += time;
					}
				}
			}
		}
	}


	outFile << "Case #" << caseIndex << ": " << seconds << "\n";
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inFile;  // declarations of streams fp_in and fp_out
	ofstream outFile;
	inFile.open("A-small-practice.in", ios::in);    // open the streams
	outFile.open("A-small-practice.out", ios::out);

	int T; // the number of cases
	inFile >> T;

	for (int i = 0; i < T; i++)
	{
		ProcessCase(i + 1, inFile, outFile);
	}

	inFile.close();   // close the streams
	outFile.close(); 

	return 0;
}
