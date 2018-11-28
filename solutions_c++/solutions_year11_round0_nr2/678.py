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

int main(int argc, char* argv[])
{
  int numCases;

  
  //ifstream fin("input.txt");FILE *f2 = fopen("output.txt","w");
 	ifstream fin("B-large.in");FILE *f2 = fopen("B-large.out","w");
  //	ifstream fin("B-small-attempt0.in");FILE *f2 = fopen("B-small-attempt0.out","w");
  //	ifstream fin("B-small-attempt1.in");FILE *f2 = fopen("B-small-attempt1.out","w");
  //	ifstream fin("B-small-attempt2.in");FILE *f2 = fopen("B-small-attempt2.out","w");
  //	ifstream fin("B-small-attempt3.in");FILE *f2 = fopen("B-small-attempt3.out","w");
  

 
  int i;
  char temp[2000];
  fin >> numCases;
  fin.getline(temp,2000);
  for (i=0;i<numCases;++i)
  {
    int result[256][256];
    bool destroyer[256][256];
    vector<char> invokeArray;
    int j,k,l,m;
    for (j=0;j<256;++j)
    {
      for (k=0;k<256;++k)
      {
        result[j][k] = 0;
        destroyer[j][k] = false;
      }
      
    }
    
    fin.getline(temp,2000);
    strstream ss;
    ss << temp;
    int nComb, nOpposites, nInovkations;
    ss >> nComb;
    for (j=0;j<nComb;++j)
    {
      string tempCombo;
      char comb1, comb2, tresult;
      ss >> tempCombo;
      assert(tempCombo.length() == 3);
      comb1 = tempCombo[0];
      comb2 = tempCombo[1];
      tresult = tempCombo[2];

      result[comb1][comb2] = tresult;
      result[comb2][comb1] = tresult;
      
    }
    ss >> nOpposites;
    for (j=0;j<nOpposites;++j)
    { 
      string tempOpposites;
      ss >> tempOpposites;
      assert(tempOpposites.length() == 2);
      char opp1, opp2;
      opp1 = tempOpposites[0];
      opp2 = tempOpposites[1];
      destroyer[opp1][opp2] = true;
      destroyer[opp2][opp1] = true;

    }
    ss >> nInovkations;
    string invokestr;
    ss >> invokestr;
    assert(invokestr.length() == nInovkations);
    for (j=0;j<invokestr.length();++j)
    {
      char currentchar = invokestr[j];
      bool combined = false;
      invokeArray.push_back(currentchar);
      int ivend = invokeArray.size()-1;
      int ivend2 = invokeArray.size()-2;
      if (ivend2 >= 0) {
       
         if  (result[invokeArray[ivend2]] [invokeArray[ivend]])
         {
           combined = true;
           currentchar = result[invokeArray[ivend2]] [invokeArray[ivend]];
           invokeArray.push_back(currentchar);
           invokeArray.erase(invokeArray.begin()+ivend);
           invokeArray.erase(invokeArray.begin()+ivend2);
           
         }
      }
      if (!combined)
      {
        for (k=0;k<invokeArray.size()-1;++k)
        {
           if (destroyer[currentchar][invokeArray[k]])
           {
             invokeArray.clear();
             int cnum = invokeArray.size();
             break;

           }
        }
      }
      
    }

  
  //cout << "case " << i << ": " << step << endl;
    fprintf(f2,"Case #%d: [",i+1);
    int setsize = invokeArray.size(); 
    for (k=0;k<(setsize-1);++k)
    {
           fprintf(f2,"%c, ",invokeArray[k]);
    }
    if (setsize) fprintf(f2,"%c",invokeArray[setsize-1]);
    fprintf(f2,"]\n");



  }
    
    
    
    
    
  
  return 0;	
}