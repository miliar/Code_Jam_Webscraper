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

  int bef[60][60];
  int aft[60][60];
  int dro[60][60];

  for (int tt=0; tt<TT; tt++)
  { 
	  int n, k;

	  fin >> n >> k;

      memset(bef, 0, sizeof(bef));
	  memset(aft, 0, sizeof(aft));
	  memset(dro, 0, sizeof(dro));

      string na;
      getline(fin,na);

	  for (int i=0; i<n; i++)
	  {
         getline(fin,na);
	     for (int j=0; j<n; j++)
		 {
            if (na[j] == 'R')
				bef[i][j] = 1;
			else if (na[j] == 'B')
				bef[i][j] = 2;
		 }
	  }

      int lev;
	  for (int i=0; i<n; i++)
	  {
        for (int j=0; j<n; j++)
		{
           aft[i][j] = bef[i][j];
		}
	  }

	  for (lev =0; lev <n/2; ++lev)
	  {
         int st  = lev;
		 int end = n - 1 - lev;
		 for (int i=st; i<end; ++i)
		 {
            int dif = i - st;
			aft[st][i]          = bef[end-dif][st];
            aft[end-dif][st]    = bef[end][end - dif];
			aft[end][end - dif] = bef[i][end];
            aft[i][end]         = bef[st][i]; 
		 }
	  }

      for (int i=0; i<n; i++)
	  {
        int pos1 = n-1;
        int pos2 = n-1;
		while (pos2 >= 0)
		{
          if (aft[pos2][i] != 0)
		  {
             dro[pos1][i] = aft[pos2][i];
			 pos1--;
		  }
		  pos2--;
		}
	  }

      bool red = false;
	  bool blu = false;

	  for (int i=0; i<n; i++)
	  {
         for (int j=0; j<=n-k; j++)
		 {
           bool locred = true;
		   bool locblu = true;
		   for (int p=0; p<k; p++)
		   {
              if (dro[i][j+p] != 1)
			   locred = false;
			  if (dro[i][j+p] != 2)
			   locblu = false;
		   }
		   if (locred)
			   red = true;
		   if (locblu)
			   blu = true;
		 }

         for (int j=k-1; j<n; j++)
		 {
           bool locred = true;
		   bool locblu = true;
		   for (int p=0; p<k; p++)
		   {
              if (dro[i][j-p] != 1)
			   locred = false;
			  if (dro[i][j-p] != 2)
			   locblu = false;
		   }
		   if (locred)
			   red = true;
		   if (locblu)
			   blu = true;
		 }
	  }

      for (int i=k-1; i<n; i++)
	  {
         for (int j=k-1; j<n; j++)
		 {
           bool locred = true;
		   bool locblu = true;
		   for (int p=0; p<k; p++)
		   {
              if (dro[i-p][j-p] != 1)
			   locred = false;
			  if (dro[i-p][j-p] != 2)
			   locblu = false;
		   }
		   if (locred)
			   red = true;
		   if (locblu)
			   blu = true;
		 }
	  }

      for (int i=k-1; i<n; i++)
	  {
         for (int j=0; j<=n-k; j++)
		 {
           bool locred = true;
		   bool locblu = true;
		   for (int p=0; p<k; p++)
		   {
              if (dro[i-p][j+p] != 1)
			   locred = false;
			  if (dro[i-p][j+p] != 2)
			   locblu = false;
		   }
		   if (locred)
			   red = true;
		   if (locblu)
			   blu = true;
		 }
	  }

	  for (int i=k-1; i<n; i++)
	  {
         for (int j=0; j<n; j++)
		 {
           bool locred = true;
		   bool locblu = true;
		   for (int p=0; p<k; p++)
		   {
              if (dro[i-p][j] != 1)
			   locred = false;
			  if (dro[i-p][j] != 2)
			   locblu = false;
		   }
		   if (locred)
			   red = true;
		   if (locblu)
			   blu = true;
		 }
	  }

	  string s;

	  if (red && blu)
		  s = "Both";
	  else if (red)
		  s = "Red";
	  else if (blu)
	      s = "Blue";
	  else
	      s = "Neither"; 

      fout << "Case #" << tt+1 << ": " << s << endl; 
  }

   return 0;
}
