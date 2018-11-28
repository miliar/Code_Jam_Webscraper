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
     int N;
	 fin >> N;

	 long long pos = 0;
	 long long su  = 0;
	 long long mi  = 100000000;
     long long cur = 0; 

     for (int i=0; i<N; i++)
	 {
         fin >> cur;
		 pos = pos ^ cur;
		 su = su + cur;
		 mi = min(mi, cur);
	 }

	 su = su - mi;

	 if (pos != 0)
         fout << "Case #" << tt+1 << ": " << "NO" << endl;
	 else
         fout << "Case #" << tt+1 << ": " << su << endl;
  }

   return 0;
}
