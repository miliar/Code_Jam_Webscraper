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

  string yes = "ON";
  string  no = "OFF";

  for (int tt=0; tt<TT; tt++)
  { 
     unsigned long long n;
	 unsigned long long k;

	 fin >> n;
	 fin >> k;
     
     unsigned long long a = 0;
	 
	 a = 1 << n;

	 k = (k%a);

	 k++;

	 string res;

	 if ( k == a )
       res = yes;
	 else
       res = no;

     fout << "Case #" << tt+1 << ": " << res << endl;
  }

   return 0;
}
