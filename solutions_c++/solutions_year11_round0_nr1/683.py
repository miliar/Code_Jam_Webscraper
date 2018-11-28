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
  int i,j,k,l,m;
  
  //ifstream fin("input.txt");FILE *f2 = fopen("output.txt","w");
  	ifstream fin("A-large.in");FILE *f2 = fopen("A-large.out","w");
  //	ifstream fin("A-small-attempt0.in");FILE *f2 = fopen("A-small-attempt0.out","w");
  //	ifstream fin("A-small-attempt1.in");FILE *f2 = fopen("A-small-attempt1.out","w");
  //	ifstream fin("A-small-attempt2.in");FILE *f2 = fopen("A-small-attempt2.out","w");
  //	ifstream fin("A-small-attempt3.in");FILE *f2 = fopen("A-small-attempt3.out","w");
  

 
  
  char temp[2000];
  fin >> numCases;
  fin.getline(temp,2000);
  for (i=0;i<numCases;++i)
  {
    vector<int> path;
    vector<int> pathO;
    vector<int> pathB;

   
    char color;
    int ncount, button;
    fin.getline(temp,2000);
    strstream ss;
    ss << temp;
    ss >> ncount;
    for (j=0;j<ncount;++j)
    {
      ss >> color;
      ss >> button;
      //cout << "Color : " << color << "Button : " << button << endl;
      if (color == 'O') pathO.push_back(button);
      if (color =='B') button = button + 200;
      path.push_back(button);
      if (color == 'B') pathB.push_back(button);
      
    }
    bool done = false;
    k = 0;
    int kb = 0, ko = 0, step = 0;

    int buttonO = 1, buttonB = 201;
    int targetB = -1, targetO = -1, target = -1;
    if (pathB.size() > kb) {
        targetB = pathB[kb];
    }
    if (pathO.size() > ko) {
      targetO = pathO[ko];
    }
    if (path.size() > k) {
      target = path[k];
    }


    while (!done)
    {
      bool bpush = false, opush = false;
       ++step;
       //cout << target  << " target B = " << targetB << " target O : "<< targetO << " positionB - " << buttonB << " positionO " << buttonO << endl;
      
        if (target == targetB)
        {
          if (buttonB == targetB)
          {
            //push buttonB now;
            ++k;
            ++kb;
            bpush = true;
            if (pathB.size() > kb) {
              targetB = pathB[kb];
            }
            if (path.size() > k) {
              target = path[k];
            }
            else done = true;
          }

        }
        else 
        {
          assert(target == targetO);
          if (buttonO == targetO)
            {
              //push buttonO now;
              ++k;
              ++ko;
              opush = true;
              if (pathO.size() > ko) {
                targetO = pathO[ko];
              }
              if (path.size() > k) {
                target = path[k];
              }
              else done = true;
            }
           


        }
       
  if (!opush)
  {
       if (buttonO > targetO) --buttonO;
       if (buttonO < targetO) ++buttonO; 
  }

  if (!bpush)
  {
       if (buttonB > targetB) --buttonB;
       if (buttonB < targetB) ++buttonB; 
  }   





    }


    //cout << "case " << i << ": " << step << endl;
    fprintf(f2,"Case #%d: %d\n",i+1,step);

     




  }
    
    
    
    
    
  
  return 0;	
}