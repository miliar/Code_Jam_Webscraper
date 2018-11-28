// C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
#include <cassert>
#include <map>
#include <set>
using namespace std;
ifstream in("C-large.in");
ofstream out("out.txt");


int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	in >> T;
	for(int i = 0;i<T;++i)
	{
		int n;
		in >> n;
		int acum = 0;
		int total = 0;
		int min = 100000000;
		for(int j = 0;j < n;++j)
		{
			int val;
			in >> val;
			acum ^= val;
			total += val;
			if(val < min)
				min = val;
		}
		out << "Case #" << (i+1) << ": ";
		if(acum == 0)
			out << (total-min);
		else 
			out << "NO";

		out << endl;
			
	}

	return 0;
}

