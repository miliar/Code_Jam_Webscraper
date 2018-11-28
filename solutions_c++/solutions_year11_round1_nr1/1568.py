// codejam1A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
using namespace std;

int main(int argc, char* argv[])
{
    ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
    
    int pd,pg,t, i, j, k, b, d, y;
	long n;

	fin >> t;
	for (i=1;i<=t;i++){
      fin >> n;
	  fin >> pd;
	  fin >> pg;
      
	  b=1;
      
	  if (pg==100){
		  if (pd<100) {
			  b=0;
		  }
	  }else	if (pg==0){
		  if (pd>0) {
			  b=0;
		  }
	  }else{
          if ((n>0)&&(n<=100)){
			  b=0;
			  for (d=1;d<=n;d++){
				  for (y=0;y<=d;y++){
					  if (pd*d==100*y){
						  b=1;
					  }
				  }
			  }
		  }
	  }
      fout << "Case #" << i << ": " << ((b==1)?"Possible":"Broken") << endl;
    }
	fin.close();
	fout.close();
	return 0;
}

