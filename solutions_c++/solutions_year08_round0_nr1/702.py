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

using namespace std;


    ofstream fout("ou.txt");
    //ofstream fout ("fence4.out");
    //ifstream fin ("fence4.in");
    ifstream fin ("beads.txt");

	//FILE* pFile;
    //int c;
    //pFile = fopen("ou.txt","w");
    //pFile=fopen ("beads.txt","r");

map <string, int> M;
vector <vector<int> > nex(103);


int main() {

FILE* pFile;
pFile = fopen("ou.txt","w");

int N;

fin >> N;

for (int t=0; t<N; t++)
{
  M.clear();
  for (int i=0; i<102; i++)
     nex[i].clear();

  string na;

  if (t == 0)
   getline(fin,na);

  int s, q;
  fin >> s;
  getline(fin,na);

  for (int i=0; i<s; i++)
  {
    getline(fin,na);
	M[na]=i;
  }

  fin >> q;
  getline(fin,na);

  for (int i=0; i<q; i++)
  {
    getline(fin,na);
	nex[M[na]].push_back(i);
  }

  for (int i=0; i<s; i++)
    nex[i].push_back(q+1);

  int res = 0;
  bool done = false;
  int last = -1;
  while (!done)
  {
    int lo=-1;
	int lind = -1;
	bool early = false;
	for (int i=0; i<s && !early; i++)
	{
     if (last != i)
	 {
      if (nex[i][0] == q+1)
	    early = true;
	  else
	  {
        if (nex[i][0] > lo)
		{
          lo = nex[i][0];
		  lind = i;
		}
	  }
	 }
	}

	  if (early)
		  done = true;
	  else
	  {
	    last = lind;
        res++;
		for (int j=0; j<s; j++)
		{
           int x = nex[j][0];
		   while (x <= lo)
		   {
             nex[j].erase(nex[j].begin());
			 x = nex[j][0];
		   }
		}
	  }
  }
 
 //fprintf(pFile, "Case #%d: ", t+1);
 //fprintf(pFile,"%d\n",res);

  fout << "Case #" << t+1 << ": " << res << endl;
}

   return 0;
}
