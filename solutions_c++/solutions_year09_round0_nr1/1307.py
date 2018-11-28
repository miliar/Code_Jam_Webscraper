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


ofstream fout("oooo.txt");
ifstream fin ("iiii.in");

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


//sscanf(stringHM,"%d:%d",&h,&m);


 //fprintf(pFile, "Case #%d: ", t+1);
 //fprintf(pFile,"%d\n",res);

  int L, D, N;

  fin >> L >> D >> N;

  string words[5010];

  for (int i=0; i<D; i++)
    fin >> words[i];

  int pres[17][28];

  for (int i=0; i<N; i++)
  {
     memset(pres, 0, sizeof(pres));

     string s;
	 fin >> s;

	 int ind = 0;
	 for (int j=0; j<L; j++)
	 {
        char c = s[ind];
        if ( c != '(' )
		{
           int val = (int) ( c - 'a' );
		   pres[j][val]=1;
		   ind++;
		}
		else
		{
           ind++;
		   c = s[ind];
		   while ( c != ')' )
		   {
               int val = (int) ( c - 'a' );
		       pres[j][val]=1;
		       ind++;
			   c=s[ind];
		   }
		   ind++;
		}
	 }

	 int res = 0;

	 for ( int j=0; j<D; j++)
	 {
         bool ok = true;
		 for (int k=0; k<L && ok; k++)
		 {
            char c = words[j][k];
			int val = (int) ( c - 'a' );
			if (pres[k][val] != 1)
				ok=false;
		 }

		 if (ok)
           res++;
	 }

     fout << "Case #" << i+1 << ": " << res << endl;
  }

   return 0;
}
