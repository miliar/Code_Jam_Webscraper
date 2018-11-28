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

vector <int> x;
vector <int> y;

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

  int nn;

  fin >> nn;

  x.clear();
  y.clear();

  for (int i=0; i<nn; i++)
  {
    int te;
	fin >> te;
	x.push_back(te);
  }

  for (int i=0; i<nn; i++)
  {
    int te;
	fin >> te;
	y.push_back(te);
  }

  sort(x.begin(), x.end());
  sort(y.begin(), y.end());
  reverse(y.begin(), y.end());

  long long res = 0;

  for (int i=0; i<nn; i++)
    res += x[i]*y[i];

  fout << "Case #" << tt+1 << ": " << res << endl;
}

   return 0;
}
