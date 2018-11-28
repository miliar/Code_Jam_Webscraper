// Dancing With the Googlers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <ostream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream i;
	std::ofstream o("temp");
	//string s;
	
	
	i.open("in.txt");
	
	int num_of_cases;
	i>>num_of_cases;
	//
	for (int jj=1; jj<=num_of_cases; ++jj) 
	{
		o<<"Case #"<<jj<<": ";
		int N,S,p;
		i>>N;
		i>>S;
		i>>p;

		int m_count = 0;
		int m_count_S = 0;
		for (int kk =0; kk<N; ++kk)
		{
			int temp;
			i>>temp;
			if (temp>= 3*p -2)
			{
				m_count++;
			}
			else if (temp>= 3*p - 4 && temp>0)
			{
				m_count_S++;
			}
		}
		if (m_count_S <=S)
		{
			m_count+= m_count_S;
		}
		else
		{
			m_count+=S;
		}
		o<<m_count<<std::endl;

		

	}

	return 0;
}

