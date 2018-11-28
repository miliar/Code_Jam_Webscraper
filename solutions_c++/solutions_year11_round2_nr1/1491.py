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


__int64 gcd(__int64 p, __int64 q, __int64 *x, __int64 *y)
{
  __int64 x1,y1;			/* previous coefficients */
  __int64 g;				/* value of gcd(p,q) */
  
  if (q > p) return(gcd(q,p,y,x));
  
  if (q == 0) {
    *x = 1;
    *y = 0;
    return(p);
  }
  
  g = gcd(q, p%q, &x1, &y1);
  
  *x = y1;
  *y = (x1 - floor((long double)(p/q))*y1);
  
  return(g);
}


int main(int argc, char* argv[])
{
  int numCases;
  int i,j,k,l,m;
  
  //ifstream fin("input.txt");FILE *f2 = fopen("output.txt","w");
  	ifstream fin("A-large.in");FILE *f2 = fopen("A-large.out","w");
  	//ifstream fin("A-large-practice.in");FILE *f2 = fopen("A-large-practice.out","w");
  //	ifstream fin("A-small-attempt0.in");FILE *f2 = fopen("A-small-attempt0.out","w");
  //	ifstream fin("A-small-attempt1.in");FILE *f2 = fopen("A-small-attempt1.out","w");
  //	ifstream fin("A-small-attempt2.in");FILE *f2 = fopen("A-small-attempt2.out","w");
  //	ifstream fin("A-small-attempt3.in");FILE *f2 = fopen("A-small-attempt3.out","w");
  

 
  
  char temp[20000];
  fin >> numCases;
  fin.getline(temp,20000);
  for (int ii=0;ii<numCases;++ii)
  {
    int NPlayers;
	int Win[101][101];
	int nWin[101],nLoss[101];
	double pWin[101],poWin[101][101],opoWin[101][101],foWin[101],fooWin[101];
    fin.getline(temp,20000);
    strstream ss;
    ss << temp;
	ss >> NPlayers;
	repz(i,NPlayers)
	{
		repz(j,NPlayers)
		Win[i][j] = -1;
		nWin[i]=0;
		nLoss[i]=0;
	}
	repz(i,NPlayers)
	{
		fin.getline(temp,20000);
		ss.flush();
		ss << temp;
		repz(j,NPlayers)
		{
           if (temp[j]=='0') {++nLoss[i];Win[i][j]=0; }
		   else if (temp[j]=='1') { ++nWin[i];Win[i][j]=1;};

		}
		pWin[i] = (double) nWin[i]/(double)(nWin[i]+nLoss[i]);
	}

	repz(i,NPlayers)
	{
		repz(j,NPlayers)
		{
			//leave out match between i,j
			poWin[i][j]=0;
			if (Win[i][j]==1){
				poWin[i][j]= (double) nWin[j]/(double)(nWin[j]+nLoss[j]-1);
			}
			if (Win[i][j]==0){
				poWin[i][j]= (double) (nWin[j]-1)/(double)(nWin[j]+nLoss[j]-1);
			}
		}
	}

	repz(i,NPlayers)
	{
		double sum = 0;
		repz(j,NPlayers)
		{
			sum += poWin[i][j];
		}
		foWin[i] = sum/(nWin[i]+nLoss[i]);
	}

	repz(i,NPlayers)
	{
		double sum = 0;
	
		repz(j,NPlayers){
			if (Win[i][j]>=0)
			{
				sum += foWin[j];
			}
		}
		fooWin[i]=sum/(nWin[i]+nLoss[i]);
	}




    fprintf(f2,"Case #%d:\n",ii+1);
	repz(i,NPlayers)
	{
		double rpi;
		rpi = 0.25*pWin[i]+0.5*foWin[i]+0.25*fooWin[i];
		fprintf(f2,"%.12lf\n",rpi);
	}

     




  }
    
    
 
    
  
  return 0;	
}