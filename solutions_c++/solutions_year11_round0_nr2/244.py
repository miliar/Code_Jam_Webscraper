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
     int C;
	 fin >> C;
	 map < vector<char>, char> comb;
     vector <char> te(2);
	 for (int i=0; i<C; i++)
	 {
        string s;
		fin >> s;
        te[0]=s[0];
		te[1]=s[1];
		comb[te]=s[2];
        te[0]=s[1];
		te[1]=s[0];
		comb[te]=s[2];
	 }

	 int D;
	 fin >> D;
	 map < vector<char>, int> oppo;
	 for (int i=0; i<D; i++)
	 {
        string s;
		fin >> s;
		te[0]=s[0];
		te[1]=s[1];
		oppo[te]=1;
        te[0]=s[1];
		te[1]=s[0];
		oppo[te]=1;
	 }

	 int N;
	 fin >> N;
	 vector <char> res;
	 res.clear();
     string str;
     fin >> str;
     for (int j=0; j<N; j++)
	 {
        int n = res.size();
		if (n == 0)
			res.push_back(str[j]);
		else
		{
           te[0]=res[n-1];
		   te[1]=str[j];
		   if (comb.find(te) != comb.end())
		   {
              res.erase(res.end()-1);
			  res.push_back(comb[te]);
		   }
		   else
		   {
              bool er = false;   
              for (int i=0; i<n && !er; i++)
			  {
                 te[0]=res[i];
				 te[1]=str[j];
				 if (oppo.find(te) != oppo.end())
					 er = true;
			  }
			  if (er)
				  res.clear();
			  else
				  res.push_back(str[j]);
		   }
		}
	 }

	 string ou = "[";
	 if (res.size() == 0)
		 ou = "[]";
	 else
	 {
	     for (int i=0; i<res.size()-1; i++)
		     ou = ou + res[i] + ", ";
	     if (res.size() > 0)
		     ou = ou + res[res.size()-1];
	     ou = ou + "]";
	 }

     fout << "Case #" << tt+1 << ": " << ou << endl;

  }

   return 0;
}
