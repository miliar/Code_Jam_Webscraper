// round12p2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <strstream>
#include <map>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#define rep(i,a,b) for(i=a;i<b;i++)
#define repz(i,n) rep(i,0,n)


using namespace std;



int main(int argc, char* argv[])
{
  int numCases;
  int i,j,k,l,m;

  //ifstream fin("input.txt");FILE *f2 = fopen("output.txt","w");
  	ifstream fin("B-large.in");FILE *f2 = fopen("B-large.out","w");
  //	ifstream fin("B-small-attempt0.in");FILE *f2 = fopen("B-small-attempt0.out","w");
  //	ifstream fin("B-small-attempt1.in");FILE *f2 = fopen("B-small-attempt1.out","w");
  //	ifstream fin("B-small-attempt2.in");FILE *f2 = fopen("B-small-attempt2.out","w");
  //	ifstream fin("B-small-attempt3.in");FILE *f2 = fopen("B-small-attempt3.out","w");


  char temp[2000];
  fin >> numCases;
  fin.getline(temp,2000);
  for (i=0;i<numCases;++i)
  {
    int nsamples,surprises, maxnum, maxpossible;
    fin.getline(temp,2000);
    strstream ss;
    ss << temp;   
    ss >> nsamples;
     ss >> surprises;
    ss >> maxnum;
    maxpossible = 0;

    for (j=0;j<nsamples;++j)
    {
      int sample;
      ss >> sample;
      if (maxnum == 0) { ++maxpossible;continue;}
      if (sample == 0) continue;
      if (sample >= (3*maxnum-2)){ ++maxpossible;continue;}
      if ((sample >= (3*maxnum-4)) && (surprises>0)) {--surprises;++maxpossible;};
    }
    
    fprintf(f2,"Case #%d: %d\n",i+1,maxpossible);
  }
	
  return 0;	
}