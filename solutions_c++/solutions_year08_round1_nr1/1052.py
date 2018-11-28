// zero.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
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
		   int size  = atoi(line.c_str());
		   cout<< "case " << (i + 1) << endl;
		   cout<< "size " << size << endl;
		   
		   multiset<int, greater<int> > v1;
		   multiset<int, less<int> > v2;
		   for (j=0; j< size; j++)
		   {
			   int k;
			   myfile>>k;
			   v1.insert(k);			   

		   }
		   getline (myfile,line);
		   for (j=0; j< size; j++)
		   {
			   int k;
			   myfile>>k;
			   v2.insert(k);
		   }
		   getline (myfile,line);

		   
		   multiset<int, greater<int> >::iterator it1 =  v1.begin();
		   multiset<int, less<int> >::iterator it2= v2.begin();
		   while (it1 != v1.end())
		   {
			   total += (*it1++) * (*it2++);
		   }


		   res << "Case #"<<(i+1) <<": " <<total<<endl;

	   }
    
	   myfile.close();
   }
   else cout << "Unable to open file"; 

  res.close();
  return 0;
}




