// codejam1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <stdio.h>



typedef struct engine
{
	int n;
	std::string name;
	int findit;
};


int _tmain(int argc, _TCHAR* argv[])
{
	FILE * fout;
	fout = fopen("d:\\largeout.txt","w+b");
	std::string str_in = "d:\\A-large.in";
	std::ifstream is(str_in.c_str());
	std::string line;

	int N,S,Q;
	is >> N;//number of cases
	engine *engines = new engine[100];
	int queries[1000];

	for (int i=0; i<N; i++)
	{
		is >> S; // number of search engines
		
		std::getline(is,line);
		for (int j=0; j<S; j++)
		{			
			std::getline(is,engines[j].name); //read engines name
			engines[j].n=j;
			engines[j].findit = 1;
		}
		is >> Q; // number of queries
		
		std::getline(is,line);			
		for (int j=0; j<Q; j++)
		{
		
			std::getline(is,line);	 // read queries		

			for (int k=0; k<S; k++)
			{
				if (engines[k].name.compare(line)==0)
				{
					queries[j] = engines[k].n;
					break;
				}
			}
		}

		//solve;
	
		
		int change = 0;
		int eg=0;
		int j=0;
		while (j<Q)
		{
			// searching for the first engine
			engines[queries[j]].findit = 0;
			eg=0;
			for (int k=0; k<S; k++) eg+=engines[k].findit;
			
			// changing
			if (eg==0)
			{
				for (int k=0; k<S; k++) engines[k].findit=1;
				engines[queries[j]].findit = 0;
				change++;
			}
						
			j++;
		}

		fprintf(fout,"Case #%d: %d\r\n",i+1,change);

	}
	
	fclose(fout);

	
	return 0;
}

