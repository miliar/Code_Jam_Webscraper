#include "stdafx.h"
#include "stdio.h"


bool snappers[30];

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fin,*fout;
	int T,x,N,K,y;
	fin=fopen("c:\\jaanus\\codejam\\task1\\task1\\A-small.in","r");
	fout=fopen("c:\\jaanus\\codejam\\task1\\task1\\A-small.out","w");
	fscanf(fin,"%d\n",&T);
	
	for(int h=0;h<T;h++){
	  fscanf(fin,"%d %d\n",&N,&K);

	  //preset
	  for(x=0;x<N;x++){
		snappers[x]=false;
	  }

	  for(x=0;x<K;x++){
		  for(y=0;y<N;y++){
			  if(!snappers[y]){
				  snappers[y]=!snappers[y];
				  break;
			  }
			  snappers[y]=!snappers[y];
		  }
	  }

	  //check
	  for(y=0;y<N;y++){
		  if(!snappers[y]){
			  fprintf(fout,"Case #%d: OFF\n",h+1);
			  break;
		  }
	  }
	  if(y==N){
	    fprintf(fout,"Case #%d: ON\n",h+1);
	  }
	}
  
}

