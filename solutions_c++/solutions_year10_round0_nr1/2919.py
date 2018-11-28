// snapper.cpp : définit le point d'entrée pour l'application console.
//

#include "stdafx.h"
#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>



bool comp (int N, int K)
{

		bool result = false;

		if (N ==0 || K ==0)
			return false;
	int comp = 0;

	 for(int i = 0 ; i < N ; i++)
	 {
		 comp = comp << 1;
		 comp += 1;

	 }
	
	 
	 if((comp & K) == comp)
		 result = true;

	 return result;

}


int _tmain(int argc, _TCHAR* argv[])
{
	
	std::ifstream myInput ("d:\\A-large.in");
	if(!myInput)
		return 0;

	int maxCase;
	myInput >> maxCase;

	

	int count = 1;

	std::ofstream myOutput("d:\\output.txt");

	for(;count <=maxCase ; count ++)
	{	
		
		int nFromFile, kFromFile;
		myInput >> nFromFile;
		myInput >> kFromFile;

		bool temp = comp(nFromFile,kFromFile);

		char * output = new char[64];

		sprintf(output,"Case #%d: %s\n",  count, temp==true?"ON":"OFF");
	//	printf("Case #%d:\t%s\n", j,i, count, temp==true?"ON":"OFF");
		
		myOutput << output;

		delete output;

	}
	myInput.close();
	return 0;
}

