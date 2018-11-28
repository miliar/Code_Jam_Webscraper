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
#define rep(i,a,b) for(i=a;i<b;i++)
#define repz(i,n) rep(i,0,n)
/*#define MAXN 100
//Binomial functions typed from Programming Challenges  - Skiena, Revilla
long bc[MAXN][MAXN];
long binomial_cofficient(int n,int m)
{
   int i,j;
   repz(i,n+1) bc[i][0] = 1;
   repz(j,n+1) bc[j][j] = 1;

   rep(i,1,n+1)
	   rep(j,1,i)
			bc[i][j] = bc[i-1][j-1] + bc[i-1][j];
   return bc[n][m];
}
*/

using namespace std;


int main(int argc, char* argv[])
{
	int numCases;
	int i,j,k,l,m;
	ifstream fin("input.txt");
	FILE *f2 = fopen("output.txt","w");
	char temp[2000];
	fin >> numCases;
	fin.getline(temp,2000);

	for (i=0;i<numCases;++i)
	//repz(i,numCases);
	{
		fin.getline(temp,2000);
		strstream ss;
		ss << temp;
		int tbase;
		ss >> tbase;
		double sx,sy,sz,svx,svy,svz;
		sx = 0;
		sy = 0;
		sz = 0;
		svx = 0;
		svy = 0;
		svz = 0;
		rep(j,0,tbase)
		{
			fin.getline(temp,2000);
			strstream ss1;
			ss1 << temp;
			int tempi;
			ss1 >> tempi;
			sx += tempi;
			ss1 >> tempi;
			sy += tempi;
			ss1 >> tempi;
			sz += tempi;
			ss1 >> tempi;
			svx += tempi;
			ss1 >> tempi;
			svy += tempi;
			ss1 >> tempi;
			svz += tempi;
		}
		double ix,iy,iz,ivx,ivy,ivz;
		ix = sx/tbase;
		iy = sy/tbase;
		iz = sz/tbase;
		ivx = svx/tbase;
		ivy = svy/tbase;
		ivz = svz/tbase;
		double dx =0 ;
		double dy =0 ;
		double dz =0 ;
		
		double t = -(ivx*ix+ivy*iy+ivz*iz)/(ivx*ivx+ivy*ivy+ivz*ivz);
		if (t < 0) t = 0;

		dx = ix+ivx*t;
		dy = iy+ivy*t;
		dz = iz+ivz*t;
		double d;
		d = sqrt(dx*dx+dy*dy+dz*dz);
				fprintf(f2,"Case #%d: %0.8f %0.8f\n",i+1,d,t);
	
	}

	return 0;
}

