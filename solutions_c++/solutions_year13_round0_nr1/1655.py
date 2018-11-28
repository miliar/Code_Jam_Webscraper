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
char board[4][4];



string Process()
{
  int i,j,k;
  int numDots = 0;
  bool XWon,OWon;
  for (i=0;i<4;++i)
    for (j=0;j<4;++j)
    {
      if (board[i][j]=='.') ++numDots;
    }

    //Look at all rows for winners
    for (i=0;i<4;++i)
    {
      XWon = true;OWon=true;
      for (j=0;j<4;++j)
      {
         if ((board[i][j]=='.') ||(board[i][j]=='O')) XWon = false;
         if ((board[i][j]=='.') ||(board[i][j]=='X')) OWon = false;
      }
      if (XWon) return "X won" ;
      if (OWon) return "O won";
    }

    //Look at all Columns for winners
    for (j=0;j<4;++j)
    {
      XWon = true;OWon=true;
      for (i=0;i<4;++i)
      {
        if ((board[i][j]=='.') ||(board[i][j]=='O')) XWon = false;
        if ((board[i][j]=='.') ||(board[i][j]=='X')) OWon = false;
      }
      if (XWon) return "X won" ;
      if (OWon) return "O won";
    }

    XWon = true;OWon=true;
    //Look at first diagonal
    for (i=0;i<4;++i)
    { 
        if ((board[i][i]=='.') ||(board[i][i]=='O')) XWon = false;
        if ((board[i][i]=='.') ||(board[i][i]=='X')) OWon = false;
     
    }
    if (XWon) return "X won" ;
    if (OWon) return "O won";
    
    XWon = true;OWon=true;
    //Look at the other diagonal
    for (i=0;i<4;++i)
    { 
      if ((board[i][4-i-1]=='.') ||(board[i][4-i-1]=='O')) XWon = false;
      if ((board[i][4-i-1]=='.') ||(board[i][4-i-1]=='X')) OWon = false;
      
    }
    if (XWon) return "X won" ;
    if (OWon) return "O won";


    if (numDots == 0) return "Draw";

  return "Game has not completed";
}

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
    
    for (j=0;j<4;++j)
    {
      fin.getline(temp,2000);
      strstream ss;
      ss << temp;
      for (k=0;k<4;++k)
      {
        ss>>board[j][k];
      }

    }
    if (i<(numCases-1))fin.getline(temp,2000);

    string result = Process();
    fprintf(f2,"Case #%d: %s\n",i+1,result.c_str());

  }
    
    
    
    
    
  
  return 0;	
}


