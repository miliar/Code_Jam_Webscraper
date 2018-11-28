#include <fstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <stdio.h>

#include <math.h>

using namespace std;

ofstream fout("OUT444.txt");
ifstream fin ("INP444.in");


//FILE* pFile;
//int c;
//pFile = fopen("ou.txt","w");
//pFile=fopen ("beads.txt","r");

double X[50];
double Y[50];
double R[50];

bool isin(int i, int j)
{
   double xy = sqrt(  (X[i] - X[j])*(X[i] - X[j]) + (Y[i] - Y[j])*(Y[i] - Y[j]));
   if ( xy + R[j] <= R[i] + 0.000000001 )
     return true;
   if ( xy + R[i] <= R[j] + 0.000000001 )
     return true;
   return false;
}

double comp(int i, int j)
{
   double xy = sqrt(  (X[i] - X[j])*(X[i] - X[j]) + (Y[i] - Y[j])*(Y[i] - Y[j]));
   double res = (R[i] + R[j] + xy)/2;
   return res;
}

int main() {

//FILE* pFile;
//pFile = fopen("ou.txt","w");

// string na;
// if (tt == 0)
//  getline(fin,na);

// getline(fin,na);

// istringstream sin(na); 
// string v; 
// while (sin>>v) 
//   names.push_back(v); 

//fprintf(pFile, "Case #%d: ", t+1);
//fprintf(pFile,"%d\n",res);

  int TT;

  fin >> TT;

  for (int tt=0; tt<TT; tt++)
  { 

     int N;
	 fin >> N;
	 for (int i=0; i<N; i++)
	 {
       fin >> X[i] >> Y[i] >> R[i];
	 }

	 double ma = 0;

	 for (int i=0; i<N; i++)
		 ma = max(ma, R[i]);

     double result = 0;  
 
     if ( N<=2)
	 {
        fout << "Case #" << tt+1 << ": " << ma << endl;
	 }
	 else
	 {
        bool done = false;
        for (int i=0; i<3; i++)
		{
          for (int j=i+1; j<3; j++)
		  {
             if (isin(i,j))
			 {
               fout << "Case #" << tt+1 << ": " << ma << endl;
			   done = true;
			 }
		  }
		}
		if ( !done )
		{
               result = 1000000;
			   double r01 = comp(0,1);
			   double r02 = comp(0,2);
			   double r12 = comp(1,2);
			   double m01 = max(r01,R[2]);
			   double m02 = max(r02,R[1]);
			   double m12 = max(r12,R[0]);
			   result = min(result, m01);
			   result = min(result, m02);
			   result = min(result, m12);

               fout << "Case #" << tt+1 << ": " << result << endl;
		}
	 }
  }

   return 0;
}
