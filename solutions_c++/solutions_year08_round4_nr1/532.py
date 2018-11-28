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

	int val[10003];
	bool cha[10003];

	int M;

int mmin(int a, int b)
{
  if (a < b)
   return a;
  else
   return b;
}

int comp(int ind, int des)
{
  if (2*(ind) + 1 > M)
  {
    if (des == val[ind])
	  return 0;
	else
	  return 20000;
  }

  if (cha[ind] == 0)
  {
    if (val[ind] == 1)
	{
      int res1 = comp(2*ind, des);
	  int res2 = comp(2*ind+1, des);
	  if (des == 0)
	   return (mmin(res1,res2));
	  else
       return (mmin(20000, res1+res2));
	}
	else
	{
      int res1 = comp(2*ind, des);
	  int res2 = comp(2*ind+1, des);
	  if (des == 0)
        return (mmin(20000,res1+res2));
	  else
	    return (mmin(res1,res2));
	}
  }
  else
  {
      int res1 = comp(2*ind, des);
	  int res2 = comp(2*ind+1, des);
	  int te1 = 0;
	  if (des == 0)
	   te1 = mmin(res1,res2);
	  else
       te1 = mmin(20000, res1+res2);
      int te2 = 0;
	  if (des == 0)
        te2 = mmin(20000,res1+res2);
	  else
	    te2 = mmin(res1,res2);

	if (val[ind] == 1)
	{
      int te3 = mmin(te1, te2+1);
	  return (mmin(20000, te3));
	}
	else
	{
      int te3 = mmin(te1+1, te2);
	  return (mmin(20000, te3));
	}
  }
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

 int V;
 memset(val, 0, sizeof(val));
 memset(cha, false, sizeof(cha));

 fin >> M >> V;

 for (int i=1; i< ((M-1)/2)+1; i++)
 {
   int tv = 0;
   int tc = 0;
   fin >> tv >> tc;
   if (tv == 1)
     val[i] = 1;
   if (tc == 1)
     cha[i] = true;
 }

 for (int i =((M-1)/2)+1; i < M+1; i++)
 {
   int tv = 0;
   fin >> tv;
   if (tv == 1)
     val[i] = 1;
 }

 int res = comp(1, V);

 if (res >= 20000)
   fout << "Case #" << tt+1 << ": " << "IMPOSSIBLE" << endl;
 else
  fout << "Case #" << tt+1 << ": " << res << endl;
}

   return 0;
}
