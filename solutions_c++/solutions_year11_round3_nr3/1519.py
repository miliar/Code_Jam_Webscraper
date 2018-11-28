// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently, but
// are changed infrequently
//

#pragma once

#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <iomanip>
#include <sstream>
#include <queue>
#include <list>
#include <string.h>
#include <fstream>
#include <conio.h>

using namespace std;



int main()
{
	int test_count=0, no_test;

	int n, flag;

	int low,high,lcm;

	int i,j,k;

	string str;

	vector <int> freq;

	ifstream in("input.txt");
	ofstream out("output.txt");

	if(!in) 
		cout << "Cannot open input file.\n";

	while(in) 
	{
		if(in) 
		{
			if (test_count == 0)
			{
				in >> str; 
				no_test = atoi(str.c_str());
			}
			else
			{
				freq.clear();
				if (test_count > no_test)
					break;

				in >> str; 
				n = atoi(str.c_str());

				in >> str; 
				low = atoi(str.c_str());

				in >> str; 
				high = atoi(str.c_str());

				for (i=0 ; i<n ; i++)
				{
					in >> str; 
					freq.push_back(atoi(str.c_str()));
				}

				flag = 0;
				for (k=low ; k<=high ; k++)
				{
					for (i=0 ; i<freq.size() ; i++)
					{
						if (k%freq.at(i) == 0 || freq.at(i)%k == 0)
						{
							flag = 1;
						}
						else
						{
							flag = 0;
							break;
						}
					}
					if (flag == 1)
					{
						lcm = k;
						break;
					}
				}
				
				if (test_count > 0)
				{
					if (flag == 0)
						out << "Case #" << test_count << ": " << "NO" << endl;
					else
						out << "Case #" << test_count << ": " << lcm << endl;
				}
				
			}
			test_count++;
		}
	}

in.close();

return 0;
}


