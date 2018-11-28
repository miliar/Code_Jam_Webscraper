// Codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ofstream out; out.open ("out.txt");
	ifstream in("in.txt");
	int wires[10000][2];
	

	int cases;
	in>>cases;
	for (int tc=1; tc<=cases; tc++)
	{
		memset(wires,0,sizeof(wires));
		int count;
		in>> count;

		int intersects = 0;
		for (int i=0; i<count; i++)
		{
			in>>wires[i][0];
			in>>wires[i][1];
			for (int j=0; j<i; j++)
				if ((wires[j][0] - wires[i][0]) * (wires[j][1] - wires[i][1])<0)
					intersects++;
		}

		out<<"Case #"<<tc<<": "<<intersects<<"\n";

	}


	out.close();
	in.close();
	
	return 0;
}

