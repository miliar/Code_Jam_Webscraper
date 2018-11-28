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

	long long mo=10007;

	int xp[11];
	int yp[11];

	long long dp[103][103];
	bool poi[103][103];

	int h,w;

	long long comp(long long x, long long y)
	{
      if (dp[x][y] != -1)
	    return dp[x][y];
	  
	  if (x==w && y == h)
	  {
        dp[x][y]=1;
		return 1;
	  }

	  long long su1=0;
	  long long su2=0;

	  if (y+1 <= h && x+2 <= w && !poi[x+2][y+1])
        su1 = comp(x+2,y+1);
	  if (y+2 <= h && x+1 <= w && !poi[x+1][y+2])
        su2 = comp(x+1,y+2);
	  long long su3 = (su1+su2)%mo;
	  dp[x][y]=su3;
	  return su3;
	}

int main() {

//FILE* pFile;
//pFile = fopen("ou.txt","w");

int NN;

fin >> NN;

for (int tt=0; tt<NN; tt++)
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

  memset(xp, 0, sizeof(xp));
  memset(yp, 0, sizeof(yp));
  memset(dp, -1, sizeof(dp));
  memset(poi, false, sizeof(poi));

  int r;

  fin >> h >> w >> r;

  for (int i=0; i<r; i++)
  {
    fin >> yp[i] >> xp[i];
    poi[xp[i]][yp[i]]=true;
  }

  long long res = comp(1,1);

  fout << "Case #" << tt+1 << ": " << res << endl;
}

   return 0;
}
