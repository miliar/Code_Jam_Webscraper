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

	int n,d,g,pd,pg, flag1=0,flag2=0;

	int i,j,k;

	double res1,res2;

	char *str;
	str = new char[8196];

	string input, output;
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
				no_test = atoi(str);
			}
			else
			{
				flag1=0,flag2=0;

				if (test_count > no_test)
					break;

				in >> str; 
				n = atoi(str);
				in >> str; 
				pd = atoi(str);
				in >> str; 
				pg = atoi(str);

				for (i=1 ; i<=n ; i++)
				{
					res1 = ((double)i*(double)pd)/100;
					if ((res1 - (int)res1 == 0))
					{
						flag1 = 1;
						break;
					}
				}

				if (pg == 100 && pd!= 100)
					flag2 = -1;

				j=1; 
				while (flag2 == 0)
				{
					res2 = ((double)j*(double)pg)/100;
					if ((res2 - (int)res2 == 0) )
					{
						flag2 = 1;
						break;
					}
					j++;
				}

				if ((j < i) || (flag2 == 1 && (res2 < res1)))
					flag2 = -1;

				if (test_count > 0)
				{
					if (flag1 == 1 && flag2 == 1)
						out << "Case #" << test_count << ": Possible" << endl;
					else
						out << "Case #" << test_count << ": Broken" << endl;
				}
				
			}
			test_count++;
		}
	}

in.close();

return 0;
}

