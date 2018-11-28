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

ofstream fout("OUT111.txt");
ifstream fin ("INP111.in");


//FILE* pFile;
//int c;
//pFile = fopen("ou.txt","w");
//pFile=fopen ("beads.txt","r");


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

  fout.precision(30);

  double pos[300];
  int    num[300];
  double big = 1500000000000;

  int TT;
  fin >> TT;
  for (int tt=0; tt<TT; tt++)
  {
     int C;
	 double D;
	 memset(pos, 0, sizeof(pos));
     memset(num, 0, sizeof(num));

	 fin >> C >> D;
	 for (int i=0; i<C; i++)
	 {
        fin >> pos[i];
		fin >> num[i];
	 }

	 double tol = 0.0000001;

	 double ma = big;
	 double mi = 0;

	 while ( (ma - mi) > tol && (ma-mi)/(mi+1) > tol)
	 {
        double mid = (ma +mi)/2;
		int ind = 0;
		bool poss = true;
		double left = -big;
		while (ind < C && poss)
		{
           double upl = pos[ind] - mid;
		   double lol = pos[ind] + mid;
           left = max(left, upl);
		   left = left + D*(num[ind]-1);
           if (left > lol)
			   poss = false;
		   left = left+D;
		   
           ind++;  
		}

        if (poss)
			 ma = mid;
		else
			 mi = mid;
	 }

     double res = (ma+mi)/2;
	 if (res < tol)
		 res = 0;

     fout << "Case #" << tt+1 << ": " << res << endl;
  }

   return 0;
}
