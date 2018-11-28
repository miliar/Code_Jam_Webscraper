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

long long r[3][3];

void comp(long long x, long long y)
{
  int i = x%3;
  int j = y%3;
  r[i][j]++;
}

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

  memset(r, 0, sizeof(r));

  long long n, A, B, C, D, x0, y0, M;

  fin >>  n >> A >> B >> C >> D >> x0 >> y0 >> M;

//X = x0, Y = y0
//print X, Y
//for i = 1 to n-1
//  X = (A * X + B) mod M
//  Y = (C * Y + D) mod M
//  print X, Y

  comp(x0,y0);
  long long x = x0;
  long long y = y0;
  long long x2 = x;
  long long y2 = y;
  for (int i=0; i<n-1; i++)
  {
     x2 = (A*x + B)%M;
	 x = x2;
	 y2 = (C*y + D)%M;
	 y = y2;
	 comp(x,y);
  }

  long long res = 0;

  long long te = 0;

  for (int i=0; i<3; i++)
  {
    for (int j=0; j<3; j++)
	{
      for (int k=0; k<3; k++)
	  {
        if ( (i+j+k)%3 == 0)
		{
         for (int l=0; l<3; l++)
		 {
            for (int p=0; p<3; p++)
			{
               for (int q=0; q<3; q++)
			   {
                  if ( (l+p+q)%3 == 0 )
				  {
                   te = 0; 
                   if ( i == j && j == k && l == p && p == q )
				   {
                     if (r[i][l] > 2)
					   te = (r[i][l])*(r[i][l]-1)*(r[i][l]-2);
				   }
				   else
				   {
                    te = r[i][l]*r[j][p]*r[k][q];
				   }
					//if ( i == j && j == k && l == p && p == q )
					//	te = te/6;
					res = res + te;
				  }
			   }
			}
		 }
		}
	  }
	}
  }

  res = res/6;

  fout << "Case #" << tt+1 << ": " << res << endl;
}

   return 0;
}
