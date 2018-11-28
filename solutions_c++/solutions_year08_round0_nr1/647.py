// zero.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
using namespace std;


int main(int argc, char* argv[])
{
   ofstream res;
   res.open ("e:\\output");
   

   string line;
   ifstream myfile ("e:\\input");
   if (myfile.is_open())
   {
	   getline (myfile,line);
	   int cases = atoi(line.c_str());
	   cout<< "cases " << cases << endl;
	   int i,j;

	   for (i=0;i<cases;i++)
	   {		   
		   int total = 0;
		   getline (myfile,line);
		   int nengines = atoi(line.c_str());
		   cout<< "case " << i << endl;
		   cout<< "engines " << nengines << endl;
		   set<string> engines;
		   set<string> engines_tmp;
		   for (j=0; j< nengines; j++)
		   {
			   getline (myfile,line);
			   engines.insert(line);
		   }

#define reset() engines_tmp.clear(); engines_tmp=engines;

		   reset();

		   getline (myfile,line);
		   int nqueries = atoi(line.c_str());		   
		   cout<< "queries " << nqueries << endl;
		   vector<string> queries;
		   for (j=0; j< nqueries; j++)
		   {
			   getline (myfile,line);
			   engines_tmp.erase(line);
			   if (engines_tmp.empty()) 
			   {
				   ++total;
				   reset();
				   engines_tmp.erase(line);
			   }
		   }
		   res << "Case #"<<(i+1) <<": " <<total<<endl;

	   }
    
	   myfile.close();
   }
   else cout << "Unable to open file"; 

  res.close();
  return 0;
}




