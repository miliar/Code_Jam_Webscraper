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

long long m[1100]; 
long long pr[11][550];
long long dp[11][1100][11]; 
int p;
int n;

long long LA;
//1000000000

long long comp(long long lev, long long pos, long long off)
{
   if (dp[lev][pos][off] != -1)
	   return dp[lev][pos][off];

   if (lev == 0)
   {
      bool ok = true;
	  if (p - m[pos] > off)
		  ok = false;
	  //if (p - m[2*pos-1] > off)
	  //	  ok = false;

	  if (!ok)
	  {
        dp[lev][pos][off]=LA;
		return LA;
	  }
	  else
	  {
        dp[lev][pos][off]=0;
		return 0;
	  }
   }

   long long with1 = comp(lev-1, 2*pos-1, off+1);
   long long with2 = comp(lev-1, 2*pos, off+1);
   
   long long with=LA; 
   if ( (with1 == LA) || (with2 == LA) )
      with == LA;
   else
      with = with1 + with2 + pr[lev][pos];

   long long without1 = comp(lev-1, 2*pos-1, off);
   long long without2 = comp(lev-1, 2*pos, off);

   long long without=LA; 
   if ( (without1 == LA) || (without2 == LA) )
      without == LA;
   else
      without = without1 + without2;

   if ( (without == LA) && (with == LA) )
   {
      dp[lev][pos][off]=LA;
   }
   else if (without == LA)
   {
      dp[lev][pos][off]=with;
   }
   else if (with == LA)
   {
      dp[lev][pos][off]=without;
   }
   else
   {
     dp[lev][pos][off]=min(with, without);
   }

   return dp[lev][pos][off] ;
   
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

  LA = -2;
  int TT;
  fin >> TT;

  for (int tt=0; tt<TT; tt++)
  { 

	  fin >> p;
      memset(m,  0, sizeof(m));
      memset(pr, 0, sizeof(pr));
	  memset(dp, -1, sizeof(dp));

	  n = (1<<p);

	  for (int i=1; i<=n; i++)
		  fin >> m[i];

	  int nl = n;
	  for (int i=1; i<=p; i++)
	  {
         nl = nl/2;
         for (int j=1; j<=nl; j++)
			 fin >> pr[i][j];
	  }

	    long long bes = comp(p, 1, 0);
        fout << "Case #" << tt+1 << ": " << bes << endl;
  }

   return 0;
}
