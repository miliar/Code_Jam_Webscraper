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

string goog = "welcome to code jam";
string s;

int comb[510][20];

#define MO 10000

int comp(int tex, int pat)
{
   if (tex < pat )
     return 0;
   if ( pat <= 0 )
	   return 1;
   if (comb[tex][pat] != -1 )
	   return comb[tex][pat];
   int su = 0;
   su = comp(tex-1, pat);
   if ( s[tex-1] == goog[pat-1] )
	   su = (su + comp(tex-1, pat-1) ) % MO;
   comb[tex][pat] = su;
   return su;
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


//sscanf(stringHM,"%d:%d",&h,&m);


 //fprintf(pFile, "Case #%d: ", t+1);
 //fprintf(pFile,"%d\n",res); 

  int T;
  fin >> T;

  getline(fin,s);

  for (int tt=0; tt<T; tt++)
  {

     s.clear();
	 getline(fin,s);

     memset(comb, -1, sizeof(comb));

     int res = comp(s.size(), 19);
	 string ou = "0000";
     int ind = 3;
	 while ( res > 0)
	 {
        char c = (char) ('0' + (res%10));
        ou[ind] = c;
		res = (res - (res%10) )/10;
		ind--;
	 }
     fout << "Case #" << tt+1 << ": " << ou << endl;
  }

   return 0;
}
