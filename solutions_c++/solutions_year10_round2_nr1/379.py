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

vector<string> SPLIT(string s, string del = "/", bool f = false)
{ 
   s += del[0];
   string w = ""; 
   vector<string> res; 
   for(string::iterator it = s.begin(); it != s.end(); ++it)
   { 
        if  (find(del.begin(), del.end(), *it) == del.end())
           w += *it; 
       else if (f || w != "")
       { 
            res.push_back(w); 
            w = ""; 
       } 
  } 
  return res;
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

  for (int tt=0; tt<TT; tt++)
  { 
      int n, m;
      fin >> n >> m;
      string na;
      getline(fin,na);

      vector <string> ex;
	  vector <string> ne;
	  ex.clear();
	  ne.clear();

	  for (int i=0; i<n; i++)
	  {
         getline(fin,na);
		 ex.push_back(na);
	  }

	  for (int i=0; i<m; i++)
	  {
         getline(fin,na);
		 ne.push_back(na);
	  }

	  map <string, int> allex;
	  allex.clear();

	  for (int i=0; i<n; i++)
	  {
        vector <string> cur = SPLIT(ex[i]);
		string s = "";
		int szcur = cur.size();
		for (int j=0; j<szcur; j++)
		{
          s = s+ "/" + cur[j];
		  allex[s]=1;
		}
	  }

	  vector <string> allne;
	  allne.clear();

      for (int i=0; i<m; i++)
	  {
        vector <string> cur = SPLIT(ne[i]);
		string s = "";
		int szcur = cur.size();
		for (int j=0; j<szcur; j++)
		{
          s = s + "/" + cur[j];
		  if (allex.find(s) == allex.end())
		  {
             allne.push_back(s);   
		  }
		}
	  }

      sort(allne.begin(), allne.end());
	  int tot = 0;

	  int szall = allne.size();
	  if (szall == 0)
	  {
         fout << "Case #" << tt+1 << ": " << tot << endl; 
	  }
	  else
	  {
		  tot=1;
		  for (int j=1; j<szall; j++)
		  {
             if (allne[j] != allne[j-1])
			 {
				 tot++;
			 }
		  }

          fout << "Case #" << tt+1 << ": " << tot << endl; 
	  }
  }

   return 0;
}
