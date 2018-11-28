// Q1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;



int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("A-large.in");
	ofstream out ("A-large.out");

	unsigned int t, n, k;
	in >> t >> ws;
	for (int i =0;i<t;i++)
	{
		in >> n >> k;
		if ((k+1)%(int)(pow(2,(double)n))==0)
		{
//			cout << "Case #" << i+1 <<": ON";
			out <<  "Case #" << i+1 <<": ON";
		}
		else
		{
//			cout << "Case #" << i+1 <<": OFF";
			out << "Case #" << i+1 <<": OFF";
		}

//		cout << endl;
		out << endl;
	}

	out.close();
	in.close();

	return 0;
}