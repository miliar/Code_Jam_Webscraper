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



int main(int argc, char* argv[])
{
  int numCases;

  
  //ifstream fin("input.txt");FILE *f2 = fopen("output.txt","w");
 	ifstream fin("C-large.in");FILE *f2 = fopen("C-large.out","w");
 // 	ifstream fin("C-small-attempt0.in");FILE *f2 = fopen("C-small-attempt0.out","w");
  //	ifstream fin("C-small-attempt1.in");FILE *f2 = fopen("C-small-attempt1.out","w");
  //	ifstream fin("C-small-attempt2.in");FILE *f2 = fopen("C-small-attempt2.out","w");
  //	ifstream fin("C-small-attempt3.in");FILE *f2 = fopen("C-small-attempt3.out","w");
  

 
  int i;
  char temp[20000];
  fin >> numCases;
  
  fin.getline(temp,20000);
  for (i=0;i<numCases;++i)
  {
    int inum, Numbers[1001];
     unsigned long sum = 0;
    int max = -1;
    int min = 100000000;
    int j,k,l;
    bool impossible = false;
    for (j=0;j<1001;++j) Numbers[j] =0;
   
    fin.getline(temp,20000);
    strstream ss,ss2;
    ss << temp;
    ss >> inum;
    fin.getline(temp,20000);
    ss2 << temp;
    for (j=0;j<inum;++j)
    {
      ss2 >> Numbers[j];
      if (Numbers[j]>max)  max = Numbers[j];
      if (Numbers[j]<min)  min = Numbers[j];
      sum += Numbers[j]; 
     
    }
    cout << (sum -min) << endl;
    int iteration = 0;
    while (max > 0)
    {
      iteration++;
      int sumparity = 0;
      max = max / 2;
      for (j=0;j<inum;++j)
      {
        sumparity += (Numbers[j]%2);
        //printf("Number - %d, sumparity - %d, inum= %d\n",Numbers[j],sumparity,inum);
        Numbers[j] = (Numbers[j]/2);
      }
      if (sumparity%2) 
      {
        //printf("Iteration:%d Parity%d\n",iteration,sumparity);
        impossible = true;
        break;
      }

    }



    if (impossible) fprintf(f2,"Case #%d: NO\n",i+1);
    else fprintf(f2,"Case #%d: %d\n",i+1,sum-min);
   


  }
    
    
    
    
    
  
  return 0;	
}