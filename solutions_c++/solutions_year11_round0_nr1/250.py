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
	 vector <int> col;
	 vector <int> pos;
     for (int i=0; i<N; i++)
	 {
        string s;
		fin >> s;
		if (s == "O")
		  col.push_back(0);
		else
		  col.push_back(1);
		int p;
		fin >> p;
		pos.push_back(p);
	 }

	 int t = 0;
	 vector <int> ti;
	 ti.push_back(pos[0]);

     for (int i=1; i<N; i++)
	 {
        int orind = -1;
		for (int j=i-1; j>=0 && orind==-1; j--)
		{
           if (col[j] == 0)
		   {
               orind = j;
		   }
		}
        int blueind = -1;
		for (int j=i-1; j>=0 && blueind==-1; j--)
		{
           if (col[j] == 1)
		   {
               blueind = j;
		   }
		}		
		if (col[i]==0)
		{
		   int tim;
           if (orind == -1)
              tim = max(ti[i-1]+1, pos[i]);
		   else
              tim = max(ti[i-1]+1, ti[orind]+abs(pos[orind]-pos[i])+1);
		   ti.push_back(tim);
		}
		else
		{
		   int tim;
           if (blueind == -1)
              tim = max(ti[i-1]+1, pos[i]);
		   else
              tim = max(ti[i-1]+1, ti[blueind]+abs(pos[blueind]-pos[i])+1);
		   ti.push_back(tim);
		}
	 }


     fout << "Case #" << tt+1 << ": " << ti[N-1] << endl;
  }

   return 0;
}
