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

vector <int> prim;
vector <vector<int> > con(1002);

int comp[1002];

int main() {

//FILE* pFile;
//pFile = fopen("ou.txt","w");

prim.clear();

prim.push_back(2);
  
int curPr = 2;
int j = 2;

int upperBound = 1002;

while (j <= upperBound )
{  
   bool fou = false;
   j = curPr+1;
   while (!fou)
   {
     bool locFou = false;
     for (int p=0; p<prim.size() && !locFou; p++)
     {
        if (j%prim[p] == 0)
        {
         locFou = true;
        }
     }
     if (locFou)
      j++;
     else
     {
      fou = true;
      curPr = j;
      if (j <= upperBound)
        prim.push_back(j);
      //cout << j << endl;
     }
   }
}


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

  memset(comp, -1, sizeof(comp));
	 
  int A, B, P;

  fin >> A >> B >> P;

  for (int j=A; j<=B; j++)
    comp[j] = j;

  for (int j=A; j<=B; j++)
  {
    con[j].clear();
	con[j].push_back(j);
  }

  for (int i=0; i<prim.size(); i++)
  {
    if (prim[i] >= P && prim[i] <= B)
	{
	  int curind = -1;	 
      for (int j=A; j<=B; j++)
	  {
        if (j%prim[i] == 0)
		{
          if (curind == -1)
		    curind = comp[j];
		  else
		  {
            int currr = comp[j]; 
            if (currr != curind)
			{
              for (int k=0; k<con[currr].size(); k++)
			  {
			    con[curind].push_back(con[currr][k]);
				comp[con[currr][k]]=curind;
			  }
			  con[currr].clear();
			}
		  }
		}
	  }
	}
  }

  int res = 0;

  for (int j=A; j<=B; j++)
  {
    if (!con[j].empty())
	  res++;
  }

  fout << "Case #" << tt+1 << ": " << res << endl;
}

   return 0;
}
