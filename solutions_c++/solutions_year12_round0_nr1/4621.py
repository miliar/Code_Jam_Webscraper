// GCJ2012R1P1.cpp : Defines the entry point for the console application.
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

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
  char transform[256];
  bool  transformed[256];

  int numCases;
  int i,j,k,l,m;

  for (i=0;i<255;++i){transform[i]=i;transformed[i]=false;}
char t1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi\0";
char t2[] =  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\0";
char t3[] =  "de kr kd eoya kw aej tysr re ujdr lkgc jv\0";

char o1[] = "our language is impossible to understand\0";
char o2[] = "there are twenty six factorial possibilities\0";
char o3[] = "so it is okay if you want to just give up\0";

for (i=0;i<strlen(t1);++i)
{
  transform[t1[i]]=o1[i];
  transformed[t1[i]] = true;
}

for (i=0;i<strlen(t2);++i)
{
  transform[t2[i]]=o2[i];
   transformed[t2[i]] = true;
}

for (i=0;i<strlen(t3);++i)
{
  transform[t3[i]]=o3[i];
   transformed[t3[i]] = true;
}

transform['z']='q';
transform['q']='z';
transform[0]=0;
transform[' ']=' ';

//	ifstream fin("A-large.in");FILE *f2 = fopen("A-large.out","w");
//	ifstream fin("A-small-attempt0.in");FILE *f2 = fopen("A-small-attempt0.out","w");
//	ifstream fin("A-small-attempt1.in");FILE *f2 = fopen("A-small-attempt1.out","w");
//	ifstream fin("A-small-attempt2.in");FILE *f2 = fopen("A-small-attempt2.out","w");
//	ifstream fin("A-small-attempt3.in");FILE *f2 = fopen("A-small-attempt3.out","w");
  	ifstream fin("A-small-attempt4.in");FILE *f2 = fopen("A-small-attempt4.out","w");
  fin >> numCases;
  	char temp[2000];
  fin.getline(temp,2000);
  for (i=0;i<numCases;++i)
  {
    unsigned long Nsnpappers,Ksnaps;
    fin.getline(temp,2000);

     for (j=0;j<strlen(temp);++j)
     {
       temp[j]=transform[temp[j]];
     }
    fprintf(f2,"Case #%d: %s\n",i+1,temp);
  
    }
  for (i=0;i<255;++i)printf("%d  %d %d\n",i,transformed[i],transform[i]);
	return 0;
}

