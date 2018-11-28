// zero.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;


int main(int argc, char* argv[])
{
   ofstream res;
   res.open ("e:\\output");
   

   string line;
   ifstream myfile ("e:\\B-small-attempt1.in");
   if (myfile.is_open())
   {
	   getline (myfile,line);
	   int cases = atoi(line.c_str());
	   cout<< "cases " << cases << endl;
	   int i,j;

	   for (i=0;i<cases;i++)
	   {		   
		   int totalA = 0, totalB = 0;
		   getline (myfile,line);
		   int turnaround = atoi(line.c_str());
		   cout<< "case " << (i + 1) << endl;
		   cout<< "turnaround " << turnaround << endl;

		   int countA = 0, countB = 0;
		   int A, B;
		   myfile >> A;
		   myfile >> B;
		   getline (myfile,line);
		   cout<< "A " << A << "; B " << B << endl;
		   map<int, int> timetableA,timetableB;
		   for (j=0;j<A;j++)
		   {
			   int h,m;
			   char c;
			   int t1,t2;
			   myfile >> h >> c >> m ;
			   t1 = h*60 + m;
			   timetableA[t1]--;
			   cout << h <<":" << m << " A->B " ;
			   myfile >> h >> c >> m ;
			   cout << h <<":" << m << endl;
			   t2 = h*60 + m + turnaround;
			   if (t1>t2) exit(9);
			   timetableB[t2]++;
		   }
		   for (j=0;j<B;j++)
		   {
			   int h,m;
			   char c;
			   int t1,t2;
			   myfile >> h >> c >> m ;
			   t1 = h*60 + m;
			   timetableB[t1]--;
			   cout << h <<":" << m << " B->A " ;
			   myfile >> h >> c >> m ;
			   t2 = h*60 + m + turnaround;
			   timetableA[t2]++;
			   cout << h <<":" << m << endl;
			   getline (myfile,line);			   
		   }

		   // processing!!!
		   map<int, int>::iterator it;

		   it = timetableA.begin();
		   while (it != timetableA.end())
		   {			   
			   countA += it->second;
			   if (countA<0) {totalA -= countA; countA = 0;}
			   cout << "A : " << totalA << "| "<<it->first / 60 << ":" << it->first % 60 << " - " << it->second << " : current count = " << countA << endl;
			   ++it;
		   }
			
		   it = timetableB.begin();
		   while (it != timetableB.end())
		   {			   
			   countB += it->second;
			   if (countB<0) {totalB -= countB; countB = 0;}
			   cout << "B : " << totalB << "| "<< it->first / 60 << ":" << it->first % 60 << " - " << it->second << " : current count = " << countB << endl;
			   ++it;
		   }


		   cout << "Case #"<<(i+1) <<": " <<totalA << " " << totalB <<endl;
		   res << "Case #"<<(i+1) <<": " <<totalA << " " << totalB <<endl;

	   }
    
	   myfile.close();
   }
   else cout << "Unable to open file"; 

  res.close();
  return 0;
}




