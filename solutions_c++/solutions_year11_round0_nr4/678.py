// round12p2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cassert>
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

double func(int x)
{
    return x;
}


int main(int argc, char* argv[])
{
  int numCases;
  
  
  //ifstream fin("input.txt");FILE *f2 = fopen("output.txt","w");
 	ifstream fin("D-large.in");FILE *f2 = fopen("D-large.out","w");
 //  	ifstream fin("D-small-attempt0.in");FILE *f2 = fopen("D-small-attempt0.out","w");
  //	ifstream fin("D-small-attempt1.in");FILE *f2 = fopen("D-small-attempt1.out","w");
  //	ifstream fin("D-small-attempt2.in");FILE *f2 = fopen("D-small-attempt2.out","w");
  //	ifstream fin("D-small-attempt3.in");FILE *f2 = fopen("D-small-attempt3.out","w");
  
  
  int i;
  char temp[20000];

  fin >> numCases;
  
  fin.getline(temp,20000);
 for (i=0;i<numCases;++i)
  {
    unsigned long swaps = 0;
    double result = 0;
    int inum;
    int j,k,l;
    int Numbers[1002];
    int covered[1002];
    for (j=0;j<1001;++j)
    {
      Numbers[j]=0;
      covered[j]=0;
    }

   
 
    fin.getline(temp,20000);
    strstream ss,ss2;
    ss << temp;
    ss >> inum;
    fin.getline(temp,20000);
    ss2 << temp;
    for (j=1;j<=inum;++j)
    {
      ss2 >> Numbers[j];
    }
    

    for (j=1; j <=inum; ++j)
    {
      if (covered[j]) continue;
      covered[j] = 1;
      int index = j;
      int circlelength = 1;
      while (Numbers[index]!=j)
      {
        index = Numbers[index];
        covered[index] = 1;
        ++circlelength;
      }
      if (circlelength>1) result += circlelength; 
    }
    fprintf(f2,"Case #%d: %.6lf\n",i+1,result);
     
    
    
  }
  
  
  
  
  
  
  return 0;	
}