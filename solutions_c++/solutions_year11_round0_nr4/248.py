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

double tc[1010];
double tr[1010];

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

  fout.precision(30);

  memset(tc, 0, sizeof(tc));
  memset(tr, 0, sizeof(tr));

  tc[2]=2;
  tr[2]=1; 

  int n;
  double su=0;
  for (n=2; n<=1005; n++)
  {
     su    = su + tc[n-1] + tr[n-1];
	 double ra = n;
	 ra = ra/(ra-1);
	 double rr = n;
	 tc[n] = ra+su/(rr-1);
	 tr[n] = tc[n]-1;
  }

  for (int tt=0; tt<TT; tt++)
  { 
     int N;
	 fin >> N;

	 int tak[1010];
	 int arr[1010];
	 memset(tak, 0, sizeof(tak));

	 for (int i=0; i<N; i++)
	    fin >> arr[i];

	 double res=0;
	 for (int i=0; i<N; i++)
	 {
        if (tak[i] == 0)
		{
          int count = 1;
		  int ind   = i;
		  while (arr[ind] != i+1)
		  {
             ind = arr[ind]-1;
			 tak[ind]=1;
			 count++;
		  }
		  tak[i]=1;
		  res = res + tc[count];
		}
	 }

     fout << "Case #" << tt+1 << ": " << res << endl;
  }

   return 0;
}
