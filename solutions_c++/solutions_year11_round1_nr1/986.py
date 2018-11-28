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

  int TT;

  fin >> TT;

  for (int tt=0; tt<TT; tt++)
  { 
     long long N;
	 int PD, PG;
     fin >> N >> PD >> PG;

	 bool br = false;
	 bool pos = false;
	 if (PG == 100)
	 {
        if (PD != 100)
		{
          fout << "Case #" << tt+1 << ": " << "Broken" << endl;
		  continue;
		}
		else 
		{
          fout << "Case #" << tt+1 << ": " << "Possible" << endl;
		  continue;
		}
	 }

	 if (PG == 0)
	 {
        if (PD != 0)
		{
          fout << "Case #" << tt+1 << ": " << "Broken" << endl;
		  continue;
		}
		else 
		{
          fout << "Case #" << tt+1 << ": " << "Possible" << endl;
		  continue;
		}
	 }


	 if (N >= 100)
	 {
	    fout << "Case #" << tt+1 << ": " << "Possible" << endl;
        continue;
	 }

	 int NN=N;

     pos = false;
	 for (int D=1; D<=NN && !pos; D++)
	 {
       if ( (PD*D)%100 == 0)
	   {
		  pos=true;
	   }
	 }

	 if (pos)
	    fout << "Case #" << tt+1 << ": " << "Possible" << endl;
	 else
        fout << "Case #" << tt+1 << ": " << "Broken" << endl;
  }

   return 0;
}
