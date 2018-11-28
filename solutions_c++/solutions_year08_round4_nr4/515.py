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


    ofstream fout("ou.txt");
    ifstream fin ("beads.txt");

    //FILE* pFile;
    //int c;
    //pFile = fopen("ou.txt","w");
    //pFile=fopen ("beads.txt","r");


double tol = 0.0;

int main() {

//FILE* pFile;
//pFile = fopen("ou.txt","w");

int N;

fin >> N;

for (int tt=0; tt<N; tt++)
{
 
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

  int k;
  string s;
  fin >> k;
  fin >> s;

  string a = s;

  long long bes = 100000;

  //int ma = 1 << k;
  int m = s.size()/k;

  vector <int> pe;
  for (int i=0; i<k; i++)
   pe.push_back(i);

    for (int j=0; j<m; j++)
	{
      for (int t=0; t<k; t++)
	  {
         char c = s[j*k+pe[t]];
         a[j*k+t]=c;
	  }
	}

	long long llbes = 1;
    for (int i=1; i<a.size(); i++)
	{
      if (a[i] != a[i-1])
		  llbes = llbes + 1;
	}

	if (bes > llbes)
	 bes = llbes;

  do
  {
    for (int j=0; j<m; j++)
	{
      for (int t=0; t<k; t++)
	  {
         char c = s[j*k+pe[t]];
         a[j*k+t]=c;
	  }
	}

	long long lbes = 1;
    for (int i=1; i<a.size(); i++)
	{
      if (a[i] != a[i-1])
		  lbes = lbes + 1;
	}

	if (bes > lbes)
	 bes = lbes;

  }while (next_permutation(pe.begin(),pe.end()));

  //int res = 0;


  fout << "Case #" << tt+1 << ": " << bes << endl;
}

   return 0;
}
