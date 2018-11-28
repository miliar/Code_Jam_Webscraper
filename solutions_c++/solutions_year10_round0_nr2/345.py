#include "stdafx.h"
#include <stdio.h>
#include <math.h>
#include <string>
#include <iostream>
#include "BigIntegerLibrary.hh"

//http://mattmccutchen.net/bigint/ library was used


BigInteger  common(BigInteger  in1, BigInteger  in2){
	
  BigInteger  a=(in1>in2 ? in1 : in2);
  BigInteger  b=(in1<in2 ? in1 : in2);
  if(b==0)
	return 1;
  BigInteger  c=a%b;
  while(c>0){
	  a=b;
	  b=c;
	  if(b==0)
		return 1;
	  c=a%b;
  }
  return b;
}


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fin,*fout;
	int C,N,x;
	char input[200];
	BigInteger t[1001],min,T;
	fin=fopen("c:\\test.in","r");
	fout=fopen("c:\\test.out","w");
	fscanf(fin,"%d\n",&C);
	
	for(int h=0;h<C;h++){
	  printf("CASE %d\n",h+1);
	  min=stringToBigInteger("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999");
	  fscanf(fin,"%d ",&N);
	  for(x=0;x<N;x++){
		fscanf(fin,"%s ",input);
		t[x]=stringToBigInteger(input);
		if(t[x]<min)
			min=t[x];
	  }
		
	  T=0;
	  for(x=1;T==0 && x<N;x++)
	    T=t[x]-t[0];
	  if(T<0)
		T=T-T-T;
	  for(x=0;x<N;x++){		  
		if(t[x]!=min && ((t[x]-min)%T)>0){
		  T=common(T,t[x]-min);
		}
	  }

	  min=min-min-min;
	  while(min<0)
		  min=min+T;

	  fprintf(fout,"Case #%d: %s\n",h+1,bigIntegerToString(min).c_str());
	}
	fclose(fin);
	fclose(fout);
}

