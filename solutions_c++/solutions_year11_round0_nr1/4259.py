#include "stdlib.h"
#include "stdio.h"
#include "string.h"
#include "math.h"
#include "time.h"


//-- Main -----------------------------------------------------------------------
int main(int argc, char *argv[]) 
{
	FILE *f_in,*f_out;
	int N[100],T,P[100][100];
	char C[100][100];
	int time[100];
	int B[100];
	int O[100];
	int now[100];
	char prev;
	int BPlace=1,OPlace=1;
	
	f_out = fopen ("output.txt","w");
	f_in = fopen("input.txt","r");
	
	
	fscanf(f_in,"%d",&T);
	//printf("T:%d\n",T);
	
	for(int i=0;i<T;i++)
	{
		fscanf(f_in,"%d",&N[i]);
		//printf(" N:%d",N[i]);
		for(int j=0;j<N[i];j++)
		{
			fscanf(f_in," %c",&C[i][j]);
			//printf("C:%c ",C[i][j]);
			fscanf(f_in,"%d",&P[i][j]);
			//printf("P:%d ",P[i][j]);
		}
		//printf("\n\n",T);
		time[i]=0;
		

		BPlace=1;
		OPlace=1;

		for(int j=0;j<N[i];j++)
		{
			O[j]=0;
			B[j]=0;
			now[j]=0;
			if(C[i][j]=='B')
			{
				B[j]=abs(BPlace-P[i][j])+1;
				BPlace=P[i][j];
				
			}else if(C[i][j]=='O'){
				O[j]=abs(OPlace-P[i][j])+1;
				OPlace=P[i][j];
			}
			
		
		}
		
		int bsum=0;
		int osum=0;
		
		for(int j=0;j<N[i];j++)
		{
			if(O[j]==0)
			{
				if(bsum>=B[j])
				{
					now[j]=1;
					bsum=0;	
					osum=1;
				}
				else {
					now[j]=B[j]-bsum;
					osum=osum+now[j];
					bsum=0;
				}
			}
			if(B[j]==0)
			{
				if(osum>=O[j])
				{
					now[j]=1;
					osum=0;	
					bsum=1;
				}
				else {
					now[j]=O[j]-osum;
					bsum=bsum+now[j];
					osum=0;
				}
			}

			time[i]=time[i]+now[j];

		}
		
		
		
		
		fprintf(f_out,"Case #%d: %d\n", i+1,time[i]);
	}
	
	fclose(f_out);
	fclose(f_in);
};
