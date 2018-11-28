// codejam1D.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[])
{
    ifstream fin("D-large.in");
	ofstream fout("D-large.out");
    
    int i,j,k,n,t,sum;

	fin >> t;
	for (i=1;i<=t;i++){
      fin >> n;
	  sum=0;
      for (j=1;j<=n;j++){
		  fin >> k;
          sum+=(k==j?0:1);
      } 
	  fout << "Case #" << i << ": " << sum << ".000000" << endl;
	}
	fin.close();
	fout.close();
	return 0;
}

