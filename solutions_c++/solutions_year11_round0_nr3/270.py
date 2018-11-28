// codejam1B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[])
{
    ifstream fin("C-large.in");
	ofstream fout("C-large.out");
    
    long i,j,k,n,t,sum,min,bit;

	fin >> t;
	for (i=1;i<=t;i++){
      fin >> n;
	  bit=0; sum=0;
	  min=2147483647;
      for (j=1;j<=n;j++){
		  fin >> k;
          bit^=k;
		  sum+=k;
		  min=(k<=min?k:min);
      } 
	  fout << "Case #" << i << ": " ;
	  if(bit==0){
		  fout << sum-min << endl;
	  }else{
  		  fout << "NO" << endl;
	  }
	}
	fin.close();
	fout.close();
	return 0;
}

