#include "stdafx.h"
#include <stdio.h>



int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fin,*fout;
	__int64 T,R,k,N,pos,rides,size,money,started;
	__int64 g[1001];
	__int64 sinceVal[1001],sinceRid[1001];
	fin=fopen("c:\\test.in","r");
	fout=fopen("c:\\test.out","w");
	fscanf(fin,"%I64d",&T);
	
	for(__int64 h=0;h<T;h++){
	  fscanf(fin,"\n%I64d %I64d %I64d\n",&R,&k,&N);
	  pos=(N>1 ? 1 : 0);
	  rides=0;
	  money=0;
	  started=0;
	  for(__int64 x=0;x<N;x++){
	    sinceVal[x]=0;
	    sinceRid[x]=0;
		fscanf(fin,"%I64d ",&g[x]);
	  }
	  size=g[0];

	  //Starts passing
	  while(rides<R){
		  //if filled
		  if(size+g[pos] > k || pos==started){
			money+=size;
			rides++;
			if(sinceRid[pos]>0){
				__int64 vaheRides=rides-sinceRid[pos];
				__int64 vaheMoney=money-sinceVal[pos];
				__int64 loops=(R-rides)/vaheRides;
				money+=loops*vaheMoney;
				rides+=loops*vaheRides;
			}
		    sinceVal[pos]=money;
			sinceRid[pos]=rides;
			size=0;
			started=pos;
		  }

		  size+=g[pos];
		  pos++;
		  if(pos == N)
			pos=0;
	  }

	  fprintf(fout,"Case #%I64d: %I64d\n",h+1,money);
	}
	fclose(fin);
	fclose(fout);
}


