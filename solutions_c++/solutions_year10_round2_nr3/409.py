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

long long comp[510][510];
long long cb[510][510];

long long mo = 100003;

long long comb(long long a, long long b)
{
   if (comp[a][b] != -1)
	   return comp[a][b];

   if (a == 2)
   {
     comp[a][b] = 1;
	 return 1;
   }

   if ( b == 1 )
   {
     comp[a][b] = 1;
	 return 1;
   }

   long long su = 0;
   for (long long j=1; j<b; j++)
   {
      long long re1 = (comb(b, j))%mo;
      long long re2 = (cb[a-b-1][b-j-1])%mo;
	  long long re3 = (re1*re2)%mo;
	  su = (su + re3)%mo;
   }
   

   comp[a][b] = su;
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

//fprintf(pFile, "Case #%d: ", t+1);
//fprintf(pFile,"%d\n",res);

  int TT;

  fin >> TT;

  memset(comp, -1, sizeof(comp));
  memset(cb, 0, sizeof(cb));

  cb[0][0] = 1; 
  cb[1][1] = 1; 
  cb[1][0] = 1; 

  for (int i=2; i<= 502; i++) 
  { 
     cb[i][0] = 1; 
     cb[i][i] = 1; 
     for (int j=1; j< i; j++) 
       cb[i][j] = (cb[i-1][j-1] + cb[i-1][j]) % mo; 
  } 

  for (int tt=0; tt<TT; tt++)
  { 
     int n;

	 fin >> n;
     if (n == 2)
	 {
        fout << "Case #" << tt+1 << ": " << 1 << endl;
		continue;
	 }

     long long su = 0;
	 for (long long i=1; i<n; i++)
	 {
        su = (su + comb(n, i) )%mo;
	 }

     fout << "Case #" << tt+1 << ": " << su << endl; 
  }

   return 0;
}
