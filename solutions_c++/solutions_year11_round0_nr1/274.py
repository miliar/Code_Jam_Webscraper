// codejam1A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[])
{
    ifstream fin("A-large.in");
	ofstream fout("A-large.out");
    
    int i,j,k1,k2,k,n,sum,p,m,f,x,y,t;
	char r,c[120];
	int a[120];

	fin >> t;
	for (i=1;i<=t;i++){
      fin >> n;
      for (j=1;j<=n;j++){
		  fin >> c[j];
		  fin >> a[j];
      } 
      p=1; sum=0; x=1; y=1;
      k1=0; k2=0; k=0; m=0; f=0;
	  r=c[p];
	  while (p<=n){
		  while ((c[p]==r)&&(p<=n)){
			  m+=abs(a[p]-(c[p]=='O'?x:y))+1;
              x=(c[p]=='O'?a[p]:x);
			  y=(c[p]=='B'?a[p]:y);
		      p++;
		  }
		  if (p<=n){
            f=abs(a[p]-(c[p]=='O'?x:y))+1;
			x=(c[p]=='O'?a[p]:x);
			y=(c[p]=='B'?a[p]:y);
            if(f<=m){
               sum+=m;
			   f=0;
			   m=1;
			   r=c[p];
			   p++;
			}else{
               sum+=m;
			   m=f-m;
			   r=c[p];
			   f=0;
			   p++;
			}
		  }
	  }	  
	  sum+=m; m=0;
	  fout << "Case #" << i << ": " << sum << endl;
	}
	fin.close();
	fout.close();
	return 0;
}

