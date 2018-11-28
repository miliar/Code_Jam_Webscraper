// new.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iosfwd>
#include <string>
#include <list>

int _tmain(int argc, _TCHAR* argv[])
{
	using namespace std;
	ifstream in;
	ofstream out;
	in.open("C:\\A-large.in");
	out.open("C:\\A-large.out");
	int n_cases, n_engines, n_queries;
	
	int i, j, k, t;

	string s[101];
	int sFlag[100];
	for (i=0;i<100;++i)
	{
		s[i] = ' ';
		sFlag[i] = 0;
	}
	int n_CurrentQ;
	int switches;
	switches = 0;



	string current;
	in>>n_cases;
	for (i=0;i<n_cases;++i)
	{
		in>>n_engines;
		getline(in,s[100]);
		for (j=0;j<n_engines;++j)
		{
			getline(in,s[j]);
		}
		in>>n_queries;
		getline(in,s[100]);
		n_CurrentQ = 0;
		for (k=0;k<n_queries;++k)
		{
			getline(in, current);
			for (j=0;j<n_engines;++j)
			{

				if (sFlag[j] == 0)
				{

					if (s[j] == current)
					{
						sFlag[j] = 1;
						n_CurrentQ++;
						if (n_CurrentQ == n_engines)
						{
							switches++;
							for (t=0;t<100;++t)
							{
								sFlag[t] = 0;
							}
							sFlag[j] = 1;
							n_CurrentQ = 1;
						}

					}

				}
			}
		}
		for (t=0;t<100;++t)
		{
			s[t] = ' ';
			sFlag[t] = 0;
		}
		out<<"Case #"<<i+1<<": "<<switches<<endl;
		switches = 0;
	}

	in.close();
	out.close();
	return 0;
}

