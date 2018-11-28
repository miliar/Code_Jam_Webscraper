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

  fout.precision(30);

  int TT;
  fin >> TT;

  double b[1010];
  double e[1010];
  double w[1010];
  double d[1010];
  vector < vector<double> > cp;

  for (int tt=0; tt<TT; tt++)
  {
      double x, s, r, t;
	  int n;

	  double diswalk;

	  fin >> x >> s >> r >> t >> n;
      cp.clear();

	  if (r < s)
		  r = s;

	  diswalk = x;

	  for (int i=0; i<n; i++)
	  {
         fin >> b[i] >> e[i] >> w[i];
		 vector <double> te;
		 te.push_back(w[i]);
		 te.push_back(e[i]-b[i]);
		 cp.push_back(te);
		 diswalk = diswalk - te[1];
	  }

	  vector <double> te;
	  te.push_back(0);
	  te.push_back(diswalk);
	  cp.push_back(te);

	  n++;

	  sort(cp.begin(), cp.end());
	  //reverse(cp.begin(), cp.end());

	  double time = 0;

	  for (int i=0; i<n; i++)
	  {
        vector <double> te = cp[i]; 
		{
           double ttem = te[1]/(r+te[0]);
		   if (ttem <= t)
		   {
		     time += ttem;
			 t = t-ttem;
		   }
		   else
		   {
              double dr = (te[0]+r)*t;
			  double dw = te[1]-dr;
			  double tw = dw/(te[0]+s);
			  time += t;
			  time += tw;
			  t = 0;
		   }
		}
	  }

//      int res = 0; 
      fout << "Case #" << tt+1 << ": " << time << endl;
  }

   return 0;
}
