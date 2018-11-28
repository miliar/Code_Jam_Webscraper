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
#include <sstream>
#include <queue>
#include <list>
#include <string.h>
#include <fstream>

using namespace std;

int main()
{
	int test_count=0, i, j, pos1, pos2;
	int no_combine, no_clear, no_test;
	int a,b,c,d;
	char *str, *result, *rev;
	str = new char[256];
	result = new char[256];
	rev = new char[256];

	map <string,string> combine, combine_rev;
	vector <string> clear, clear_rev;
	string input, output;
	ifstream in("input.txt");
	ofstream out("output.txt");

	map<string,string>::iterator it, it_rev;

	if(!in) 
		cout << "Cannot open input file.\n";

	while(in) 
	{
		in.getline(str, 255);  
		
		no_combine = no_clear = 0;

		if(in) 
		{
			if (test_count == 0)
				no_test = atoi(str);
			else
			{
				combine.clear();
				clear.clear();
				combine_rev.clear();
				clear_rev.clear();

				result = strtok( str, " ");
				no_combine = atoi(result);
				for (i=0 ; i<no_combine ; i++)
				{
					result = strtok( NULL, " ");
					rev[0] = result[1];
					rev[1] = result[0];
					rev[2] = '\0';
					combine[string(result).substr(0,2)] = string(result).substr(2,1);
					combine_rev[string(rev)] = string(result).substr(2,1);
				}

				result = strtok( NULL, " ");
				no_clear = atoi(result);
				for (i=0 ; i<no_clear ; i++)
				{
					result = strtok( NULL, " ");
					rev[0] = result[1];
					rev[1] = result[0];
					rev[2] = '\0';
					clear.push_back(string(result));
					clear_rev.push_back(string(rev));
				}

				for (i=0 ; i<2 ; i++)
				{
					result = strtok( NULL, " ");
					input = string(result);
				}

				j=0;
				if (input.size() > 0)
				{
					output = input[j];
					j++;
					output.append(input.substr(j,1));
					j++;
				}

				while (j <= input.size())
				{
					it = combine.begin();
					it_rev = combine_rev.begin();
			
					while (it != combine.end())
					{
						a = output.find((*it).first);
						b = output.find((*it_rev).first);
						if (a != -1 && b != -1)
							pos1 = (a<b)?a:b;
						else
							pos1 = (a>b)?a:b;

						while ( pos1 != -1)
						{
							if (pos1 == output.size()-2)
								output.replace(pos1, 2, (*it).second);

							a = output.find((*it).first);
							b = output.find((*it_rev).first);
							if (a != -1 && b != -1)
								pos1 = (a<b)?a:b;
							else
								pos1 = (a>b)?a:b;

						}

					++it;
					++it_rev;
					}

					for (i=0 ; i<clear.size() ; i++)
					{
						pos1 = output.find(clear.at(i).substr(0,1));
						pos2 = output.find(clear_rev.at(i).substr(0,1));

						if (pos1 <= pos2)
						{
							a = 0;
							while ( pos1 != -1 && a != -1)
							{
								a =  output.find(clear.at(i).substr(1,1));
								output.clear();
								a = -1;
								pos1 = output.find(clear.at(i));
							}
						}
						else
						{
							a = 0;
							while ( pos2 != -1 && a != -1)
							{
								a =  output.find(clear_rev.at(i).substr(1,1));
								output.clear();
								a = -1;
								pos2 = output.find(clear_rev.at(i));
							}
						}
					}

					if (input.size() > 0 && j < input.size())
					{
						output.append(input.substr(j,1));
					}
					j++;
				}
			}

			

			if (test_count > 0)
			{
				out << "Case #" << test_count << ": [";
				for (i=0 ; i<output.size() ; i++)
				{
					out << output.substr(i,1);
					if (i != output.size()-1)
						out << ", ";
				}
				out << "]\n";
			}

			test_count++;
		}
	}

in.close();

return 0;
}





