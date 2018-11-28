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

int ini[110][110];
int upd[110][110];

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
	  int r;
	  int x1, y1, x2, y2;

	  memset(ini, 0, sizeof(ini));
	  memset(upd, 0, sizeof(upd));

	  fin >> r;

	  for (int i=0; i<r; i++)
	  {
        fin >> x1 >> y1 >> x2 >> y2;
  
        for (int j=y1; j<=y2; j++)
		{
           for (int k=x1; k<=x2; k++)
		   {
              ini[j][k] = 1;
		   }
		}
	  } 

	  bool notdone = true;
	  long long count = 0;

	  while (notdone)
	  {
         notdone = false;
		 for (int i=1; i<=100; i++)
		 {
           for (int j=1; j<=100; j++)
		   {
              upd[i][j] = ini[i][j];  
              if (ini[i][j] == 1)
			  {
                if ( (ini[i-1][j] == 0) && (ini[i][j-1] == 0))
					upd[i][j] = 0;
				else
                    notdone = true;  
			  }
			  else
			  {
                if ((ini[i-1][j] == 1) && (ini[i][j-1] == 1))
				{
					upd[i][j] = 1;
                    notdone = true;
				}
			  }
		   }
		 }

		 count++;
		 if (notdone)
		 {
            memcpy(ini, upd, 12100*sizeof(int));
		 }
	  }

        fout << "Case #" << tt+1 << ": " << count << endl;
  }

   return 0;
}
