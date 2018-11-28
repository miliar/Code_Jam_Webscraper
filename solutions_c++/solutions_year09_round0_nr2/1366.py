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

#define MA 100000 

using namespace std;


ofstream fout("oooo.txt");
ifstream fin ("iiii.in");

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


//sscanf(stringHM,"%d:%d",&h,&m);


 //fprintf(pFile, "Case #%d: ", t+1);
 //fprintf(pFile,"%d\n",res);

  int T;
  fin >> T;

  int xsink[28];
  int ysink[28];
  int elev[110][110];
  int from[110][110][4];
  int sinklab[110][110];
  int numsink;
  int mapLabel[28];

  for (int tt=0; tt<T; tt++)
  {
     numsink=0;
	 memset(xsink, 0, sizeof(xsink));
	 memset(ysink, 0, sizeof(ysink));
     memset(from, 0, sizeof(from));
     memset(sinklab, -1, sizeof(sinklab));
	 memset(mapLabel, -1, sizeof(mapLabel));

     for (int i=0; i<110; i++)
	 {
		 for (int j=0; j<110; j++)
		 {
            elev[i][j] = MA;
		 }
	 }

     int H, W;

	 int dirx[4] = {1,0, 0,-1};
	 int diry[4] = {0,1,-1, 0}; 

	 fin >> H >> W;

	 for (int i=0; i<H; i++)
	 {
       for (int j=0; j<W; j++)
	   {
          fin >> elev[i+1][j+1];
	   }
	 }

     for (int i=1; i<=H; i++)
	 {
        for (int j=1; j<=W; j++)
		{
           int bes = elev[i][j];
		   int curd = -1;
		   for (int k=0; k<4; k++)
		   {
 		      int curx = i - dirx[k];
		      int cury = j - diry[k];
              if (elev[curx][cury] < bes )
			  {
                 bes  = elev[curx][cury];
				 curd = k; 
			  }
		   }
		   if (curd != -1)
		   {
 		     int curx = i - dirx[curd];
		     int cury = j - diry[curd];             
             from[curx][cury][curd]=1;
		   }
		   else
		   {
              xsink[numsink]=i;
			  ysink[numsink]=j;
			  numsink++;
		   }
		}
	 }

	 for (int i=0; i<numsink; i++)
	 {
        sinklab[xsink[i]][ysink[i]]=i;
        queue <vector <int> > Q;
		vector <int> L;
		L.push_back(xsink[i]);
		L.push_back(ysink[i]);
		Q.push(L);
	    while (!Q.empty())
		{
           vector <int> cur = Q.front();
		   Q.pop();
           for (int j=0; j<4; j++)
		   {
              int xcur = cur[0];
			  int ycur = cur[1];
              if (from[xcur][ycur][j] == 1)
			  {
				  xcur = xcur + dirx[j];
				  ycur = ycur + diry[j];
				  if (sinklab[xcur][ycur] == -1)
				  {
                     L[0] = xcur;
					 L[1] = ycur;
					 Q.push(L);
					 sinklab[xcur][ycur]=i;
				  }
			  }
		   }
		}
	 }


if (1)
{

     fout << "Case #" << tt+1 << ": " << endl;



     int curlabel = 0;
	 for (int i=1; i<=H; i++)
	 {
        for (int j=1; j<=W; j++)
		{
           int presLab = sinklab[i][j]; 
           if (mapLabel[presLab] == -1)
		   {
              mapLabel[presLab] = curlabel;
			  curlabel++;
		   }
		   char c = (char) ( 'a' + mapLabel[presLab] );
		   fout << c;
		   if ( j != W )
		     fout << " ";
		}
		fout << endl;
	 }
}

  }

  if (0)
  {
   int cou = 0;
   for (int i=0; i<100; i++)
   {
     for (int j=0; j<100; j++)
	 {
       fout << cou;
	   cou++;
	   if ( j != 99 )
	     fout << " ";
	 }
	 fout << endl;
   }
  }

   return 0;
}
