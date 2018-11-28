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

unsigned __int64 x;


long gcd(long p, long q, long *x, long *y)
{
  long x1,y1;			/* previous coefficients */
  long g;				/* value of gcd(p,q) */
  
  if (q > p) return(gcd(q,p,y,x));
  
  if (q == 0) {
    *x = 1;
    *y = 0;
    return(p);
  }
  
  g = gcd(q, p%q, &x1, &y1);
  
  *x = y1;
  *y = (x1 - floor(p/q)*y1);
  
  return(g);
}


int main(int argc, char* argv[])
{
  int numCases;
  int i,j,k,l,m;
  
  //ifstream fin("input.txt");FILE *f2 = fopen("output.txt","w");
  	//ifstream fin("A-large.in");FILE *f2 = fopen("A-large.out","w");
  	ifstream fin("A-small-attempt0.in");FILE *f2 = fopen("A-small-attempt0.out","w");
  //	ifstream fin("A-small-attempt1.in");FILE *f2 = fopen("A-small-attempt1.out","w");
  //	ifstream fin("A-small-attempt2.in");FILE *f2 = fopen("A-small-attempt2.out","w");
  //	ifstream fin("A-small-attempt3.in");FILE *f2 = fopen("A-small-attempt3.out","w");
  

 
  
  char temp[2000];
  fin >> numCases;
  fin.getline(temp,2000);
  for (i=0;i<numCases;++i)
  {
    
    fin.getline(temp,2000);
    strstream ss;
    bool impossible = false;
    ss << temp;
    long nmax;
    int pd, pg;
    ss >> nmax;
    ss >> pd;
    ss >> pg;
    
    long d1, d2;
    long g = 100/gcd(100,pd,&d1,&d2);
    if (g > nmax) impossible = true;
    
    if ((pg == 100) && (pd!= 100)) impossible = true;
    if ((pg == 0) && (pd!= 0)) impossible = true;


    //cout << "case " << i << ": " << step << endl;
    string result;
    if (impossible) result = "Broken";
    else result = "Possible";
    fprintf(f2,"Case #%d: %s\n",i+1,result.c_str());

     




  }
    
    
    
    
    
  
  return 0;	
}