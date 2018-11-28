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

ofstream fout("out111.txt");
ifstream fin ("inp111.in");


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

  int TT;

  fin >> TT;

  int vis[2000];
  unsigned long long totval[2000];
  unsigned long long val[2000];

  for (int tt=0; tt<TT; tt++)
  { 
     memset(totval, 0, sizeof(totval));

     for (int i=0; i<1010; i++)
		 vis[i] = -1;

     unsigned long long R, k, N;

	 fin >> R >> k >> N;

	 unsigned long long su = 0;

	 for (int i=0; i<N; i++)
	 {
        fin >> val[i];
		su += val[i];
	 }

     if ( su <= k )
	 {
        unsigned long long res = R*su;
        fout << "Case #" << tt+1 << ": " << res << endl;
		continue;
	 }

     int curind = 0;
	 int ti     = 0;

	 unsigned long long gloval = 0;

     bool found = false;

     unsigned long long persize = 0;
     unsigned long long perval  = 0;

	 while ( ti < R && !found )
	 {
        unsigned long long lsu = 0;

	    while (lsu <= k)
		{
           lsu    += val[curind];
		   gloval += val[curind];
		   curind = (curind+1)%N;
		}

		curind = (curind + N - 1)%N;
		gloval -= val[curind];
		lsu    -= val[curind];

		ti++;
        if (vis[curind] == -1)
		{
           vis[curind] = ti;  
           totval[ti]  = gloval;
		}
		else
		{
           found   = true;
		   persize = ti - vis[curind];
		   perval  = gloval - totval[vis[curind]];
		}
	 }

	 if (!found)
	 {
        fout << "Case #" << tt+1 << ": " << gloval << endl;
		continue;
	 }
	 else
	 {
        R = R - ti;
        unsigned long long rem = R%persize;
		unsigned long long div = (R - rem)/persize;
		gloval += div*perval;

		ti = 0;
		while (ti < rem)
		{
           unsigned long long lsu = 0;

	       while (lsu <= k)
		   {
             lsu    += val[curind];
		     gloval += val[curind];
		     curind = (curind+1)%N;
		   }

		   curind = (curind + N - 1)%N;
		   gloval -= val[curind];
		   lsu    -= val[curind];

		   ti++;          
		}

        fout << "Case #" << tt+1 << ": " << gloval << endl;
	 }
  }

   return 0;
}
