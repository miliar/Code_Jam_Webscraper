// Magicka.cpp : main project file.

#include "stdafx.h"
#include <ios>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <string>
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
		map<string,char> combs;
		int C;
		inp >> C;
		for(int c = 0; c < C; c++)
		{
			char c1;
			char c2;
			char dest;
			inp >> c1;
			inp >> c2;
			inp >> dest;
			string combo = "";
			combo += c1;
			combo += c2;
			combs[combo] = dest;
			combo = "";
			combo += c2;
			combo += c1;
			combs[combo] = dest;	
		}

		multimap<char,char> destrs;
		int D;
		inp >> D;
		for(int d = 0; d < D; d++)
		{
			char c1;
			char c2;
			inp >> c1;
			inp >> c2;
			destrs.insert(pair<char,char>(c1,c2));
			destrs.insert(pair<char,char>(c2,c1));
		}

		list<char> comms;
		int N;
		inp >> N;
		for(int n = 0; n < N; n++)
		{
			char ele;
			inp >> ele;
			if(comms.empty())
			{
				comms.push_back(ele);
			}
			else
			{
				char back = comms.back();
				string combo = "" ;
				combo += back;
				combo += ele;
				if(combs.find(combo) != combs.end())
				{
					comms.pop_back();
					comms.push_back(combs[combo]);
				}
				else
				{
					comms.push_back(ele);
					 pair<multimap<char,char>::iterator,multimap<char,char>::iterator> range;
					range = destrs.equal_range(ele);
					bool resize = false;
					if(range.first != range.second)
					{
						multimap<char,char>::iterator it;
						for (it=range.first; it!=range.second; ++it)
						{
							char checkwith = (*it).second;
							list<char>::iterator iter;

							for ( iter=comms.begin() ; iter != comms.end(); iter++ )
							{
								if(*iter == checkwith)
								{
									resize =true;
								}
							}
							if(resize)
								comms.resize(0);
						}
					}
				}
			}
		}

		ou << "Case #" << t << ": [";
		list<char>::iterator it = comms.begin();

		if(!comms.empty())
		{
			ou << comms.front();
			it++;
		}


		for ( ; it != comms.end(); it++ )
		{
			ou << ", ";
			ou << " " << *it;
		}
		ou << "]\n";
	}
	inp.close();
	ou.close();
	return 0;

}
