#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <fstream.h>

#include <string.h>

using namespace std;

int main()
{
	int i, j, k, t1, tt;
	

	FILE *in,*out;
 	in=fopen("B-small-attempt2.in","r");
    out=fopen("B-small.out","w");	


	
	fscanf(in,"%d\n", &tt );
	for( t1 = 1; t1 <= tt; ++ t1 )
	{
		fprintf(out,"Case #%d: ", t1 );

					
		int N,S,P,num[100][100];
		j=0;i=0;
		
		fscanf(in,"%d %d %d",&N,&S,&P);
		
		int go[100][2];
		for(i=0; i<N; ++i)
		{
			go[i][0] = -1;
			go[i][1] = -1;
		}
		
		for(i=0;i<N;++i)
		{
			int arr[100], n=3;
			fscanf(in,"%d",&arr[i]);
			
			int d = arr[i]/n;
			int r = arr[i]%n;
			
			if(r==0)
			{
				if( (d<11) && (d > -1) )
				{
					go[i][0] = 0;
					num[j][1]=d;num[j][2]=d;num[j][3]=d;num[j][0]=-1;
					j++;
					if((d) >= P)
						go[i][0]=1;
				}
				if((d+1 < 11) && (d < 11) && (d-1 < 11) && (d-1 > -1) )
				{
					go[i][1] = 0;
					num[j][1]=d-1;num[j][2]=d;num[j][3]=d+1;num[j][0]=-2;
					j++;
					if((d+1) >= P)
						go[i][1]=1;
				}
			}
			else if(r==1)
			{
				if((d+1 < 11) && (d < 11)&& (d > -1) )
				{
					go[i][0] = 0;
					num[j][1]=d;num[j][2]=d;num[j][3]=d+1;num[j][0]=-1;
					j++;
					if((d+1) >= P)
						go[i][0]=1;
				}
				if((d+1 < 11) && (d-1 < 11) && (d-1 > -1) )
				{
					go[i][1] = 0;
					num[j][1]=d-1;num[j][2]=d+1;num[j][3]=d+1;num[j][0]=-2;
					j++;
					if((d+1) >= P)
						go[i][1]=1;
				}
			}
			else if(r==2)
			{
				if( (d < 11) && (d-1 < 11)&& (d-1 > -1) )
				{
					go[i][0] = 0;
					num[j][1]=d;num[j][2]=d+1;num[j][3]=d+1;num[j][0]=-1;
					j++;
					if((d+1) >= P)
						go[i][0]=1;
				}
				if( (d+2 < 11) && (d < 11) && (d > -1) )
				{
					go[i][1] = 0;
					num[j][1]=d;num[j][2]=d;num[j][3]=d+2;num[j][0]=-2;
					j++;
					if((d+2) >= P)
						go[i][1]=1;
				}
			}
		}
		
		int lls=0, ols=0, los=0,oos=0,r=0;
		
		for(i=0; i<N; ++i)
		{
			if( (go[i][0]==1) && go[i][1]==1)
				lls++;
			else if( (go[i][0]==1) && go[i][1]==0)
				los++;
			else if( (go[i][0]==0) && go[i][1]==1)
				ols++;
			else if( (go[i][0]==0) && go[i][1]==0)
				oos++;
			else if( (go[i][0]==1) && go[i][1]== -1)
				lls++;
			else if( (go[i][0]== -1) && go[i][1]== 1)
				ols++;
			else if( (go[i][0]== -1) && go[i][1]== 0)
				oos++;
				
			//fprintf(out,"\n!%d %d!\n", go[i][0],go[i][1] );	 	      	 	    	 
		} 
		
		if(ols >= S)
			r = S + lls + los;
		else 
		{
			if(ols + lls  >= S)
				r = ols + lls + los;
			else
			{
				r = ols + lls;
				int tem = S - (ols+lls);
				if(los >= tem)
					r = r + los-tem;
			}	 
		}
		/*if(t1==41)
		{
			for(int tem6 = 0; tem6<N; ++tem6)
			{
				fprintf(out,"!%d%d!",go[tem6][0],go[tem6][1] );
			}
		}*/
		fprintf(out,"%d\n", r );	
	}
	//input.close();outfile.close();
	fclose(in);fclose(out);
	
	
	return 0;
}

